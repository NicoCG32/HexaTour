# 15 — Justificación, proyección y escalabilidad

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** desarrollo del proyecto.

## Justificación y proyección

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

### Ajuste entre problema y solución

| Necesidad                    | Razón del diseño                                                            |
| ---------------------------- | --------------------------------------------------------------------------- |
| Conectividad insuficiente    | Los archivos y el portal residen en el equipo local                         |
| Orientación sólo en pantalla | La impresión proporciona una copia física cuando el montaje está disponible |
| Contenido disperso           | Categorías y fichas JSON organizan lugares con formato común                |

Capacidad de encontrar indicaciones, cobertura sin internet y tasa de acciones físicas completadas; mantenimiento por punto de información.

### Qué se puede abstraer y qué no

Las entidades, reglas y fronteras de [04-base-de-datos.md](04-base-de-datos.md) permiten evaluar reutilización. Cambiar un nombre o una categoría no prueba compatibilidad con otro sector: datos, permisos, reglas, operación y costos deben validarse de nuevo.

### Extensiones de contexto: hipótesis, no mercados validados

- Centros de interpretación
- Senderos educativos
- Museos con conectividad limitada
- Ferias o recintos con información local

No se atribuyen clientes, ventas, demanda ni superioridad sobre competidores sin evidencia. La primera validación consiste en una necesidad concreta, un flujo útil y disposición real a adoptarlo. Para juegos, el valor inicial es una experiencia disfrutable, no ahorro de horas ni una promesa educativa no ensayada.

### Límites y trade-offs

- Actualización de contenido turístico
- Energía, SD, impresora y consumibles
- Confundir información de ejemplo con orientación validada
- Operación del portal cautivo en equipos de visitantes

### Prioridad de inversión

| Prioridad   | Iniciativa                                                     | Impacto a comprobar                                                                                                                         | Criterio económico                                                    |
| ----------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Alta        | Reproducción de un punto y medición de operación/mantenimiento | Capacidad de encontrar indicaciones, cobertura sin internet y tasa de acciones físicas completadas; mantenimiento por punto de información. | Rango de esfuerzo y costo en capítulo 18; no presupuesto comprometido |
| Media       | Reproducción, soporte y recuperación por plataforma            | Menos fallos de entrega y pérdida de datos                                                                                                  | Costo recurrente separado de implementación                           |
| Estratégica | Validar una extensión/forma de sostenimiento                   | Uso y aceptación fuera del contexto inicial                                                                                                 | Investigar costos, demanda y condiciones antes de monetizar           |

Las cifras CLP/USD, supuestos, sensibilidad y retorno se presentan en [18-analisis-economico-clp-usd.md](18-analisis-economico-clp-usd.md); no son una valoración comercial del repositorio.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
