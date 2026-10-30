# 00 — Problemática, cliente y solución

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** general.

## Síntesis general — HexaTour

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

### Problemática

En recorridos turísticos rurales, la conectividad y la orientación pueden ser insuficientes. La información de lugares, rutas y servicios debe poder consultarse cerca del punto de uso y conservar una alternativa material sin depender de internet del visitante.

### Cliente, usuario y beneficiario

| Perfil                         | Contexto                             | Necesidad                                            |
| ------------------------------ | ------------------------------------ | ---------------------------------------------------- |
| Usuario                        | Visitante de un circuito rural       | Consultar lugares y orientarse con baja conectividad |
| Operador                       | Responsable del punto de información | Mantener contenido, equipo y consumibles             |
| Beneficiario/cliente potencial | Organización turística local         | Evaluar cobertura y mantenimiento antes de adoptar   |

### Solución y límites

Un ESP32-S3 ofrece un portal local con contenido en SD y coordina con Arduino UNO la impresión térmica de indicaciones. El visitante usa su navegador; el montaje combina red local, fichas y salida física. Una demo web separada comunica la experiencia con acciones simuladas.

### Por qué corresponde al problema

| Fricción / necesidad         | Mecanismo de la solución                                                    |
| ---------------------------- | --------------------------------------------------------------------------- |
| Conectividad insuficiente    | Los archivos y el portal residen en el equipo local                         |
| Orientación sólo en pantalla | La impresión proporciona una copia física cuando el montaje está disponible |
| Contenido disperso           | Categorías y fichas JSON organizan lugares con formato común                |

### Validación pendiente o continua

Capacidad de encontrar indicaciones, cobertura sin internet y tasa de acciones físicas completadas; mantenimiento por punto de información.

La motivación del creador se presenta en [16-motivacion-y-contexto.md](16-motivacion-y-contexto.md); el análisis de costos y proyección se separa en [18-analisis-economico-clp-usd.md](18-analisis-economico-clp-usd.md). Afinidad personal, un prototipo o cercanía con una organización no equivalen a demanda/venta demostrada.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
