# 05 · Reglas del sistema y decisiones de diseño

El núcleo operativo resuelve contenido local, presenta indicaciones y coordina las solicitudes de impresión y PDF.

## Reglas comprobables

| Regla | Dónde se aplica | Razón |
| --- | --- | --- |
| Resolver `category` y `slug` hacia archivos del catálogo | JavaScript y firmware ESP32 | Evita depender de una API remota. |
| Rechazar o informar fichas/rutas inexistentes | Cliente, firmware y validador Python | No imprimir indicaciones sin contenido. |
| Mantener coherentes índice, listas, fichas e imágenes | `test/validate_data.py` | Evitar enlaces rotos y datos incompletos. |
| No aceptar otro ticket mientras el ESP32 está ocupado | `HexaTour.ino` | Evitar superposición de trabajos. |
| Consultar disponibilidad del UNO antes de mandar el texto | Protocolo `STATUS?` | Distinguir aceptación web de posibilidad de imprimir. |
| Ignorar un trabajo si su id coincide con el último atendido | Firmware UNO | Prevenir algunos duplicados simples; no es garantía de entrega exactamente una vez. |
| Desactivar acciones físicas en demo | JavaScript y empaquetador | Evitar que el usuario confunda un mensaje con una impresión o un aviso real. |

## Limitaciones relevantes

La ruta es **texto e imagen previamente preparados**. Los tiempos a pie o en vehículo son campos informativos, no cálculos producidos por un servicio de mapas. Tampoco se mide el estado del papel, la calidad final del ticket ni la recepción de un SMS. El servidor de prueba puede aceptar un trabajo ficticio, mientras que el hardware tiene tiempos de respuesta y errores propios.

Para entender el orden preciso de decisiones, ver los [estados y secuencia de impresión](03-flujo-de-usuario.md) y la [arquitectura técnica ampliada](Arquitectura.md).
