# HexaTour

Prototipo de orientacion turistica rural que funciona sin Internet. Ofrece un portal cautivo con informacion de puntos de interes y permite imprimir indicaciones mediante una impresora termica. El sistema se basa en ESP32-S3 (portal, SD, PDF) y Arduino UNO (control de impresora).

Video promocional: https://www.youtube.com/shorts/Zw-bziu8veU

## Tabla de contenidos

- [Vision general](#vision-general)
- [Guia rapida](#guia-rapida)
- [Documentacion clave](#documentacion-clave)
- [Mapa del repo](#mapa-del-repo)
- [Pruebas locales](#pruebas-locales)
- [FAQ](#faq)
- [Creditos y terceros](#creditos-y-terceros)

## Vision general

- Portal cautivo con UI de visitante y operador.
- Base de datos JSON y assets en la SD.
- Impresion de rutas via impresora termica.

## Guia rapida

1. Carga los sketches:
   - ESP32: [firmware/esp32/HexaTour.ino](firmware/esp32/HexaTour.ino)
   - UNO: [firmware/uno/ImpresoraUNO.ino](firmware/uno/ImpresoraUNO.ino)
2. Copia la carpeta www a la SD desde [web/www](web/www).
3. Enciende el equipo y conecta al Wi-Fi HexaTour.
4. Abre el portal:
   - Visitante: http://192.168.4.1/visitor/
   - Operador: http://192.168.4.1/main/

![Diagrama de conexion de HexaTour](docs/diagramas/HexaTourCircuito.jpg)

## Documentacion clave

- Manual del proveedor: [docs/manual-proveedor.md](docs/manual-proveedor.md)
- Firmware y pines: [firmware/README.md](firmware/README.md)
- Contenidos y portal cautivo: [web/README.md](web/README.md)
- Backend local (mock): [tools/backend-local/README.md](tools/backend-local/README.md)

## Mapa del repo

- [docs](docs): documentacion tecnica y entregables.
- [docs/diagramas](docs/diagramas): diagramas del sistema y conexionado.
- [docs/informes](docs/informes): informes y anexos del proyecto.
- [docs/manual-proveedor.md](docs/manual-proveedor.md): guia operativa para equipo tecnico.
- [firmware](firmware): sketches, pines y librerias locales para ESP32 y UNO.
- [web](web): portal cautivo, base JSON y assets para la SD.
- [tools/backend-local](tools/backend-local): servidor mock para pruebas locales.

## Pruebas locales

Para probar la UI sin ESP32, usa el backend mock y sigue la guia en [tools/backend-local/README.md](tools/backend-local/README.md).

## FAQ

**El portal se ve lento**
- Verifica que los .gz existan en [web/www/db](web/www/db) y [web/www/img](web/www/img), y limpia cache del navegador.

**No aparecen datos**
- Confirma que exista [web/www/db/index.json](web/www/db/index.json) y limpia cache.

**No imprime**
- Revisa papel, alimentacion de la impresora y enlace serial con el UNO.

## Creditos y terceros

El proyecto incluye componentes de terceros. Se mantienen sus licencias en las carpetas correspondientes.

- Librerias y cores: ver detalle en [firmware/README.md](firmware/README.md).
- Arduino core para AVR (UNO): SoftwareSerial, Wire, SPI, SD y otros headers provienen del core oficial de Arduino.
- Arduino core para ESP32 (ESP32-S3): WiFi, WebServer, DNSServer, SPI, SD, Wire y otros headers provienen del core oficial de Espressif.
