# Documentación de HexaTour

<!-- DOCUMENTACION:indice-niveles-2026-10-29:BEGIN -->

## Documentación por cuatro niveles — 2026-10-29

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

| Nivel                      | Pregunta principal                                                    | Lectura                                                  |
| -------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------- |
| 1. General                 | Qué problema, para quién, qué solución y por qué lo eligió el creador | 00, 02, 03 y 16                                          |
| 2. Técnica                 | Cómo funciona, entidades, persistencia y ejecución                    | 01, 04, 05, 06, 07, 08 y 09                              |
| 3. Desarrollo del proyecto | Cómo se llegó, por qué corresponde y qué cuesta continuar             | 17, 15 y 18                                              |
| 4. Académica/formativa     | Qué se entregó en un curso y a qué etapa pertenece                    | [Documentación académica/formativa](academica/README.md) |

### Rutas por lector

- **Dirección/cliente/responsable:** 00 → 16 → 01 → 15 → 18.
- **Desarrollo/técnica:** 01 → 04 → 05 → 06 → 09; complementar con las guías especializadas conservadas.
- **Producto/operaciones:** 00 → 02 → 03 → 07 → 08 → 17.
- **Académica/formativa:** contexto de 16 y catálogo del nivel 4 cuando corresponda; contrastar luego con la arquitectura vigente.

| Capítulo | Documento                                                                          | Nivel                   |
| -------- | ---------------------------------------------------------------------------------- | ----------------------- |
| 00       | [Problemática, cliente y solución](00-problematica-cliente-y-valor.md)             | general                 |
| 01       | [Arquitectura por niveles](01-arquitectura-general.md)                             | técnica                 |
| 02       | [Catálogo funcional](02-funcionalidades.md)                                        | general / técnica       |
| 03       | [Recorrido y estados](03-flujo-de-usuario.md)                                      | general / técnica       |
| 04       | [Dominio, entidades y persistencia](04-base-de-datos.md)                           | técnica                 |
| 05       | [Reglas y núcleo](05-motor-o-nucleo-de-negocio.md)                                 | técnica                 |
| 06       | [Integraciones y asistencia](06-capa-de-ia-o-analisis.md)                          | técnica                 |
| 07       | [Diseño y accesibilidad](07-diseno-e-identidad.md)                                 | técnica / producto      |
| 08       | [Salidas y entregables](08-exportacion-e-informes.md)                              | técnica                 |
| 09       | [Puesta en marcha y distribución](09-instalacion-y-despliegue.md)                  | técnica                 |
| 15       | [Justificación, proyección y escalabilidad](15-escalabilidad-y-nuevos-mercados.md) | desarrollo del proyecto |
| 16       | [Motivación personal y contexto](16-motivacion-y-contexto.md)                      | general                 |
| 17       | [Etapas y metodología](17-desarrollo-y-metodologia.md)                             | desarrollo del proyecto |
| 18       | [Escenarios económicos CLP / USD](18-analisis-economico-clp-usd.md)                | desarrollo del proyecto |

Los nuevos capítulos complementan las fuentes especializadas existentes; no reemplazan contratos detallados por resúmenes. Los originales académicos se conservan intactos. La documentación del desarrollo describe etapas/metodología del producto y no contiene instrucciones o conversaciones internas.
<!-- DOCUMENTACION:indice-niveles-2026-10-29:END -->

HexaTour es un prototipo académico de orientación turística rural con portal local, contenido en tarjeta SD, generación de PDF e impresión térmica. Esta documentación describe la implementación disponible y distingue la prueba con mock del montaje físico.

## Por dónde empezar

