"""Regresiones del arranque CLI y selección de contenido del mock local."""
from contextlib import contextmanager
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import URLError
from urllib.request import urlopen

REPO = Path(__file__).resolve().parent.parent
SERVER = REPO / "tools/backend-local/server.py"


@contextmanager
def running_backend(cwd, *args):
    with socket.socket() as available:
        available.bind(("127.0.0.1", 0))
        port = available.getsockname()[1]
    with tempfile.TemporaryFile() as log:
        process = subprocess.Popen(
            [sys.executable, "-B", "-u", str(SERVER), "--port", str(port), *args],
            cwd=cwd, stdout=log, stderr=log)
        base = f"http://127.0.0.1:{port}"
        try:
            deadline = time.monotonic() + 10
            while True:
                if process.poll() is not None:
                    log.seek(0)
                    raise AssertionError(log.read().decode("utf-8", errors="replace"))
                try:
                    with urlopen(base + "/api/health", timeout=1) as response:
                        if json.load(response).get("status") == "ok":
                            break
                except (URLError, TimeoutError):
                    if time.monotonic() >= deadline:
                        raise AssertionError("El mock no inició en diez segundos")
                    time.sleep(0.05)
            yield base
        finally:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)


class BackendLocalTests(unittest.TestCase):
    def test_default_content_from_repository_and_external_directory(self):
        with tempfile.TemporaryDirectory(prefix="hexatour-backend-") as external:
            for cwd in (REPO, external):
                with self.subTest(cwd=str(cwd)):
                    with running_backend(cwd) as base:
                        with urlopen(base + "/visitor/", timeout=5) as response:
                            self.assertEqual(response.read(), (REPO / "web/www/visitor/index.html").read_bytes())
                        smoke = subprocess.run(
                            [sys.executable, "-B", str(REPO / "tools/backend-local/smoke_test.py"), "--base", base],
                            cwd=cwd, capture_output=True, text=True, timeout=15)
                        self.assertEqual(smoke.returncode, 0, smoke.stdout + smoke.stderr)
                        self.assertEqual(smoke.stdout.count("[ok]"), 3)

    def test_explicit_relative_root_overrides_default(self):
        with tempfile.TemporaryDirectory(prefix="hexatour-backend-") as external:
            custom = Path(external) / "contenido"
            custom.mkdir()
            expected = b"<h1>Contenido alternativo de prueba</h1>"
            (custom / "index.html").write_bytes(expected)
            with running_backend(external, "--root", "contenido") as base:
                with urlopen(base + "/index.html", timeout=5) as response:
                    self.assertEqual(response.read(), expected)


if __name__ == "__main__":
    unittest.main()
