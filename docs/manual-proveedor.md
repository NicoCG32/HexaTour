# Manual del proveedor - HexaTour

Este manual esta orientado al equipo tecnico que provee y mantiene el servicio HexaTour. Cubre puesta en marcha, validaciones operativas, actualizaciones de contenido y diagnostico basico.

## Tabla de contenidos

- [Guia rapida de proveedor](#guia-rapida-de-proveedor)
- [Componentes y conexionado](#componentes-y-conexionado)
- [Checklist de puesta en marcha](#checklist-de-puesta-en-marcha)
- [Operacion diaria](#operacion-diaria)
- [Actualizacion de contenidos](#actualizacion-de-contenidos)
- [Actualizacion de firmware](#actualizacion-de-firmware)
- [Mantenimiento preventivo](#mantenimiento-preventivo)
- [Diagnostico rapido](#diagnostico-rapido)
- [FAQ tecnico](#faq-tecnico)
- [Alcance](#alcance)

## Guia rapida de proveedor

- Verifica que el firmware este cargado segun [firmware/README.md](../firmware/README.md).
- Prepara la SD con [web/www](../web/www).
- Enciende el equipo y confirma la red Wi-Fi HexaTour.
- Valida el portal:
   - Visitante: http://192.168.4.1/visitor/
   - Operador: http://192.168.4.1/main/
- Ejecuta una impresion de prueba desde la vista de operador.

## Componentes y conexionado

- Tableta (monitor tactil principal)
- ESP32-S3
- Arduino UNO
- Impresora termica con TTL
- Pantalla LCD 2x16 (I2C)
- Modulo SD y tarjeta SD

Notas criticas:
- La impresora termica debe usar fuente propia (9V en este prototipo).
- No alimentar la impresora desde el ESP32 ni desde el UNO.
- Unificar tierra (GND) entre todos los modulos.
- Usar divisores de voltaje en lineas de comunicacion hacia el ESP32-S3.

Detalle de pines y cableado en [firmware/README.md](../firmware/README.md).

## Checklist de puesta en marcha

- SD insertada con [web/www](../web/www).
- Impresora con papel y fuente independiente.
- Red Wi-Fi HexaTour visible.
- Portal operativo en modo visitante y operador.
- Impresion de ticket OK.

## Operacion diaria

- Operador inicia sesion en http://192.168.4.1/main/.
- Usuario navega en http://192.168.4.1/visitor/.
- El sistema imprime rutas y genera PDF cuando se solicita.

Credenciales por defecto:
- Usuario: operator
- Contrasena: HexaTour2025!

## Actualizacion de contenidos

La base de datos y assets se gestionan en [web/README.md](../web/README.md). Mantener consistencia de slugs, imagenes y archivos JSON.

## Actualizacion de firmware

Para cambios de configuracion, pines o credenciales, seguir [firmware/README.md](../firmware/README.md). Documentar toda actualizacion con fecha y motivo.

## Mantenimiento preventivo

- Revisar cableado y conectores cada ciclo de mantenimiento.
- Limpiar cache del navegador en pruebas de contenido.
- Verificar existencia de .gz cuando se despliega contenido a SD.
- Hacer respaldo periodico de [web/www](../web/www).

## Diagnostico rapido

- Portal no abre: confirmar conexion a la red HexaTour y abrir URLs de visitante u operador.
- Error SD: revisar formato FAT32 y contenido en [web/www](../web/www).
- Datos no cargan: validar indice en [web/www/db/index.json](../web/www/db/index.json).
- No imprime: revisar fuente independiente, papel y enlace serial UNO-ESP32.
- PDF sin logo: verificar [web/www/img/map/logo.jpg](../web/www/img/map/logo.jpg).

## FAQ tecnico

**No puedo iniciar sesion en operador**
- Confirmar usuario y contrasena, y URL de operador.

**No se ve la lista de lugares**
- Verificar indice en [web/www/db/index.json](../web/www/db/index.json) y limpiar cache.

**Imprimir se queda en espera**
- Confirmar que la impresora esta encendida y que el UNO reciba datos.

## Alcance

Este manual cubre la operacion y mantenimiento del prototipo con ESP32-S3 y Arduino UNO. Funcionalidades proyectadas (NFC, voz, multilenguaje) pueden no estar disponibles en esta version.
