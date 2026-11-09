# 06 · Integraciones del sistema

El portal utiliza contenido preparado manualmente y comunicación local entre sus componentes.

## Componentes e interfaces

| Integración | Uso | Dependencia |
| --- | --- | --- |
| Wi-Fi AP, DNS y HTTP del ESP32-S3 | Conectar y servir el portal local | Firmware, energía y hardware ESP32 |
| SD por SPI | Leer páginas, JSON, imágenes y recursos de PDF | Tarjeta y módulo SD |
| UART ESP32 ↔ UNO | Consultar estado y solicitar impresión | Cableado, niveles eléctricos y dos firmwares |
| Serial TTL UNO ↔ ticketera | Imprimir el texto del trabajo | Fuente de la impresora, papel, enlace serial |
| LCD I²C | Informar estados locales | Pantalla y cableado |
| Aplicación SMS del visitante | Abrir un mensaje preparado sólo con configuración válida | Dispositivo con capacidad de SMS y acción del usuario |
| Python `http.server` extendido | Simular endpoints sin hardware | PC de desarrollo, no forma parte del firmware |
| GitHub Pages | Servir una demo estática | Acceso a Internet para abrir el sitio público; no controla hardware |

[Arquitectura](01-arquitectura-general.md) · [Compilación y pines](../firmware/README.md)
