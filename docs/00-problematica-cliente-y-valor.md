# 00 · Problema, público y propuesta

## El problema que investigamos

Durante el curso estudiamos dificultades para orientarse en sectores de turismo rural de la Región de Coquimbo. Cuando la cobertura móvil falla o faltan señales claras, una ficha, un horario o unas indicaciones que dependen de Internet pueden dejar de servir justo cuando se necesitan. Los [informes originales](academica/README.md) reúnen las entrevistas y el análisis de esa etapa.

## La propuesta

HexaTour busca ofrecer un **punto de información local** al que el visitante se conecte mediante Wi-Fi y acceda con su navegador. La información reside en una SD conectada a un ESP32-S3. En el montaje, una impresora térmica controlada por un Arduino UNO permite entregar indicaciones impresas. El ESP32 también dispone de un endpoint para generar PDF.

Las indicaciones se preparan previamente y requieren actualización y validación por el responsable del lugar. El catálogo actual contiene ejemplos; los [límites de uso](02-funcionalidades.md#límites-de-uso) explican su alcance.

## Personas involucradas en la experiencia

| Perfil | Qué necesita |
| --- | --- |
| **Visitante** | Encontrar un lugar, leer indicaciones y conservarlas cuando sea posible. |
| **Operador de un punto** | Consultar contenido y, con la impresora disponible, solicitar un ticket. |
| **Responsable del montaje** | Mantener la SD, alimentar placas y consumibles, revisar errores y actualizar fichas. |
| **Organización que quisiera instalarlo** | Comprobar utilidad, costos y condiciones reales antes de adoptar el prototipo. |

## Conveniencia: comparación antes que promesa

El primer valor que queremos evaluar es si **una consulta local funciona donde una página remota no está disponible** y si las instrucciones impresas ayudan a seguir un recorrido previamente validado. Eso no implica que un tótem sea siempre mejor que señalética o folletos. Para algunos recintos una solución física sin electrónica puede ser más barata y robusta.

Las brechas de infraestructura en turismo rural están documentadas por la [Subsecretaría de Turismo](https://www.subturismo.gob.cl/wp-content/uploads/2025/07/plan-turismo-y-desarrollo-rural.pdf), pero **no existe demanda pagadora demostrada de HexaTour**. El [estudio de mercado](19-mercado-y-validacion-comercial.md) identifica segmentos y sustitutos, y el [análisis de costos](18-analisis-economico-clp-usd.md) separa el beneficio al visitante del margen del proveedor.

## Criterio de utilidad

El objetivo es que una persona encuentre indicaciones comprensibles sin depender de sus datos móviles. Para evaluarlo, se necesita observar consultas en condiciones reales, revisar el contenido con responsables locales y medir la disponibilidad de la impresora y el esfuerzo de mantenimiento.

[Estado de las funcionalidades](02-funcionalidades.md) · [Contexto formativo](academica/README.md)
