"""Regresiones del validador sobre un catálogo temporal; no modifica web/www."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from validate_data import validate


class ValidateDataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hexatour-validator-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "www"
        self.index = {"version": 1, "categories": [{"id": "campings", "label": "Campings", "count": 1}]}
        self.listing = {"category": "campings", "label": "Campings",
                        "items": [{"slug": "camping1", "name": "Lugar de ejemplo"}]}
        self.poi = {"slug": "camping1", "name": "Lugar de ejemplo", "category": "campings",
                    "fields": {key: "ejemplo" for key in
                               ("descripcion", "tpie", "tveh", "apertura", "cierre", "alertas")},
                    "route": {"text": "Indicaciones de ejemplo"},
                    "images": {"main": "img/campings/main.jpg", "route": "img/campings/route.jpg"}}
        self.save()
        for name in ("main.jpg", "route.jpg"):
            path = self.root / "img/campings" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            # El validador comprueba presencia; decodificación pertenece a la revisión gráfica.
            path.write_bytes(b"fixture")

    def write(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def save(self):
        self.write("db/index.json", self.index)
        self.write("db/categories/campings.json", self.listing)
        self.write("db/poi/campings/camping1.json", self.poi)

    def assertInvalid(self, fragment):
        errors, _ = validate(self.root)
        self.assertTrue(errors)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_minimum_and_empty_optional_text(self):
        self.poi["route"]["text"] = ""
        self.poi["fields"]["alertas"] = ""
        self.save()
        errors, stats = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(stats, {"categories": 1, "pois": 1, "image_references": 2})

    def test_names_can_repeat_with_distinct_slugs(self):
        self.index["categories"][0]["count"] = 2
        self.listing["items"].append({"slug": "camping2", "name": self.poi["name"]})
        other = copy.deepcopy(self.poi)
        other["slug"] = "camping2"
        self.save()
        self.write("db/poi/campings/camping2.json", other)
        self.assertEqual(validate(self.root)[0], [])

    def test_optional_variant_when_declared_must_exist(self):
        self.poi["images"]["main_640"] = "img/campings/missing.jpg"
        self.save()
        self.assertInvalid("missing.jpg")
        (self.root / "img/campings/missing.jpg").write_bytes(b"fixture")
        self.assertEqual(validate(self.root)[0], [])

    def test_missing_main_image(self):
        (self.root / "img/campings/main.jpg").unlink()
        self.assertInvalid("main.jpg")

    def test_missing_route_image(self):
        (self.root / "img/campings/route.jpg").unlink()
        self.assertInvalid("route.jpg")

    def test_missing_poi(self):
        (self.root / "db/poi/campings/camping1.json").unlink()
        self.assertInvalid("camping1.json")

    def test_orphan_poi(self):
        self.write("db/poi/campings/unlisted.json", self.poi)
        self.assertInvalid("ficha no listada")

    def test_undeclared_category_list(self):
        self.write("db/categories/unlisted.json", self.listing)
        self.assertInvalid("lista no declarada")

    def test_undeclared_poi_directory(self):
        (self.root / "db/poi/unlisted").mkdir()
        self.assertInvalid("entrada fuera")

    def test_exact_case_even_on_windows(self):
        self.poi["images"]["main"] = "img/campings/Main.jpg"
        self.save()
        self.assertInvalid("capitalización")

    def test_invalid_json_utf8_bom_duplicate_keys_and_constants(self):
        path = self.root / "db/index.json"
        for data in (b"{", b"\xff", b"\xef\xbb\xbf{}", b'{"version":1,"version":2}', b'{"version":NaN}'):
            with self.subTest(data=data):
                path.write_bytes(data)
                self.assertInvalid("no se pudo leer JSON")

    def test_malformed_shapes_and_inconsistent_references(self):
        cases = [
            ("index", [], "no es un objeto"),
            ("index", {"version": True, "categories": []}, "version"),
            ("index", {"version": 1, "categories": {}}, "lista no vacía"),
            ("index", {"version": 1, "categories": [None]}, "sin id válido"),
            ("listing", {**self.listing, "items": {}}, "items debe ser lista"),
            ("listing", {**self.listing, "items": [None]}, "item requiere"),
            ("listing", {**self.listing, "category": "otra"}, "no coinciden"),
            ("listing", {**self.listing, "label": "Otro"}, "no coinciden"),
            ("poi", [], "no es un objeto"),
            ("poi", {**self.poi, "slug": "camping2"}, "'slug' no coincide"),
            ("poi", {**self.poi, "name": "Otro lugar"}, "'name' no coincide"),
            ("poi", {**self.poi, "category": "otra"}, "'category' no coincide"),
            ("poi", {**self.poi, "fields": None}, "'fields' no es un objeto"),
            ("poi", {**self.poi, "fields": {**self.poi["fields"], "tpie": 5}}, "fields.tpie"),
            ("poi", {**self.poi, "fields": {}}, "fields.descripcion"),
            ("poi", {**self.poi, "route": {"text": []}}, "route.text"),
            ("poi", {**self.poi, "images": []}, "'images' no es un objeto"),
            ("poi", {**self.poi, "images": {"main": self.poi["images"]["main"]}}, "falta imagen 'route'"),
        ]
        paths = {"index": "db/index.json", "listing": "db/categories/campings.json",
                 "poi": "db/poi/campings/camping1.json"}
        for target, data, fragment in cases:
            with self.subTest(target=target, data=data):
                self.save()
                self.write(paths[target], data)
                self.assertInvalid(fragment)

    def test_duplicate_category_and_slug(self):
        self.index["categories"].append(copy.deepcopy(self.index["categories"][0]))
        self.save()
        self.assertInvalid("categoría duplicada")
        self.index["categories"].pop()
        self.listing["items"].append(copy.deepcopy(self.listing["items"][0]))
        self.save()
        self.assertInvalid("slug duplicado")

    def test_counts_are_integers_and_match_both_sets(self):
        for value in (True, -1, "1", 1.0, 2):
            with self.subTest(count=value):
                self.index["categories"][0]["count"] = value
                self.save()
                self.assertInvalid("count")

    def test_identifiers_cannot_escape_directories(self):
        for value in ("../outside", "/tmp", "Campings", "camp ings", "camp\\ings", ""):
            with self.subTest(identifier=value):
                self.index["categories"][0]["id"] = value
                self.save()
                self.assertInvalid("sin id válido")

    def test_image_paths_cannot_escape_or_use_urls(self):
        for value in ("img/../../outside.jpg", "img/../main.jpg", "img//main.jpg", "img/./main.jpg",
                      "/img/main.jpg", "https://example.com/image.jpg", "C:/outside.jpg",
                      "img/campings/main.jpg?x=1", "img/campings/main.jpg#x", "img/%2e%2e/outside.jpg",
                      "img/campings\\main.jpg"):
            with self.subTest(image=value):
                self.poi["images"]["main"] = value
                self.save()
                self.assertInvalid("ruta")

    def test_symlink_outside_root(self):
        outside = Path(self.temp.name) / "outside.jpg"
        outside.write_bytes(b"fixture")
        link = self.root / "img/campings/link.jpg"
        try:
            link.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"Este sistema no permite crear symlinks de prueba: {exc}")
        self.poi["images"]["main"] = "img/campings/link.jpg"
        self.save()
        self.assertInvalid("fuera de la raíz")

    def test_missing_root(self):
        self.assertTrue(validate(self.root / "missing")[0])

    def test_cli_returns_content_failure_without_traceback(self):
        script = Path(__file__).with_name("validate_data.py")
        command = [sys.executable, "-B", str(script), "--root", str(self.root)]
        valid = subprocess.run(command, cwd=self.temp.name, capture_output=True)
        self.assertEqual(valid.returncode, 0, valid.stdout + valid.stderr)
        (self.root / "img/campings/route.jpg").unlink()
        invalid = subprocess.run(command, cwd=self.temp.name, capture_output=True)
        self.assertEqual(invalid.returncode, 1, invalid.stdout + invalid.stderr)
        self.assertIn(b"route.jpg", invalid.stdout)
        self.assertNotIn(b"Traceback", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
