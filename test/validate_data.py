#!/usr/bin/env python3
"""Valida la coherencia de los datos del portal cautivo (web/www/db).

No requiere dependencias externas: corre con el Python del sistema.

    python test/validate_data.py

Verifica:
  - Que index.json sea valido y tenga categorias.
  - Que cada POI tenga los campos obligatorios (slug, name, category,
    images.main) y que su carpeta coincida con su categoria.
  - Que el conteo de cada categoria en index.json coincida con la
    cantidad real de archivos POI en web/www/db/poi/<categoria>/.

Sale con codigo 1 si hay errores; 0 si todo esta bien.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # HexaTour/
DB = ROOT / "web" / "www" / "db"

REQUIRED_POI_FIELDS = ("slug", "name", "category")
REQUIRED_IMAGE_FIELDS = ("main",)


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)
    print(f"[fail] {msg}")


def load_json(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        fail([], f"{path.relative_to(ROOT)}: no se pudo leer ({exc})")
        return None


def validate_poi_file(path: Path, category: str, errors: list[str]) -> None:
    data = load_json(path)
    if not isinstance(data, dict):
        fail(errors, f"{path.relative_to(ROOT)}: no es un objeto JSON")
        return

    for field in REQUIRED_POI_FIELDS:
        if not isinstance(data.get(field), str) or not data[field].strip():
            fail(errors, f"{path.relative_to(ROOT)}: falta campo '{field}' (texto)")

    if data.get("category") != category:
        fail(
            errors,
            f"{path.relative_to(ROOT)}: category='{data.get('category')}' "
            f"no coincide con la carpeta '{category}'",
        )

    images = data.get("images")
    if not isinstance(images, dict):
        fail(errors, f"{path.relative_to(ROOT)}: 'images' no es un objeto")
    else:
        for img in REQUIRED_IMAGE_FIELDS:
            if not isinstance(images.get(img), str) or not images[img].strip():
                fail(errors, f"{path.relative_to(ROOT)}: falta imagen '{img}'")


def main() -> int:
    errors: list[str] = []

    if not DB.exists():
        fail(errors, f"No se encontro la carpeta de datos: {DB.relative_to(ROOT)}")
        return 1

    index = load_json(DB / "index.json")
    if not isinstance(index, dict) or not isinstance(index.get("categories"), list):
        fail(errors, "index.json: sin lista de categorias")
        return 1

    poi_root = DB / "poi"
    total_pois = 0

    for cat in index["categories"]:
        cat_id = cat.get("id")
        if not isinstance(cat_id, str) or not cat_id:
            fail(errors, f"Categoria sin 'id' valido: {cat!r}")
            continue

        poi_dir = poi_root / cat_id
        if not poi_dir.is_dir():
            fail(errors, f"Falta carpeta de POIs para '{cat_id}' ({poi_dir.relative_to(ROOT)})")
            continue

        poi_files = sorted(poi_dir.glob("*.json"))
        actual = len(poi_files)
        total_pois += actual

        declared = cat.get("count")
        if declared != actual:
            fail(
                errors,
                f"Categoria '{cat_id}': index cuenta {declared}, "
                f"pero hay {actual} archivos POI",
            )

        for poi_file in poi_files:
            validate_poi_file(poi_file, cat_id, errors)

    print(f"\nResumen: {len(index['categories'])} categorias, {total_pois} POIs.")
    if errors:
        print(f"Errores encontrados: {len(errors)}")
        return 1

    print("[ok] Todos los datos son coherentes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
