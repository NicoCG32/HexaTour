# 02 — Catálogo funcional

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** general / técnica.

## Catálogo de capacidades — revisión 2026-10-29

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

| Módulo      | Capacidad / propósito                  | Caso borde o límite                      |
| ----------- | -------------------------------------- | ---------------------------------------- |
| Consulta    | Categorías y fichas de lugares         | Archivo ausente o contenido incompleto   |
| Orientación | Texto e imagen de ruta                 | Imagen no disponible                     |
| Montaje     | Portal, SD e impresión                 | Sin papel, equipo ocupado o fallo serial |
| Operación   | Actualización de contenidos y firmware | Versiones y rutas coherentes             |
| Demo        | Experiencia sin hardware               | Impresión simulada, PDF y SMS limitados  |

Los módulos propuestos se identifican expresamente. La disponibilidad en una plataforma no se extrapola a las demás; la aceptación debe cubrir los casos borde del recorrido principal.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
