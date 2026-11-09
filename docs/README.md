# Documentación · HexaTour

Guías para conocer el proyecto, probar el portal y reproducir el montaje. La [matriz de funcionalidades](02-funcionalidades.md) detalla qué ofrece el hardware, el simulador y la demo web.

## Cuatro áreas

| Área | Qué responde | Documentos |
| --- | --- | --- |
| **General** | Qué problema aborda, a quién sirve y qué ofrece. | [00 Problema](00-problematica-cliente-y-valor.md), [02 Capacidades](02-funcionalidades.md), [16 Origen](16-motivacion-y-contexto.md) |
| **Técnica** | Cómo se conectan sus piezas, qué datos se usan y cómo se comporta el sistema. | [01 Arquitectura](01-arquitectura-general.md), [03 Flujos](03-flujo-de-usuario.md), [04 Datos](04-base-de-datos.md), [05 Reglas](05-motor-o-nucleo-de-negocio.md), [06 Integraciones](06-integraciones-del-sistema.md), [07 UX](07-diseno-e-identidad.md), [08 Salidas](08-exportacion-e-informes.md) |
| **Desarrollo** | Cómo probarlo, reconstruirlo, modificarlo y evaluar su continuidad. | [09 Ejecución](09-instalacion-y-despliegue.md), [17 Proceso](17-desarrollo-y-metodologia.md), [15 Evolución](15-escalabilidad-y-nuevos-mercados.md), [18 Costos](18-analisis-economico-clp-usd.md) |
| **Académica / formativa** | Qué se investigó en 2025, quiénes participaron y qué se entregó. | [Curso, equipo, informes y anexos](academica/README.md) |

## Rutas rápidas

**Para conocer la idea:** [problema](00-problematica-cliente-y-valor.md) → [funcionalidades](02-funcionalidades.md) → [origen](16-motivacion-y-contexto.md).

**Para trabajar con el sistema:** [arquitectura](01-arquitectura-general.md) → [modelo JSON](04-base-de-datos.md) → [compilación y pruebas](09-instalacion-y-despliegue.md).

**Para revisar el curso:** [equipo y documentos originales](academica/README.md) → [lectura crítica de los informes](academica/02-lectura-critica-de-los-informes.md) → [metodología](17-desarrollo-y-metodologia.md).

**Para evaluar conveniencia y rentabilidad:** [propuesta](00-problematica-cliente-y-valor.md) → [estudio económico](18-analisis-economico-clp-usd.md) → [mercado y posicionamiento](19-mercado-y-validacion-comercial.md) → [plan de validación](20-validacion-operativa-y-pilotos.md).

## Estudios estratégicos y validación

- [18 · Costos, rentabilidad y sostenibilidad: prefactibilidad, escenarios y punto de equilibrio](18-analisis-economico-clp-usd.md).
- [19 · Mercado, compradores posibles, sustitutos y evidencia externa](19-mercado-y-validacion-comercial.md).
- [20 · Seguridad, montaje integrado y diseño de pruebas con visitantes](20-validacion-operativa-y-pilotos.md).
- [Lectura crítica del Informe N.º 2: presupuesto histórico verificado, autoría, matriz y KPI](academica/02-lectura-critica-de-los-informes.md).
- [Materiales de la maqueta realmente presentada y estimación trazable de costo de reposición de 2026](academica/03-costeo-maqueta-fisica.md).

Las proyecciones financieras **no se confunden con los costos preliminares del informe académico**. Se leyó y cotejó íntegramente el **Informe N.º 2 en PDF**, idéntico a la copia versionada en GitHub: permite citar directamente los **cuatro presupuestos 2025**, el consumo y mantenimiento esperados, así como los KPI propuestos. Todavía requieren evidencia independiente las **facturas, el costo de producción real, la validación física y los ingresos**.

## Guías de implementación

- [Arquitectura ampliada y contratos de los endpoints](Arquitectura.md).
- [Formato exacto y validación de datos](Formato-de-datos.md).
- [Portal y documentación de uso](Referencia-de-uso.md).
- [Demo y sus límites](Demo.md) · [contenido de ejemplo](Contenido-demo.md) · [publicación estática](Despliegue.md).
- [Manual del proveedor](manual-proveedor.md) · [firmware, pines y protocolo](../firmware/README.md) · [reproducción de la compilación](../firmware/Compilacion.md).
- [Simulador local](../tools/backend-local/README.md) · [gestión del contenido](../web/README.md).

## Diagramas

Los diagramas de arquitectura, flujo, modelo de datos y estados utilizan **Mermaid** y se muestran en las páginas Markdown de GitHub. Sus fuentes editables están en [`diagramas/modelos/`](diagramas/modelos/).

## Circuito y fuentes editables

El circuito del montaje está disponible en [Draw.io](diagramas/HexaTourCircuito.drawio), [SVG](diagramas/HexaTourCircuito.svg), [PNG](diagramas/HexaTourCircuito.png) y [JPG](diagramas/HexaTourCircuito.jpg). El [mapa de conexiones](diagramas/HexaTourConexionesRevisadas.svg) resume los pines de los sketches. Contrasta ambos con la [guía de firmware](../firmware/README.md#pines-usados) antes de cablear.

## Historia y documentación vigente

Los [informes y anexos académicos](academica/README.md) registran la investigación y las propuestas del curso. Para instalar o modificar la versión actual, utiliza las guías técnicas.

[Volver a la presentación](../README.md) · [Licencia y créditos](../LICENSING.md).
