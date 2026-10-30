# 03 — Recorrido y estados

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** general / técnica.

## Recorrido operativo y estados

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

1. Conectarse al equipo local o abrir demo.
2. Elegir categoría y lugar.
3. Consultar ficha y ruta.
4. Solicitar la acción disponible en esa modalidad.
5. Conservar indicaciones y reportar un fallo de contenido/equipo al operador.

### Confirmación y resultado

Un slug/categoría debe resolver a una ficha y sus recursos.

Los archivos comprimidos son artefactos derivados; sus fuentes sin comprimir deben permitir reproducir el montaje.

En formularios/operaciones, distinguir captura, revisión, confirmación, resultado y fallo. Cancelar una previsualización no debe anunciar un cambio no confirmado; cuando existe una operación persistente, su recuperación sigue el contrato específico. En juegos, las fases de simulación se definen en el núcleo y la vista refleja esas transiciones.

### Criterio de aceptación del recorrido

Capacidad de encontrar indicaciones, cobertura sin internet y tasa de acciones físicas completadas; mantenimiento por punto de información.

Validar inicio, camino principal, error relevante, cancelación y reapertura según la plataforma; registrar también los escenarios aún no ejecutados. Para HexaTour, atender especialmente: actualización de contenido turístico.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
