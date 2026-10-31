# 02 — Catálogo funcional

## Capacidades y límites

**Disponibilidad:** Prototipo de orientación turística con portal local, firmware y demo web. La demo permite recorrer la interfaz sin hardware y simula o deshabilita las acciones físicas.

| Módulo      | Capacidad / propósito                  | Caso borde o límite                      |
| ----------- | -------------------------------------- | ---------------------------------------- |
| Consulta    | Categorías y fichas de lugares         | Archivo ausente o contenido incompleto   |
| Orientación | Texto e imagen de ruta                 | Imagen no disponible                     |
| Montaje     | Portal, SD e impresión                 | Sin papel, equipo ocupado o fallo serial |
| Operación   | Actualización de contenidos y firmware | Versiones y rutas coherentes             |
| Demo        | Experiencia sin hardware               | Impresión simulada, PDF y SMS limitados  |

Las capacidades previstas se distinguen de las disponibles. Consulta los requisitos de la plataforma que vas a utilizar.

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
