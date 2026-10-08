"""Regresiones de la distribución estática; fuentes y salidas sólo temporales."""
import hashlib
import json
from pathlib import Path
import posixpath
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from build_demo import ASSETS, ENTRIES, MODE, PageContract, SMS_LINE, build


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class BuildDemoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hexatour-build-")
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / "www"
        self.output = Path(self.temp.name) / "demo"
        for relative in ENTRIES + ASSETS:
            self.write(relative, (ROOT / "web/www" / relative).read_bytes())
        for relative in ENTRIES:
            page = PageContract()
            page.feed((self.source / relative).read_text(encoding="utf-8"))
            for reference in page.resources:
                asset = posixpath.normpath(posixpath.join(posixpath.dirname(relative), reference))
                if asset.startswith("img/"):
                    self.write(asset, (ROOT / "web/www" / asset).read_bytes())
        self.write_json("db/index.json", {"version": 1, "categories": [
            {"id": "campings", "label": "Campings", "count": 1}]})
        self.write_json("db/categories/campings.json", {"category": "campings", "label": "Campings",
            "items": [{"slug": "camping1", "name": "Ejemplo"}]})
        self.write_json("db/poi/campings/camping1.json", {"slug": "camping1", "name": "Ejemplo",
            "category": "campings", "fields": {key: "" for key in
                ("descripcion", "tpie", "tveh", "apertura", "cierre", "alertas")},
            "route": {"text": ""}, "images": {"main": "img/campings/main.jpg", "route": "img/campings/route.jpg"}})
        self.write("img/campings/main.jpg", b"fixture")
        self.write("img/campings/route.jpg", b"fixture")

    def write(self, relative, content):
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def write_json(self, relative, content):
        self.write(relative, json.dumps(content).encode("utf-8"))

    def test_all_entries_are_demo_and_manifest_matches_without_source_changes(self):
        for relative in (".env", "img/.private.json", "db/notas.txt", "db/private.json", "img/main.jpg.gz",
                         "firmware/secret.ino", "assets/js/local-config.js"):
            self.write(relative, b"local only")
        before = snapshot(self.source)
        manifest = build(self.source, self.output)
        self.assertEqual(before, snapshot(self.source))
        for relative in ENTRIES:
            html = (self.output / relative).read_text(encoding="utf-8")
            page = PageContract()
            page.feed(html)
            self.assertEqual(page.modes, ["demo"])
            self.assertIn(MODE, html)
        for relative, digest in manifest["files"].items():
            self.assertEqual(hashlib.sha256((self.output / relative).read_bytes()).hexdigest(), digest)
        self.assertEqual(set(snapshot(self.output)), set(manifest["files"]) | {"demo-manifest.json"})
        self.assertEqual((self.output / "LICENSE.txt").read_bytes(), (ROOT / "LICENSE").read_bytes())
        self.assertFalse((self.output / ".env").exists())
        self.assertFalse((self.output / "firmware").exists())
        self.assertFalse((self.output / "assets/js/local-config.js").exists())
        self.assertFalse((self.output / "db/private.json").exists())

    def test_local_sms_is_cleared_in_copy_and_crlf_is_supported(self):
        path = self.source / "assets/js/visitor-lugar.js"
        configured = path.read_text(encoding="utf-8").replace(SMS_LINE,
            "  const URGENCIA_SMS = { phone: '+12025550123', punto: 'Ejemplo local' };")
        path.write_bytes(configured.replace("\n", "\r\n").encode("utf-8"))
        before = path.read_bytes()
        build(self.source, self.output)
        result = (self.output / "assets/js/visitor-lugar.js").read_text(encoding="utf-8")
        self.assertIn(SMS_LINE, result)
        self.assertNotIn("+12025550123", result)
        self.assertNotIn("Ejemplo local", result)
        self.assertEqual(path.read_bytes(), before)

    def test_existing_output_and_source_overlap_are_rejected(self):
        self.output.mkdir()
        sentinel = self.output / "keep.txt"
        sentinel.write_text("keep", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ya existe"):
            build(self.source, self.output)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")
        for target in (self.source, self.source / "demo", self.source.parent):
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "separada"):
                build(self.source, target)

    def test_bad_catalog_is_rejected_without_partial_output(self):
        (self.source / "img/campings/main.jpg").unlink()
        with self.assertRaisesRegex(ValueError, "Contenido inválido"):
            build(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_unrecognized_sms_declaration_is_rejected(self):
        path = self.source / "assets/js/visitor-lugar.js"
        path.write_text(path.read_text(encoding="utf-8").replace(SMS_LINE, "  const URGENCIA_SMS = {}; // editado"),
                        encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "No se reconoce"):
            build(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_unknown_html_entry_is_rejected(self):
        self.write("visitor/extra.html", b"<html></html>")
        with self.assertRaisesRegex(ValueError, "cinco páginas"):
            build(self.source, self.output)

    def test_missing_html_image_is_rejected(self):
        (self.source / "img/map/logoHexaTour.png").unlink()
        with self.assertRaisesRegex(ValueError, "recurso HTML fuera"):
            build(self.source, self.output)

    def test_build_is_reproducible_for_same_source(self):
        build(self.source, self.output)
        second = self.output.with_name("demo-second")
        build(self.source, second)
        self.assertEqual(snapshot(self.output), snapshot(second))


if __name__ == "__main__":
    unittest.main()
