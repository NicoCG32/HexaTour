# Compilar el firmware

[Guía de firmware](README.md) · [Índice técnico](../docs/README.md) · [Circuito y montaje](../docs/manual-proveedor.md)

## Base de reproducción

Esta base se establece el **2026-10-08**. Las versiones del entorno usado originalmente en el montaje no están disponibles; estos perfiles definen una base nueva de compilación. No se usó Arduino IDE ni se cargaron binarios en placas durante esta revisión.

| Componente | Versión o selección |
| --- | --- |
| Arduino CLI | 1.5.1 |
| UNO | Arduino AVR Boards 1.8.8, `arduino:avr:uno` |
| ESP32-S3 | Espressif Arduino ESP32 3.3.12, `esp32:esp32:esp32s3` |
| ArduinoJson local | 7.4.2 |
| LiquidCrystal_I2C local | 2.0.0 |
| Adafruit Thermal Printer Library local | 1.4.1 |

Los [perfiles del ESP32-S3](esp32/HexaTour/sketch.yaml) y [UNO](uno/ImpresoraUNO/sketch.yaml) fijan las versiones de los cores y usan las librerías incluidas en `firmware/librerias`. No descargan otra copia de esas librerías. La fuente de cada sketch queda en una carpeta con su mismo nombre, como requiere Arduino. Los includes convencionales permiten que Arduino descubra y compile también los archivos C++ de las librerías.

El perfil ESP32S3 Dev Module usa los valores predeterminados del core fijado: CPU 240 MHz, flash 4 MB, partición Default 4MB con SPIFFS, PSRAM deshabilitada y USB CDC On Boot deshabilitado. Son selecciones de compilación; antes de cargar, contrastarlas con la variante real de la placa, su memoria y conexión USB.

## Ejecutar

Instala [Arduino CLI 1.5.1 desde el release oficial](https://github.com/arduino/arduino-cli/releases/tag/v1.5.1), eligiendo el archivo de tu sistema y cotejando su SHA-256 con los checksums del release. Desde la raíz del repositorio, con `arduino-cli` disponible:

```bash
arduino-cli version
arduino-cli compile --profile uno --warnings all --output-dir build/firmware/uno firmware/uno/ImpresoraUNO
arduino-cli compile --profile esp32-s3 --warnings all --jobs 4 --output-dir build/firmware/esp32-s3 firmware/esp32/HexaTour
```

La primera ejecución necesita Internet para obtener los cores y herramientas fijados. Los perfiles de Arduino CLI usan su almacenamiento aislado de plataformas, conservando las versiones indicadas aunque existan otras instalaciones. Puedes indicar una configuración de CLI propia con `--config-file`; los perfiles no contienen rutas absolutas de este equipo. `build/` está ignorado por Git y no se usa para publicar la demo.

En Windows, usa rutas cortas para el almacenamiento de herramientas y la compilación. La revisión necesitó un alias temporal de unidad para resolver `bits/c++config.h` con la toolchain ESP32; el archivo estaba presente. Acortar las rutas resolvió esa etapa sin modificar cabeceras del compilador. Los perfiles fijan dependencias y ajustes de placa; no se promete identidad binaria entre sistemas operativos o rutas de construcción diferentes.

En Arduino IDE, abre [HexaTour.ino](esp32/HexaTour/HexaTour.ino) o [ImpresoraUNO.ino](uno/ImpresoraUNO/ImpresoraUNO.ino), instala las versiones de core indicadas y registra las librerías locales. La comprobación de esta entrega usa CLI: no se atribuye un resultado de compilación a una versión del IDE sin probarla.

## Resultado de compilación

Ambos perfiles compilaron y enlazaron correctamente el 2026-10-08 en Windows con Arduino CLI 1.5.1 y las versiones anteriores:

| Perfil | Programa usado / máximo | RAM estática usada / máximo |
| --- | --- | --- |
| uno | 9.298 / 32.256 bytes (28%) | 635 / 2.048 bytes (31%) |
| esp32-s3 | 1.041.773 / 1.310.720 bytes (79%) | 48.440 / 327.680 bytes (14%) |

La RAM indicada corresponde a variables globales; no mide el consumo dinámico máximo de impresión, PDF o cadenas. Los binarios se generan en `build/firmware`, fuera de Git.

Con `--warnings all` se conservaron advertencias: `DynamicJsonDocument` de ArduinoJson está obsoleto; LiquidCrystal_I2C usa macros binarias antiguas y declara `architectures=all`; Adafruit y el core AVR tienen variables/parámetros sin usar. No se modificaron las librerías para ocultar esas advertencias. El resultado acredita compilación y enlace, no funcionamiento del LCD, memoria bajo carga o hardware real.

## Prueba física pendiente

La compilación sólo comprueba construcción y enlace del programa. Para acreditar el montaje, registrar fecha, modelo/variante de cada placa, ajustes de memoria/USB, fuente y conexiones contrastadas con el circuito, versión/commit cargado y estos resultados:

| Prueba | Criterio | Resultado |
| --- | --- | --- |
| SD y LCD | `/www` completo, SD montada y estados visibles | Pendiente |
| Wi-Fi y portal cautivo | AP accesible y detección de portal en un dispositivo real | Pendiente |
| Catálogo | Categoría, ficha, imagen principal y ruta cargan desde SD | Pendiente |
| PDF ESP32 | Descarga abre correctamente y contiene texto/imagen esperados | Pendiente |
| UART ESP32–UNO | STATUS/PRINT/DONE observados con el mismo identificador de trabajo | Pendiente |
| Impresora | Ticket legible y confirmación DONE después de terminar | Pendiente |
| Espera y fallo | Equipo no disponible o sin respuesta muestra el estado real, sin afirmar impresión completada | Pendiente |

No activar SMS sin un destinatario acordado y configuración local válida. La demo de Pages tiene su propia copia forzada y no sustituye estas pruebas. Mantener los datos turísticos como ejemplos mientras no se verifiquen sus fuentes.

Referencias: [estructura de sketches](https://docs.arduino.cc/arduino-cli/sketch-specification) · [perfiles de compilación](https://docs.arduino.cc/arduino-cli/sketch-project-file) · [instalación del core ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html).
