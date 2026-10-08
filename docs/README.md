# Documentación de HexaTour

HexaTour es un prototipo académico de orientación turística rural con portal local, contenido en tarjeta SD, generación de PDF e impresión térmica. Esta documentación describe la implementación disponible y distingue la prueba con mock del montaje físico.

## Por dónde empezar

| Necesidad | Documento |
| --- | --- |
| Ejecutar la web sin hardware o preparar el montaje | [README del proyecto](../README.md#guia-rapida) |
| Entender componentes, acciones y límites | [Arquitectura](Arquitectura.md) |
| Distinguir montaje físico, mock y demo disponible | [Contexto](Arquitectura.md#contexto-y-modos-de-ejecución) · [Flujo de impresión](Arquitectura.md#flujo-de-datos-y-aceptación-de-impresión) · [Distribución pública](Arquitectura.md#demo-disponible-y-distribución-pública) |
| Editar categorías, fichas e imágenes de forma coherente | [Formato de datos](Formato-de-datos.md) |
| Validar catálogo y recursos sin servidor | [Validación local y regresiones](Formato-de-datos.md#validación-local) |
| Actualizar contenido y probar el portal | [Guía web](../web/README.md) |
| Pines, configuración y protocolo ESP32–UNO | [Guía de firmware](../firmware/README.md) |
| Servidor de prueba, API mock y smoke | [Backend local](../tools/backend-local/README.md) |
| Explorar en modo demo sin API ni hardware | [Demo: activación y recorrido](Demo.md) |
| Preparar la copia pública y desplegarla en Pages | [Distribución y despliegue](Despliegue.md) |
| Conocer procedencia y alcance de los ejemplos mostrados | [Contenido de la demo](Contenido-demo.md) |
| Puesta en marcha y mantenimiento del equipo | [Manual del proveedor](manual-proveedor.md) |

Las versiones de cores Arduino y una compilación reproducible del firmware todavía no están registradas. Los datos turísticos son ejemplos sin verificación de vigencia; la procedencia gráfica declarada y las condiciones de presentación están en [Contenido de la demo](Contenido-demo.md). La [demo pública](https://nicocg32.github.io/HexaTour/) fue comprobada por HTTPS el 2026-10-07; [versión publicada y recuperación](Despliegue.md#estado).

## Circuito y fuentes editables

El cableado del montaje se conserva en [HexaTourCircuito.drawio](diagramas/HexaTourCircuito.drawio). Sus vistas exportadas son [SVG](diagramas/HexaTourCircuito.svg), [PNG](diagramas/HexaTourCircuito.png) y [JPG](diagramas/HexaTourCircuito.jpg). Antes de intervenir en hardware, contrastar el circuito con los [pines de los sketches](../firmware/README.md#pines-usados) y con el montaje disponible.

## Antecedentes académicos

Estos informes y anexos registran el desarrollo del curso. Las instrucciones de ejecución y los contratos técnicos vigentes están en las guías anteriores; los antecedentes pueden describir fases o funcionalidades proyectadas.

| Documento | Archivos |
| --- | --- |
| Informe 1: problemática turística rural | [PDF](informes/Informe%20N%C2%B01.%20Limitaciones%20de%20orientaci%C3%B3n%20en%20la%20experiencia%20tur%C3%ADstica%20rural%20en%20la%20Regi%C3%B3n%20de%20Coquimbo.pdf) · [Word](informes/Informe%20N%C2%B01.%20Limitaciones%20de%20orientaci%C3%B3n%20en%20la%20experiencia%20tur%C3%ADstica%20rural%20en%20la%20Regi%C3%B3n%20de%20Coquimbo.docx) |
| Informe 2: Hexatour, la solución | [PDF](informes/Informe%20N%C2%B02.%20Hexatour,%20la%20soluci%C3%B3n.pdf) · [Word](informes/Informe%20N%C2%B02.%20Hexatour,%20la%20soluci%C3%B3n.docx) |
| Planificación y Carta Gantt | [PDF](informes/Anexo.%20Planificaci%C3%B3n%20y%20Carta%20Gantt.pdf) |
| Matriz de Priorización | [PDF](informes/Anexo.%20Matriz%20de%20Priorizaci%C3%B3n.pdf) |
| Mapa de Empatía | [PDF](informes/Anexo.%20Mapa%20de%20Empat%C3%ADa.pdf) |
| Entrevistas en bruto | [PDF](informes/Anexo.%20Entrevistas%20en%20bruto.pdf) |
| Cliente Ideal | [PDF](informes/Anexo.%20Cliente%20Ideal.pdf) |