| Necesidad                                                 | Documento                                                                                                                                                                                                                   |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ejecutar la web sin hardware o preparar el montaje        | [README del proyecto](../README.md#guia-rapida)                                                                                                                                                                             |
| Entender componentes, acciones y límites                  | [Arquitectura](Arquitectura.md)                                                                                                                                                                                             |
| Distinguir montaje físico, mock y demo disponible         | [Contexto](Arquitectura.md#contexto-y-modos-de-ejecución) · [Flujo de impresión](Arquitectura.md#flujo-de-datos-y-aceptación-de-impresión) · [Distribución pública](Arquitectura.md#demo-disponible-y-distribución-pública) |
| Editar categorías, fichas e imágenes de forma coherente   | [Formato de datos](Formato-de-datos.md)                                                                                                                                                                                     |
| Validar catálogo y recursos sin servidor                  | [Validación local y regresiones](Formato-de-datos.md#validación-local)                                                                                                                                                      |
| Actualizar contenido y probar el portal                   | [Guía web](../web/README.md)                                                                                                                                                                                                |
| Pines, configuración y protocolo ESP32–UNO                | [Guía de firmware](../firmware/README.md)                                                                                                                                                                                   |
| Compilar con versiones fijas y registrar la prueba física | [Compilación del firmware](../firmware/Compilacion.md)                                                                                                                                                                      |
| Servidor de prueba, API mock y smoke                      | [Backend local](../tools/backend-local/README.md)                                                                                                                                                                           |
| Explorar en modo demo sin API ni hardware                 | [Demo: activación y recorrido](Demo.md)                                                                                                                                                                                     |
| Preparar la copia pública y desplegarla en Pages          | [Distribución y despliegue](Despliegue.md)                                                                                                                                                                                  |
| Conocer procedencia y alcance de los ejemplos mostrados   | [Contenido de la demo](Contenido-demo.md)                                                                                                                                                                                   |
| Puesta en marcha y mantenimiento del equipo               | [Manual del proveedor](manual-proveedor.md)                                                                                                                                                                                 |

Ambos firmwares tienen una [base de compilación comprobada con versiones fijas](../firmware/Compilacion.md). El montaje original funcionaba según declaración del responsable; la [revalidación con la base nueva](../firmware/Compilacion.md#montaje-original-y-revalidación) no se ha realizado. Los datos turísticos son ejemplos sin verificación de vigencia; la procedencia gráfica declarada y las condiciones de presentación están en [Contenido de la demo](Contenido-demo.md). La [demo pública](https://nicocg32.github.io/HexaTour/) fue comprobada por HTTPS el 2026-10-07; [versión publicada y recuperación](Despliegue.md#estado).

## Circuito y fuentes editables

El cableado del montaje se conserva en [HexaTourCircuito.drawio](diagramas/HexaTourCircuito.drawio). Sus vistas exportadas son [SVG](diagramas/HexaTourCircuito.svg), [PNG](diagramas/HexaTourCircuito.png) y [JPG](diagramas/HexaTourCircuito.jpg). Antes de intervenir en hardware, contrastar el circuito con los [pines de los sketches](../firmware/README.md#pines-usados) y con el montaje disponible.

## Antecedentes académicos

Estos informes y anexos registran el desarrollo del curso. Las instrucciones de ejecución y los contratos técnicos vigentes están en las guías anteriores; los antecedentes pueden describir fases o funcionalidades proyectadas.

| Documento                               | Archivos                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Informe 1: problemática turística rural | [PDF](informes/Informe%20N%C2%B01.%20Limitaciones%20de%20orientaci%C3%B3n%20en%20la%20experiencia%20tur%C3%ADstica%20rural%20en%20la%20Regi%C3%B3n%20de%20Coquimbo.pdf) · [Word](informes/Informe%20N%C2%B01.%20Limitaciones%20de%20orientaci%C3%B3n%20en%20la%20experiencia%20tur%C3%ADstica%20rural%20en%20la%20Regi%C3%B3n%20de%20Coquimbo.docx) |
| Informe 2: Hexatour, la solución        | [PDF](informes/Informe%20N%C2%B02.%20Hexatour,%20la%20soluci%C3%B3n.pdf) · [Word](informes/Informe%20N%C2%B02.%20Hexatour,%20la%20soluci%C3%B3n.docx)                                                                                                                                                                                               |
| Planificación y Carta Gantt             | [PDF](informes/Anexo.%20Planificaci%C3%B3n%20y%20Carta%20Gantt.pdf)                                                                                                                                                                                                                                                                                 |
| Matriz de Priorización                  | [PDF](informes/Anexo.%20Matriz%20de%20Priorizaci%C3%B3n.pdf)                                                                                                                                                                                                                                                                                        |
| Mapa de Empatía                         | [PDF](informes/Anexo.%20Mapa%20de%20Empat%C3%ADa.pdf)                                                                                                                                                                                                                                                                                               |
| Entrevistas en bruto                    | [PDF](informes/Anexo.%20Entrevistas%20en%20bruto.pdf)                                                                                                                                                                                                                                                                                               |
| Cliente Ideal                           | [PDF](informes/Anexo.%20Cliente%20Ideal.pdf)                                                                                                                                                                                                                                                                                                        |

<!-- INDICE:uso-y-licencia -->

## Uso, distribución y condiciones

- [Entrada y descargas](../README.md).
- [Licencia, créditos y reutilización](../LICENSING.md).
- [Referencia ampliada de uso](Referencia-de-uso.md).
