# HexaTour

Video promocional: https://www.youtube.com/shorts/Zw-bziu8veU

HexaTour es un prototipo de orientacion turistica rural que funciona sin Internet. Ofrece un portal cautivo con informacion de puntos de interes y permite imprimir indicaciones mediante una impresora termica. El sistema se basa en ESP32-S3 (portal, SD, PDF) y Arduino UNO (control de impresora).

## Como se llevo a cabo el prototipo

- Se definio una base de datos JSON en /www/db y una estructura de imagenes en /www/img para cargar informacion desde la SD.
- Se implemento el portal cautivo en el ESP32-S3 con endpoints para imprimir rutas y generar PDF.
- Se separo el control de la impresora en un Arduino UNO, comunicandose por serial con el ESP32.
- Se documentaron pines y conexiones para permitir replicar el armado.

## Contenidos principales

- Manual de usuario: [Manual de Usuario.md](Manual%20de%20Usuario.md)
- Firmware y pines: [Backend (UNO y ESP32)/README.md](Backend%20(UNO%20y%20ESP32)/README.md)
- Contenidos y portal cautivo: [Frontend (Interfaz)/README.md](Frontend%20(Interfaz)/README.md)
- Informes: carpeta Informes (los extract no se versionan)

## Estructura del repo

- Backend (UNO y ESP32)/
- Frontend (Interfaz)/
- Informes/
- Manual de Usuario.md

## Puesta en marcha rapida

1. Carga los sketches:
   - ESP32: [Backend (UNO y ESP32)/HexaTour (ESP32)/HexaTour.ino](Backend%20(UNO%20y%20ESP32)/HexaTour%20(ESP32)/HexaTour.ino)
   - UNO: [Backend (UNO y ESP32)/Impresora (UNO)/ImpresoraUNO.ino](Backend%20(UNO%20y%20ESP32)/Impresora%20(UNO)/ImpresoraUNO.ino)
2. Copia la carpeta www del frontend a la tarjeta SD.
3. Enciende el equipo y conecta al Wi-Fi HexaTour.
4. Abre el portal:
   - Visitante: http://192.168.4.1/visitor/
   - Operador: http://192.168.4.1/main/

## Backend local (pruebas en PC)

Para probar el frontend sin ESP32, usa el backend mock en [LocalBackend/README.md](LocalBackend/README.md).

## Rendimiento

Si el portal se siente lento, verifica que los .gz esten generados para `www/db` y `www/img`, y limpia cache del navegador.

## Errores comunes

- Portal no abre: conecta al Wi-Fi HexaTour y visita http://192.168.4.1/visitor/.
- Error SD: revisa FAT32 y que exista la carpeta /www en la tarjeta.
- Datos no cargan: confirma que /www/db/index.json exista y limpia cache.
- No imprime: revisa papel, encendido de impresora y enlace serial con el UNO.

## Actualizar datos y testear

Para editar la base JSON, rutas e imagenes, y probar localmente antes de copiar a la SD, sigue la guia en [Frontend (Interfaz)/README.md](Frontend%20(Interfaz)/README.md).

## Alcances futuros

- Optimizar indices y cacheo de la base JSON en el ESP32-S3 para acelerar busquedas.
- Panel de administracion para cargar contenidos sin editar archivos manualmente.
- Integracion con nuevos modulos (NFC, voz, multilenguaje) segun la evolucion del prototipo.

## Notas

- Este repositorio incluye documentos y codigo; los archivos generados o temporales quedan fuera via .gitignore.
- Si cambias hardware o pines, actualiza los defines en el firmware y la documentacion.
