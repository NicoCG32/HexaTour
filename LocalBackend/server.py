import argparse
import json
import os
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs


ROOT = Path(__file__).resolve().parents[1]


def safe_join(root: Path, rel: str) -> Path:
    rel = rel.lstrip("/")
    rel = rel.replace("..", "")
    return (root / rel).resolve()


def read_poi(db_root: Path, category: str, slug: str) -> dict | None:
    path = db_root / "db" / "poi" / category / f"{slug}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def build_pdf(title: str, body: str) -> bytes:
    # Minimal PDF for local testing
    lines = [title] + ["Indicaciones:"] + [ln or " " for ln in body.splitlines()]
    lines = lines[:40]
    content = ["BT", "/F1 16 Tf 50 780 Td (" + pdf_escape(lines[0]) + ") Tj", "/F1 12 Tf 0 -24 Td (" + pdf_escape(lines[1]) + ") Tj", "0 -18 Td"]
    for line in lines[2:]:
        content.append("(" + pdf_escape(line) + ") Tj")
        content.append("0 -14 Td")
    content.append("ET")
    content_str = "\n".join(content) + "\n"

    header = "%PDF-1.4\n%\xE2\xE3\xCF\xD3\n"
    o1 = "1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
    o2 = "2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
    o3 = "3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj\n"
    o4 = f"4 0 obj << /Length {len(content_str)} >> stream\n{content_str}endstream\nendobj\n"
    o5 = "5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n"

    cur = len(header)
    off1 = cur; cur += len(o1)
    off2 = cur; cur += len(o2)
    off3 = cur; cur += len(o3)
    off4 = cur; cur += len(o4)
    off5 = cur; cur += len(o5)

    xref = "xref\n0 6\n0000000000 65535 f \n" + "\n".join([
        f"{off1:010d} 00000 n ",
        f"{off2:010d} 00000 n ",
        f"{off3:010d} 00000 n ",
        f"{off4:010d} 00000 n ",
        f"{off5:010d} 00000 n ",
    ]) + "\n"
    trailer = f"trailer << /Size 6 /Root 1 0 R >>\nstartxref\n{cur}\n%%EOF\n"

    return (header + o1 + o2 + o3 + o4 + o5 + xref + trailer).encode("latin-1")


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class Handler(BaseHTTPRequestHandler):
    server_version = "HexaTourLocal/1.0"

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/":
            path = "/visitor/index.html"
        elif path == "/main":
            path = "/main/"
        if path.endswith("/"):
            path += "index.html"

        if path.startswith("/api/print-ruta"):
            self.handle_print(qs)
            return
        if path.startswith("/api/route-pdf"):
            self.handle_pdf(qs)
            return

        self.serve_static(path)

    def serve_static(self, path: str):
        root = self.server.www_root
        fs_path = safe_join(root, path)
        if not fs_path.exists() or not fs_path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")
            return
        ctype = self.guess_type(fs_path.suffix)
        content = fs_path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def handle_print(self, qs):
        category = qs.get("cat", [""])[0]
        slug = qs.get("slug", [""])[0]
        file_ref = qs.get("file", [""])[0]
        if (not category or not slug) and file_ref:
            if "/" in file_ref:
                category, slug = file_ref.split("/", 1)
        if not category or not slug:
            self.send_error(HTTPStatus.BAD_REQUEST, "cat y slug requeridos")
            return

        poi = read_poi(self.server.www_root, category, slug)
        if not poi:
            self.send_error(HTTPStatus.NOT_FOUND, "poi no encontrado")
            return
        route_text = (poi.get("route") or {}).get("text", "")
        if not route_text:
            self.send_error(HTTPStatus.NOT_FOUND, "ruta no encontrada")
            return

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"print job accepted (local)\n")

    def handle_pdf(self, qs):
        category = qs.get("cat", [""])[0]
        slug = qs.get("slug", [""])[0]
        name = qs.get("name", [""])[0]
        file_ref = qs.get("file", [""])[0]
        if (not category or not slug) and file_ref:
            if "/" in file_ref:
                category, slug = file_ref.split("/", 1)
        if not category or not slug:
            self.send_error(HTTPStatus.BAD_REQUEST, "cat y slug requeridos")
            return

        poi = read_poi(self.server.www_root, category, slug)
        if not poi:
            self.send_error(HTTPStatus.NOT_FOUND, "poi no encontrado")
            return
        if not name:
            name = poi.get("name", slug)
        route_text = (poi.get("route") or {}).get("text", "")
        if not route_text:
            self.send_error(HTTPStatus.NOT_FOUND, "ruta no encontrada")
            return

        pdf = build_pdf(f"Ruta: {name}", route_text)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/pdf")
        self.send_header("Content-Length", str(len(pdf)))
        self.send_header("Content-Disposition", f"attachment; filename=\"ruta-{slug}.pdf\"")
        self.end_headers()
        self.wfile.write(pdf)

    def guess_type(self, suffix: str) -> str:
        return {
            ".html": "text/html; charset=utf-8",
            ".css": "text/css",
            ".js": "application/javascript",
            ".json": "application/json; charset=utf-8",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
            ".svg": "image/svg+xml",
            ".ico": "image/x-icon",
        }.get(suffix.lower(), "application/octet-stream")


class LocalHTTPServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, www_root: Path):
        super().__init__(server_address, RequestHandlerClass)
        self.www_root = www_root


def main():
    parser = argparse.ArgumentParser(description="HexaTour local backend")
    parser.add_argument("--root", default=str(WWW_DEFAULT()), help="Path to www")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    www_root = Path(args.root).resolve()
    if not www_root.exists():
        raise SystemExit(f"www path not found: {www_root}")

    server = LocalHTTPServer(("0.0.0.0", args.port), Handler, www_root)
    print(f"Local backend on http://localhost:{args.port}")
    server.serve_forever()


def WWW_DEFAULT() -> Path:
    return ROOT / "Frontend (Interfaz)" / "www"


if __name__ == "__main__":
    main()
