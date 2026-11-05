# 08 · Salidas y entregables

Las salidas disponibles dependen de la modalidad de ejecución:

| Salida | Dónde existe | Interpretación correcta |
| --- | --- | --- |
| Ficha e imagen de ruta en pantalla | Montaje, simulador y demo | Información predefinida del catálogo. |
| Ticket impreso | Firmware ESP32 + UNO + ticketera | El `200` HTTP indica aceptación y `DONE` el fin de la rutina del UNO; comprueba el ticket en el montaje. |
| PDF de ruta | Endpoint ESP32 | Documento generado con texto e imágenes disponibles en SD. |
| PDF de prueba | Backend Python | Simplificado; no valida la composición visual del firmware. |
| Descarga PDF en demo estática | No disponible | Se comunica como función deshabilitada. |
| Archivos de la demo | Empaquetador Python y workflow de Pages | Portal estático y manifiesto para publicación; no firmware ni servidor Python. |
| Informes del curso | `docs/informes/` | Evidencia académica histórica, no informes generados por la aplicación. |

Los datos actuales del catálogo son de ejemplo.

[Manual de demo](Demo.md) · [despliegue](Despliegue.md) · [antecedentes académicos](academica/README.md)
