#!/usr/bin/env python3
"""Valida catálogo, listas, fichas y recursos de web/www sin dependencias externas.

Uso: python test/validate_data.py [--root web/www]
Salida: 0 si el conjunto es coherente; 1 si hay errores de contenido.
Evolución del validador inicial: lectura JSON, campos POI y conteos por categoría.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IDENTIFIER = re.compile(r"[a-z0-9]+")
REQUIRED_POI_FIELDS = ("slug", "name", "category")
REQUIRED_IMAGE_FIELDS = ("main", "route")
DISPLAY_FIELDS = ("descripcion", "tpie", "tveh", "apertura", "cierre", "alertas")


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def local_path(root: Path, relative: str, errors: list[str], kind: str = "file") -> Path | None:
    """Comprueba ruta relativa, capitalización exacta y destino dentro de la raíz."""
    parts = relative.split("/")
    if (relative != relative.strip() or any(p in ("", ".", "..") for p in parts)
            or any(c in relative for c in "\\:%?#")):
        fail(errors, f"{relative!r}: ruta local inválida")
        return None
    current = root
    try:
        for part in parts:
            if not current.is_dir() or part not in {p.name for p in current.iterdir()}:
                fail(errors, f"{relative}: falta recurso o capitalización incorrecta")
                return None
            current = current / part
            if not current.resolve().is_relative_to(root):
                fail(errors, f"{relative}: destino fuera de la raíz web")
                return None
        valid = current.is_file() if kind == "file" else current.is_dir()
        if not valid:
            fail(errors, f"{relative}: se esperaba {kind}")
            return None
    except (OSError, RuntimeError) as exc:
        fail(errors, f"{relative}: no se pudo comprobar ({exc})")
        return None
    return current


def json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"clave JSON duplicada: {key}")
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError(f"constante no válida en JSON: {value}")


def load_json(root: Path, relative: str, errors: list[str]) -> dict | None:
    path = local_path(root, relative, errors)
    if path is None:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=json_object,
                          parse_constant=invalid_constant)
    except (OSError, UnicodeError, ValueError) as exc:
        fail(errors, f"{relative}: no se pudo leer JSON UTF-8 sin BOM ({exc})")
        return None
    if not isinstance(data, dict):
        fail(errors, f"{relative}: no es un objeto JSON")
        return None
    return data


def text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def identifier(value) -> bool:
    return isinstance(value, str) and IDENTIFIER.fullmatch(value) is not None


def validate_poi_file(root: Path, category: str, slug: str, name: str,
                      errors: list[str]) -> int:
    relative = f"db/poi/{category}/{slug}.json"
    data = load_json(root, relative, errors)
    if data is None:
        return 0
    for field in REQUIRED_POI_FIELDS:
        if not text(data.get(field)):
            fail(errors, f"{relative}: falta campo '{field}' (texto no vacío)")
    for field, expected in (("slug", slug), ("category", category), ("name", name)):
        if data.get(field) != expected:
            fail(errors, f"{relative}: '{field}' no coincide con lista/carpeta/archivo")
    fields = data.get("fields")
    if not isinstance(fields, dict):
        fail(errors, f"{relative}: 'fields' no es un objeto")
    else:
        for field in DISPLAY_FIELDS:
            if not isinstance(fields.get(field), str):
                fail(errors, f"{relative}: fields.{field} debe ser texto")
    route = data.get("route")
    if not isinstance(route, dict) or not isinstance(route.get("text"), str):
        fail(errors, f"{relative}: route.text debe ser texto")
    images = data.get("images")
    if not isinstance(images, dict):
        fail(errors, f"{relative}: 'images' no es un objeto")
        return 0
    for field in REQUIRED_IMAGE_FIELDS:
        if field not in images:
            fail(errors, f"{relative}: falta imagen '{field}'")
    for field, value in images.items():
        if not text(value) or not value.startswith("img/"):
            fail(errors, f"{relative}: images.{field} debe ser ruta local bajo img/")
            continue
        local_path(root, value, errors)
    return len(images)


def json_files(directory: Path | None) -> set[str]:
    return {p.name for p in directory.iterdir() if p.suffix.lower() == ".json"} if directory else set()


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    stats = {"categories": 0, "pois": 0, "image_references": 0}
    if not root.is_dir():
        fail(errors, f"No se encontró la raíz web: {root}")
        return errors, stats
    index = load_json(root, "db/index.json", errors)
    if index is None:
        return errors, stats
    if type(index.get("version")) is not int or index["version"] < 1:
        fail(errors, "db/index.json: version debe ser entero positivo")
    categories = index.get("categories")
    if not isinstance(categories, list) or not categories:
        fail(errors, "db/index.json: categories debe ser lista no vacía")
        return errors, stats
    seen = set()
    for cat in categories:
        if not isinstance(cat, dict) or not identifier(cat.get("id")):
            fail(errors, "db/index.json: categoría sin id válido (letras minúsculas y números)")
            continue
        category = cat["id"]
        if category in seen:
            fail(errors, f"db/index.json: categoría duplicada '{category}'")
            continue
        seen.add(category)
        stats["categories"] += 1
        if not text(cat.get("label")):
            fail(errors, f"{category}: label debe ser texto no vacío")
        count = cat.get("count")
        if type(count) is not int or count < 0:
            fail(errors, f"{category}: count debe ser entero no negativo")
        listing = load_json(root, f"db/categories/{category}.json", errors)
        directory = local_path(root, f"db/poi/{category}", errors, "directory")
        actual = json_files(directory)
        if listing is None:
            continue
        if listing.get("category") != category or listing.get("label") != cat.get("label"):
            fail(errors, f"{category}: category/label de la lista no coinciden con el catálogo")
        items = listing.get("items")
        if not isinstance(items, list):
            fail(errors, f"{category}: items debe ser lista")
            continue
        if count != len(items) or count != len(actual):
            fail(errors, f"{category}: count={count}, lista={len(items)}, fichas={len(actual)}")
        slugs = set()
        for item in items:
            if not isinstance(item, dict) or not identifier(item.get("slug")) or not text(item.get("name")):
                fail(errors, f"{category}: item requiere slug válido y name no vacío")
                continue
            slug = item["slug"]
            if slug in slugs:
                fail(errors, f"{category}: slug duplicado '{slug}'")
                continue
            slugs.add(slug)
            stats["pois"] += 1
            stats["image_references"] += validate_poi_file(root, category, slug, item["name"], errors)
        for filename in sorted(actual - {f"{slug}.json" for slug in slugs}):
            fail(errors, f"db/poi/{category}/{filename}: ficha no listada o nombre de archivo incorrecto")
    lists_dir = local_path(root, "db/categories", errors, "directory")
    for filename in sorted(json_files(lists_dir) - {f"{category}.json" for category in seen}):
        fail(errors, f"db/categories/{filename}: lista no declarada en el catálogo")
    poi_root = local_path(root, "db/poi", errors, "directory")
    if poi_root:
        for path in sorted(poi_root.iterdir()):
            if path.name not in seen:
                fail(errors, f"db/poi/{path.name}: entrada fuera de las categorías del catálogo")
    return errors, stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT / "web/www", help="Raíz del sitio, no de db/")
    args = parser.parse_args()
    errors, stats = validate(args.root)
    for error in errors:
        print(f"[fail] {error}")
    print(f"Resumen: {stats['categories']} categorías, {stats['pois']} POI, "
          f"{stats['image_references']} referencias de imágenes.")
    if errors:
        print(f"Errores encontrados: {len(errors)}")
        return 1
    print("[ok] Catálogo, listas, fichas y recursos coherentes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
