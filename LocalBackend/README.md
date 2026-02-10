# Local Backend (Mock)

Servidor local para probar el frontend sin ESP32. Sirve los archivos de `www` y expone endpoints mock basados en los JSON de `www/db`.

## Uso

Desde la raiz del repo:

```bash
python LocalBackend/server.py --root "Frontend (Interfaz)/www" --port 8000
```

Luego abre:
- Visitante: http://localhost:8000/visitor/
- Operador: http://localhost:8000/main/

## Endpoints mock

- `GET /api/health` -> estado basico del servidor.
- `GET /api/categories` -> lista de categorias disponibles (nombres de archivos en `db/categories`).
- `GET /api/category-items?cat=campings` -> items de una categoria (lee `db/categories/<cat>.json`).
- `GET /api/pois?cat=campings` -> lista de POIs con `slug` y `name`.
- `GET /api/poi?cat=campings&slug=camping1` -> POI completo.
- `GET /api/poi/campings/camping1` -> mismo que arriba, via path.
- `GET /api/print-ruta?cat=campings&slug=camping1` -> mock de impresion.
- `GET /api/route-pdf?cat=campings&slug=camping1` -> PDF simple.

## Ejemplos rapidos

```bash
curl http://localhost:8000/api/health
curl http://localhost:8000/api/categories
curl "http://localhost:8000/api/pois?cat=campings"
curl "http://localhost:8000/api/poi?cat=campings&slug=camping1"
curl "http://localhost:8000/api/print-ruta?cat=campings&slug=camping1"
curl -o ruta.pdf "http://localhost:8000/api/route-pdf?cat=campings&slug=camping1"
```

## Smoke test

Con el servidor corriendo en el puerto 8000:

```bash
python LocalBackend/smoke_test.py --base http://localhost:8000
```

El script valida:
- `health`
- listado de categorias y un POI real
- endpoints de impresion y PDF

## Parametros

- `--root`: ruta a la carpeta `www`
- `--port`: puerto (default 8000)
