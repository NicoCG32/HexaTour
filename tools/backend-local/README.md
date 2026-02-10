# Backend Local (Mock)

Servidor local para probar la web sin ESP32. Sirve los archivos de [web/www](web/www) y expone endpoints mock basados en los JSON de la SD.

## Tabla de contenidos

- [Guia rapida](#guia-rapida)
- [Endpoints mock](#endpoints-mock)
- [Smoke test](#smoke-test)
- [Parametros](#parametros)
- [FAQ](#faq)

## Guia rapida

1. Inicia el servidor:

```bash
python "tools/backend-local/server.py" --root "web/www" --port 8000
```

2. Abre en el navegador:
   - Visitante: http://localhost:8000/visitor/
   - Operador: http://localhost:8000/main/

Codigo fuente:
- [tools/backend-local/server.py](tools/backend-local/server.py)

## Endpoints mock

- `GET /api/health` -> estado basico del servidor.
- `GET /api/categories` -> lista de categorias disponibles (nombres de archivos en [web/www/db/categories](web/www/db/categories)).
- `GET /api/category-items?cat=campings` -> items de una categoria.
- `GET /api/pois?cat=campings` -> lista de POIs con slug y name.
- `GET /api/poi?cat=campings&slug=camping1` -> POI completo.
- `GET /api/poi/campings/camping1` -> mismo que arriba, via path.
- `GET /api/print-ruta?cat=campings&slug=camping1` -> mock de impresion.
- `GET /api/route-pdf?cat=campings&slug=camping1` -> PDF simple.

## Smoke test

Con el servidor corriendo en el puerto 8000:

```bash
python "tools/backend-local/smoke_test.py" --base http://localhost:8000
```

El script valida health, listado de categorias, un POI real y endpoints de impresion/PDF.

Codigo fuente:
- [tools/backend-local/smoke_test.py](tools/backend-local/smoke_test.py)

## Parametros

- `--root`: ruta a la carpeta [web/www](web/www).
- `--port`: puerto (default 8000).

## FAQ

**No carga la web**
- Revisa que el root apunte a la carpeta correcta y que el puerto no este ocupado.

**Quiero usar otro puerto**
- Cambia el valor de `--port` al iniciar el servidor.
