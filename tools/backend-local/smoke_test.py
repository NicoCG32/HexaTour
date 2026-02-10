import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request


def http_get(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status, resp.read()


def read_json(url: str) -> dict:
    status, body = http_get(url)
    if status != 200:
        raise RuntimeError(f"{url} -> HTTP {status}")
    return json.loads(body.decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="HexaTour local backend smoke test")
    parser.add_argument("--base", default="http://localhost:8000")
    args = parser.parse_args()

    base = args.base.rstrip("/")
    ok = True

    def check(name: str, fn):
        nonlocal ok
        try:
            fn()
            print(f"[ok] {name}")
        except Exception as exc:  # noqa: BLE001
            ok = False
            print(f"[fail] {name}: {exc}")

    def check_health():
        data = read_json(f"{base}/api/health")
        if data.get("status") != "ok":
            raise RuntimeError("status != ok")

    def check_categories_and_poi():
        data = read_json(f"{base}/api/categories")
        cats = data.get("items") or []
        if not cats:
            raise RuntimeError("no categories")

        cat = cats[0]
        items = read_json(f"{base}/api/pois?cat={urllib.parse.quote(cat)}").get("items") or []
        if not items:
            raise RuntimeError("no pois for category")

        slug = items[0].get("slug")
        if not slug:
            raise RuntimeError("poi without slug")

        poi = read_json(
            f"{base}/api/poi?cat={urllib.parse.quote(cat)}&slug={urllib.parse.quote(slug)}"
        ).get("item")
        if not poi:
            raise RuntimeError("poi not found")

    def check_print_and_pdf():
        data = read_json(f"{base}/api/categories")
        cat = (data.get("items") or [""])[0]
        if not cat:
            raise RuntimeError("no category")
        items = read_json(f"{base}/api/pois?cat={urllib.parse.quote(cat)}").get("items") or []
        slug = (items[0] or {}).get("slug") if items else ""
        if not slug:
            raise RuntimeError("no poi slug")

        status, body = http_get(
            f"{base}/api/print-ruta?cat={urllib.parse.quote(cat)}&slug={urllib.parse.quote(slug)}"
        )
        if status != 200:
            raise RuntimeError("print endpoint failed")
        if b"accepted" not in body:
            raise RuntimeError("unexpected print response")

        status, body = http_get(
            f"{base}/api/route-pdf?cat={urllib.parse.quote(cat)}&slug={urllib.parse.quote(slug)}"
        )
        if status != 200 or not body.startswith(b"%PDF"):
            raise RuntimeError("invalid pdf")

    check("health", check_health)
    check("categories/poi", check_categories_and_poi)
    check("print/pdf", check_print_and_pdf)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
