# Fuentes de diagramas · HexaTour

Cada `.mmd` contiene el código Mermaid de un diagrama de arquitectura, flujo o dominio. Para modificarlos, actualiza la fuente y el bloque correspondiente en la página Markdown.

| Fuente | Diagrama | Documento que lo contextualiza |
| --- | --- | --- |
| `01-contexto.mmd` | Contexto de usuario y punto | [Arquitectura](../../01-arquitectura-general.md) |
| `02-contenedores.mmd` | Componentes físicos | [Arquitectura](../../01-arquitectura-general.md) |
| `03-componentes.mmd` | Componentes de software | [Arquitectura](../../01-arquitectura-general.md) |
| `04-despliegues.mmd` | Montaje, simulador y demo | [Arquitectura](../../01-arquitectura-general.md) |
| `05-flujo-visitante.mmd` | Navegación y decisiones | [Flujos](../../03-flujo-de-usuario.md) |
| `06-secuencia-impresion.mmd` | Secuencia HTTP/serial | [Flujos](../../03-flujo-de-usuario.md) |
| `07-estados-esp32.mmd` | Estado de impresión ESP32 | [Flujos](../../03-flujo-de-usuario.md) |
| `08-estados-uno.mmd` | Estado operativo UNO | [Flujos](../../03-flujo-de-usuario.md) |
| `09-dominio-json.mmd` | Entidades lógicas del catálogo | [Datos](../../04-base-de-datos.md) |
| `10-flujo-datos.mmd` | Lectura de fichas e imágenes | [Datos](../../04-base-de-datos.md) |
| `11-interconexiones-hardware.dot` | Fuente Graphviz para mapa de conexiones | [SVG](../HexaTourConexionesRevisadas.svg) · [PNG](../HexaTourConexionesRevisadas.png) |

El circuito del montaje está en [`HexaTourCircuito.drawio`](../HexaTourCircuito.drawio). El mapa de conexiones resume sus pines; verifica alimentación y niveles eléctricos con la [guía de firmware](../../../firmware/README.md).
