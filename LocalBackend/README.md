# Local Backend (Mock)

Servidor local para probar el frontend sin ESP32. Sirve los archivos de `www` y expone:

- `GET /api/print-ruta` (mock)
- `GET /api/route-pdf` (PDF simple)

## Uso

```bash
python local_backend/server.py --root "Frontend (Interfaz)/www" --port 8000
```

Luego abre:
- Visitante: http://localhost:8000/visitor/
- Operador: http://localhost:8000/main/

## Parametros

- `--root`: ruta a la carpeta `www`
- `--port`: puerto (default 8000)
