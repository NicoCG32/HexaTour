# 00 — Problemática, cliente y solución

## Síntesis general — HexaTour

**Disponibilidad:** Prototipo de orientación turística con portal local, firmware y demo web. La demo permite recorrer la interfaz sin hardware y simula o deshabilita las acciones físicas.

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

Puedes conocer el origen del proyecto en [16-motivacion-y-contexto.md](16-motivacion-y-contexto.md); el análisis de costos y proyección se separa en [18-analisis-economico-clp-usd.md](18-analisis-economico-clp-usd.md).

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
