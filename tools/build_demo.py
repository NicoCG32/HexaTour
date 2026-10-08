#!/usr/bin/env python3
"""Prepara una copia estática con demo forzada; nunca modifica el portal fuente."""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
import re
import shutil
import sys
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "test"))
from validate_data import local_path, validate

ENTRIES = ("index.html", "main/index.html", "main/lugar.html",
           "visitor/index.html", "visitor/lugar.html")
ASSETS = tuple("assets/js/" + name + ".js" for name in
               ("common", "landing", "main-index", "main-lugar", "visitor-index", "visitor-lugar")) + tuple(
                   "assets/css/" + name + ".css" for name in ("base", "landing", "main", "visitor"))
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".svg"}
MODE = '<meta name="hexatour-mode" content="demo"/>'
SMS_LINE = "  const URGENCIA_SMS = { phone: '', punto: '' };"
SMS_DECLARATION = re.compile(r"(?m)^  const URGENCIA_SMS = \{[^\r\n]*\};\r?$")


class PageContract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.heads = 0
        self.common = False
        self.modes = []
        self.resources = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "head":
            self.heads += 1
        if tag == "script" and attrs.get("src", "").endswith("assets/js/common.js"):
            self.common = True
        if tag == "meta" and attrs.get("name") == "hexatour-mode":
            self.modes.append(attrs.get("content"))
        resource = attrs.get("src") if tag in ("img", "script") else (
            attrs.get("href") if tag == "link" and attrs.get("rel") == "stylesheet" else None)
        if resource:
            self.resources.append(resource)


def demo_html(content: str) -> str:
    page = PageContract()
    page.feed(content)
    if page.heads != 1 or not page.common or page.modes:
        raise ValueError("Cada entrada requiere un head, common.js y ninguna marca demo previa")
    result, count = re.subn(r"<head\s*>", lambda _: "<head>\n" + MODE, content, count=1, flags=re.I)
    if count != 1:
        raise ValueError("No se pudo insertar modo demo en head")
    return result


def build(source: Path, output: Path) -> dict:
    source, output = source.resolve(), output.resolve()
    if output == source or source in output.parents or output in source.parents:
        raise ValueError("La salida debe estar separada del portal fuente")
    if output.exists():
        raise ValueError("La salida ya existe; elegir una carpeta nueva con --output")
    errors, stats = validate(source)
    if errors:
        raise ValueError("Contenido inválido:\n" + "\n".join(errors))
    paths = list(source.rglob("*"))
    if any(path.is_symlink() for path in paths):
        raise ValueError("El portal fuente no debe contener enlaces simbólicos")
    html_paths = {p.relative_to(source).as_posix() for p in paths if p.suffix.lower() == ".html"}
    if html_paths != set(ENTRIES):
        raise ValueError("Las entradas HTML deben coincidir con las cinco páginas del portal")
    selected = set(ENTRIES + ASSETS)
    selected.add("db/index.json")
    catalog = json.loads((source / "db/index.json").read_text(encoding="utf-8"))
    for category in catalog["categories"]:
        listing_path = f"db/categories/{category['id']}.json"
        selected.add(listing_path)
        listing = json.loads((source / listing_path).read_text(encoding="utf-8"))
        selected.update(f"db/poi/{category['id']}/{item['slug']}.json" for item in listing["items"])
    selected.update(p.relative_to(source).as_posix() for p in paths if p.is_file() and (
        p.relative_to(source).parts[0] == "img" and p.suffix.lower() in IMAGE_SUFFIXES
    ) and not any(part.startswith(".") for part in p.relative_to(source).parts))
    prepared = {}
    source_hash = hashlib.sha256()
    for relative in sorted(selected):
        path = local_path(source, relative, errors)
        if path is None:
            continue
        content = path.read_bytes()
        source_hash.update(relative.encode("utf-8") + b"\0" + hashlib.sha256(content).digest())
        if relative in ENTRIES:
            html = content.decode("utf-8")
            page = PageContract()
            page.feed(html)
            for reference in page.resources:
                url = urlsplit(reference)
                target = posixpath.normpath(posixpath.join(posixpath.dirname(relative), url.path))
                if url.scheme or url.netloc or target not in selected:
                    raise ValueError(f"{relative}: recurso HTML fuera del artefacto: {reference}")
            prepared[relative] = demo_html(html).encode("utf-8")
        elif relative == "assets/js/visitor-lugar.js":
            sanitized, count = SMS_DECLARATION.subn(lambda _: SMS_LINE, content.decode("utf-8"))
            if count != 1:
                raise ValueError("No se reconoce la declaración de URGENCIA_SMS; revisar antes de empaquetar")
            prepared[relative] = sanitized.encode("utf-8")
    if errors:
        raise ValueError("\n".join(errors))
    common = (source / "assets/js/common.js").read_text(encoding="utf-8")
    if "meta[name=\"hexatour-mode\"]" not in common:
        raise ValueError("common.js no reconoce el modo del artefacto")
    license_path = ROOT / "LICENSE"
    if license_path.is_symlink():
        raise ValueError("La licencia del proyecto no debe ser un enlace simbólico")
    license_content = license_path.read_bytes()
    selected.add("LICENSE.txt")
    prepared["LICENSE.txt"] = license_content
    source_hash.update(b"LICENSE.txt\0" + hashlib.sha256(license_content).digest())
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".hexatour-demo-", dir=output.parent) as scratch:
        # La limpieza automática queda limitada a una carpeta nueva bajo el padre elegido.
        if Path(scratch).resolve().parent != output.parent:
            raise ValueError("Carpeta temporal fuera del padre de salida")
        stage = Path(scratch) / "site"
        stage.mkdir()
        for relative in sorted(selected):
            destination = stage / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if relative in prepared:
                destination.write_bytes(prepared[relative])
            else:
                shutil.copyfile(source / relative, destination)
        errors, _ = validate(stage)
        if errors:
            raise ValueError("Artefacto inválido:\n" + "\n".join(errors))
        (stage / ".nojekyll").write_text("", encoding="utf-8")
        files = {p.relative_to(stage).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in sorted(stage.rglob("*")) if p.is_file()}
        manifest = {"mode": "demo", "entries": list(ENTRIES), "sms_configured": False,
                    "source_sha256": source_hash.hexdigest(), "catalog": stats, "files": files}
        (stage / "demo-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                                                 encoding="utf-8")
        stage.rename(output)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "web/www", help="Raíz web fuente")
    parser.add_argument("--output", type=Path, default=ROOT / "dist/demo", help="Carpeta nueva para el artefacto")
    args = parser.parse_args()
    try:
        manifest = build(args.source, args.output)
    except (ValueError, OSError, UnicodeError) as exc:
        print(f"[fail] {exc}")
        return 1
    print(f"[ok] Demo preparada en {args.output.resolve()}: {len(manifest['entries'])} entradas, "
          f"{len(manifest['files']) + 1} archivos; SMS vacío.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
