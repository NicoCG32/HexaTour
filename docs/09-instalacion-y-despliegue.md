# 09 · Puesta en marcha y comprobaciones

El repositorio permite probar el portal en un PC, generar una demo estática o preparar el montaje físico.

## A. Explorar y probar el portal desde un PC

Se necesita Python 3.10+:

```bash
python tools/backend-local/server.py --root web/www --port 8000
```

Abrir `http://localhost:8000/visitor/` o `http://localhost:8000/main/`. El backend simula los endpoints de impresión y PDF, sin autenticación del operador, impresora física ni DNS cautivo.

## B. Validar datos y preparar la demo

Desde la raíz:

```bash
python -m unittest discover -s test -p 'test_*.py'
python tools/build_demo.py --output dist/demo
```

El empaquetador valida el catálogo y genera una copia con modo demo forzado en todas sus entradas. La salida debe ser una carpeta nueva; si `dist/demo` ya existe, elige otra con `--output`. La [guía de publicación](Despliegue.md) explica el proceso local y el workflow de GitHub Pages.

Puedes abrir la demo pública desde el [README](../README.md).

## C. Reproducir el montaje físico

1. Revisar [componentes, pines y alimentación](../firmware/README.md) y el [circuito editable](diagramas/HexaTourCircuito.drawio). No alimentar la ticketera desde la placa: la guía indica fuente separada.
2. Preparar la tarjeta SD con la carpeta `www` del repositorio en `/www` y comprobar las rutas del catálogo.
3. Compilar y cargar el sketch del [ESP32-S3](../firmware/esp32/HexaTour/HexaTour.ino) y del [UNO](../firmware/uno/ImpresoraUNO/ImpresoraUNO.ino) siguiendo las [versiones y comandos documentados](../firmware/Compilacion.md).
4. **Cambiar las credenciales de ejemplo del Wi-Fi y el operador** antes de cualquier instalación fuera de un banco de pruebas. El portal usa HTTP y no constituye una interfaz administrativa segura en una red compartida.
5. Comprobar alimentación, SD, conexión local, navegación, LCD, respuesta `STATUS` y una impresión real hasta `DONE`.
6. Revisar con responsables locales todas las indicaciones, horarios y alertas antes de ofrecer el contenido al público.

La [guía de compilación](../firmware/Compilacion.md#montaje-original-y-revalidación) registra la base de octubre de 2026 y las pruebas físicas pendientes con esos binarios.

## Recuperación y versiones

Conservar copia verificada de la SD, sketches, configuración usada y artefactos de prueba. Una actualización de GitHub Pages **no actualiza** la tarjeta del montaje. Si una versión falla, volver a una combinación previamente probada de firmware y contenido; no mezclar sketches/catálogo sin repetir la validación.

[Manual del proveedor](manual-proveedor.md) · [despliegue de demo](Despliegue.md) · [simulador](../tools/backend-local/README.md)
