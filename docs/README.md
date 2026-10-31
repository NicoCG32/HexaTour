# Documentación de HexaTour

Prototipo de orientación turística con portal local, firmware y demo web. La demo permite recorrer la interfaz sin hardware y simula o deshabilita las acciones físicas.

## Documentación por cuatro tipos

| Tipo                    | Qué encontrarás                                                 | Por dónde empezar                                                                                                                                |
| ----------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| General                 | Problemática, público, solución y motivación personal           | [Propuesta](00-problematica-cliente-y-valor.md) · [Origen](16-motivacion-y-contexto.md)                                                          |
| Técnica                 | Arquitectura, dominio, datos, interfaz y puesta en marcha       | [Arquitectura](01-arquitectura-general.md) · [Instalación](09-instalacion-y-despliegue.md)                                                       |
| Desarrollo del proyecto | Etapas, metodología, justificación, proyección y costos CLP/USD | [Metodología](17-desarrollo-y-metodologia.md) · [Proyección](15-escalabilidad-y-nuevos-mercados.md) · [Costos](18-analisis-economico-clp-usd.md) |
| Académica/formativa     | Contexto del curso, informes y anexos de la etapa formativa     | [Catálogo académico](academica/README.md)                                                                                                        |

## Rutas de lectura

- **Conocer el proyecto:** [propuesta](00-problematica-cliente-y-valor.md) → [motivación](16-motivacion-y-contexto.md) → [funcionalidades](02-funcionalidades.md).
- **Utilizarlo o desplegarlo:** [recorrido](03-flujo-de-usuario.md) → [instalación](09-instalacion-y-despliegue.md).
- **Desarrollar o contribuir:** [arquitectura](01-arquitectura-general.md) → [dominio y datos](04-base-de-datos.md) → [reglas](05-motor-o-nucleo-de-negocio.md).
- **Evaluar su evolución:** [metodología](17-desarrollo-y-metodologia.md) → [proyección](15-escalabilidad-y-nuevos-mercados.md) → [costos](18-analisis-economico-clp-usd.md).

## Tabla de contenidos

| Capítulo | Documento                                                                          |
| -------- | ---------------------------------------------------------------------------------- |
| 00       | [Problemática, cliente y solución](00-problematica-cliente-y-valor.md)             |
| 01       | [Arquitectura por niveles](01-arquitectura-general.md)                             |
| 02       | [Catálogo funcional](02-funcionalidades.md)                                        |
| 03       | [Recorrido y estados](03-flujo-de-usuario.md)                                      |
| 04       | [Dominio, entidades y persistencia](04-base-de-datos.md)                           |
| 05       | [Reglas y núcleo](05-motor-o-nucleo-de-negocio.md)                                 |
| 06       | [Integraciones y asistencia](06-capa-de-ia-o-analisis.md)                          |
| 07       | [Diseño y accesibilidad](07-diseno-e-identidad.md)                                 |
| 08       | [Salidas y entregables](08-exportacion-e-informes.md)                              |
| 09       | [Puesta en marcha y distribución](09-instalacion-y-despliegue.md)                  |
| 15       | [Justificación, proyección y escalabilidad](15-escalabilidad-y-nuevos-mercados.md) |
| 16       | [Motivación personal y contexto](16-motivacion-y-contexto.md)                      |
| 17       | [Etapas y metodología](17-desarrollo-y-metodologia.md)                             |
| 18       | [Escenarios económicos CLP / USD](18-analisis-economico-clp-usd.md)                |

## Guías especializadas

- [Arquitectura de HexaTour](Arquitectura.md).
- [Contenido de la demo](Contenido-demo.md).
- [Demo sin hardware](Demo.md).
- [Distribuir la demo estática](Despliegue.md).
- [Formato de datos del portal](Formato-de-datos.md).
- [Manual del proveedor - HexaTour](manual-proveedor.md).
- [Referencia ampliada de uso](Referencia-de-uso.md).
- [HexaTourCircuito.drawio](diagramas/HexaTourCircuito.drawio).
- [SVG](diagramas/HexaTourCircuito.svg).
- [PNG](diagramas/HexaTourCircuito.png).
- [JPG](diagramas/HexaTourCircuito.jpg).

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

## Uso y distribución

[Presentación y descargas](../README.md) · [Licencia y créditos](../LICENSING.md).
