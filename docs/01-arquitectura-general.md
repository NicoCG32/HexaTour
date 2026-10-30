# 01 — Arquitectura por niveles

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** técnica.

## Arquitectura del sistema por niveles

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

### Nivel 1 — Contexto y fronteras de ejecución

```text
[Visitante / navegador] -> [Wi-Fi local ESP32-S3]
                                   |
                           [Portal y API local]
                             |            |
                             v            v
                      [SD: /www]      [Arduino UNO]
                      HTML/JSON/img        |
                                     [Ticketera]

[Demo Pages] -> [Navegador: datos de muestra / simulación]
[Mock Python] -> [Prueba de portal y endpoints sin hardware]
```

Un ESP32-S3 ofrece un portal local con contenido en SD y coordina con Arduino UNO la impresión térmica de indicaciones. El visitante usa su navegador; el montaje combina red local, fichas y salida física. Una demo web separada comunica la experiencia con acciones simuladas.

### Nivel 2 — Componentes y responsabilidades

| Componente | Responsabilidad                       | Fuente                                                                                      |
| ---------- | ------------------------------------- | ------------------------------------------------------------------------------------------- |
| Portal     | HTML/CSS/JS para visitante y operador | [web/www](../web/www)                                                                       |
| Contenidos | Categorías, POI e imágenes            | [web/www/db](../web/www/db)                                                                 |
| Cliente    | Lectura y resolución de rutas         | [web/www/assets/js/common.js](../web/www/assets/js/common.js)                               |
| ESP32      | Wi-Fi, HTTP, SD y coordinación        | [firmware/esp32/HexaTour/HexaTour.ino](../firmware/esp32/HexaTour/HexaTour.ino)             |
| UNO        | Impresión y confirmación              | [firmware/uno/ImpresoraUNO/ImpresoraUNO.ino](../firmware/uno/ImpresoraUNO/ImpresoraUNO.ino) |
| Mock       | API de prueba local                   | [tools/backend-local/server.py](../tools/backend-local/server.py)                           |

Las flechas del contexto representan comunicación/flujo. No se deduce una dependencia de código o transacción compartida sólo porque dos componentes intercambien datos.

### Nivel 3 — Dominio, contratos y adaptadores

Archivos JSON e imágenes en SD bajo /www; no hay base SQL ni RLS. Los conteos/listas y las fichas deben ser coherentes. El mock usa las fuentes del sitio; una simulación no certifica DNS cautivo, autenticación del operador ni ejecución serial real.

- Un slug/categoría debe resolver a una ficha y sus recursos.
- Agregar categoría al JSON no garantiza un botón nuevo si los HTML lo declaran de forma fija.
- El modo demo debe impedir que un mensaje simulado se interprete como impresión real.

Consultar [04-base-de-datos.md](04-base-de-datos.md) para entidades, cardinalidades y representación; [05-motor-o-nucleo-de-negocio.md](05-motor-o-nucleo-de-negocio.md) para invariantes. En un prototipo, las piezas rotuladas propuestas no son clases implementadas.

### Nivel 4 — Despliegue y distribución

**Destino:** Montaje ESP32/UNO + Demo web estática.

```text
[Revisión de fuente] -> [Verificación de su plataforma] -> [Build / artefacto]
                                                                  |
                                                          [Instalación / hosting]
                                                                  |
                                                          [Usuario y sus datos]
```

La persistencia y los servicios del contexto anterior conservan sus propias fronteras. Distribuir un APK no incorpora automáticamente el servidor, una PWA no acredita un instalador y el firmware requiere dispositivo. El capítulo [09-instalacion-y-despliegue.md](09-instalacion-y-despliegue.md) concreta la puesta en marcha.

### Calidad y límites arquitectónicos

- Actualización de contenido turístico
- Energía, SD, impresora y consumibles
- Confundir información de ejemplo con orientación validada
- Operación del portal cautivo en equipos de visitantes

No se publican garantías de latencia, disponibilidad o escala sin medición para la revisión/entorno concretos. Un diagrama explica responsabilidades; no es una certificación de ejecución o seguridad del servicio desplegado.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
