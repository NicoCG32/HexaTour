# 02 · Funcionalidades por modalidad

El portal puede ejecutarse en el montaje, en un simulador local o como demo estática.

| Capacidad | Montaje ESP32 + UNO (en código) | Simulador Python | Demo estática |
| --- | --- | --- | --- |
| Portal de visitante y operador | Sí, archivos desde SD | Sí, servidos desde PC | Sí |
| Categorías, fichas e imágenes | Sí | Sí | Sí, datos de ejemplo |
| Imagen y texto de indicaciones | Sí, si existe contenido | Sí | Sí |
| Impresión térmica | Solicitud a UNO con protocolo y estados | Aceptación simulada | Mensaje de simulación; no envía API |
| PDF de ruta | Endpoint del ESP32 | PDF de prueba simplificado | Deshabilitado |
| Wi-Fi local y DNS cautivo | Implementados en ESP32 | No | No |
| LCD de estado | Implementado en ESP32 | No | No |
| Restricción de acceso a `/main/` | HTTP Basic en firmware | No | No |
| Urgencia en visitante | Puede preparar SMS desde el dispositivo si fue configurado | Depende de la interfaz del cliente; no envía SMS | Sólo demostración local |
| Urgencia en operador | Aviso local, sin llamada ni envío | Aviso local | Aviso local |

## Límites de uso

- Los tiempos, horarios, alertas e imágenes del catálogo son **datos de ejemplo**, no información corroborada en terreno.
- El portal **no usa geolocalización en vivo ni un motor de cálculo de rutas**.
- Un `200 print job accepted` significa que el ESP32 aceptó la solicitud; **no demuestra que la impresora haya terminado**.
- La acción de urgencia **no constituye un servicio de emergencias**. Abrir una app de SMS no significa que el mensaje se haya enviado o recibido.
- Los binarios de la base de compilación actual requieren una [prueba física integrada](../firmware/Compilacion.md#montaje-original-y-revalidación).

## Aspiraciones de los informes

Funciones como multilenguaje, audioguía/NFC u otras expansiones estudiadas en el curso se consideran **propuestas históricas o posibilidades futuras**, no capacidades del portal actual.

[Flujos y estados](03-flujo-de-usuario.md) · [Demo](Demo.md) · [Compilación](../firmware/Compilacion.md)
