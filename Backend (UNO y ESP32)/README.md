# Backend (UNO y ESP32) – Firmware y configuración

Este README documenta el firmware del backend y sus ajustes clave. Está enfocado en qué microcontrolador carga cada sketch, pines usados y parámetros configurables (credenciales, PDF, etc.).

## Qué se carga y dónde

- ESP32‑S3: [HexaTour (ESP32)/HexaTour.ino](Backend%20(UNO%20y%20ESP32)/HexaTour%20(ESP32)/HexaTour.ino)
- Arduino UNO: [Impresora (UNO)/ImpresoraUNO.ino](Backend%20(UNO%20y%20ESP32)/Impresora%20(UNO)/ImpresoraUNO.ino)

## Pines usados

### ESP32 (HexaTour.ino)
- SD (SPI):
  - SCK: GPIO 12
  - MISO: GPIO 13
  - MOSI: GPIO 11
  - CS: GPIO 10
- LCD I2C:
  - SDA: GPIO 8
  - SCL: GPIO 9
- UART con UNO (Serial2):
  - ESP32 RX2: GPIO 16 (desde UNO TX 11 con divisor)
  - ESP32 TX2: GPIO 17 (hacia UNO RX 10)

### Arduino UNO (ImpresoraUNO.ino)
- Enlace con ESP32 (SoftwareSerial):
  - UNO RX: 10 (desde ESP32 TX2)
  - UNO TX: 11 (hacia ESP32 RX2)
- Impresora térmica (SoftwareSerial):
  - UNO RX: 2 (desde TX impresora)
  - UNO TX: 3 (hacia RX impresora)

## Ajustes clave en el ESP32

### Wi‑Fi AP
En [Backend (UNO y ESP32)/HexaTour (ESP32)/HexaTour.ino](Backend%20(UNO%20y%20ESP32)/HexaTour%20(ESP32)/HexaTour.ino):

- SSID: `AP_SSID`
- Password: `AP_PASS`

### Credenciales del panel operador
En el mismo archivo:

- Usuario: `MAIN_USER`
- Contraseña: `MAIN_PASS`

### Página inicial del portal
- Variable `START_FILE` (por defecto /www/visitor/index.html).

### Logo en PDF de ruta
El PDF intenta incluir un logo si existe:

- Ruta esperada (JPEG): /www/img/map/logo.jpg
- Función: `findLogoJpeg()`

El archivo `logo.jpg` se usa exclusivamente en el PDF de ruta generado por el ESP32.

El archivo `logoHexaTour.png` se usa en el frontend como logo principal del portal.

### Endpoints relevantes
- `/api/print-ruta?cat=<categoria>&slug=<slug>&name=<nombre>` imprime rutas desde /www/db.
- `/api/route-pdf?cat=<categoria>&slug=<slug>&name=<nombre>&dl=1` genera PDF con texto e imagen desde /www/db.

### Dependencias

- ArduinoJson (para leer /www/db/poi/<categoria>/<slug>.json).

## Ajustes clave en el UNO

- Puerto de la impresora térmica y velocidad:
  - `SoftwareSerial mySerial(PRINTER_RX, PRINTER_TX)`
  - `mySerial.begin(9600)`

- Mensaje final del ticket:
  - `GRACIAS POR USAR HEXATOUR`

## Contenidos en SD

La SD debe contener la carpeta www del frontend, incluyendo /www/db y /www/img. Ver guía de contenidos en [Frontend (Interfaz)/README.md](../Frontend%20(Interfaz)/README.md).

## Notas de compatibilidad

- Si cambias pines en el hardware, actualiza los `#define` correspondientes.
- Si cambias el logo del PDF, reemplaza el archivo en /www/img/map/logo.jpg (JPEG).
