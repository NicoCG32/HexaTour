# 01 — Arquitectura por niveles

## Arquitectura del sistema por niveles

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

Las flechas muestran el flujo de información entre componentes. Las transacciones y dependencias de código se detallan en los contratos de cada módulo.

### Nivel 3 — Dominio, contratos y adaptadores

Archivos JSON e imágenes en SD bajo /www; no hay base SQL ni RLS. Los conteos/listas y las fichas deben ser coherentes. El mock usa las fuentes del sitio; una simulación no certifica DNS cautivo, autenticación del operador ni ejecución serial real.

- Un slug/categoría debe resolver a una ficha y sus recursos.
- Agregar categoría al JSON no garantiza un botón nuevo si los HTML lo declaran de forma fija.
- El modo demo debe impedir que un mensaje simulado se interprete como impresión real.

Consultar [04-base-de-datos.md](04-base-de-datos.md) para entidades, cardinalidades y representación; [05-motor-o-nucleo-de-negocio.md](05-motor-o-nucleo-de-negocio.md) para invariantes. Las piezas marcadas como propuestas pertenecen al diseño del prototipo.

### Nivel 4 — Despliegue y distribución

**Destino:** Montaje ESP32/UNO + Demo web estática.

```text
[Revisión de fuente] -> [Verificación de su plataforma] -> [Build / artefacto]
                                                                  |
                                                          [Instalación / hosting]
                                                                  |
                                                          [Usuario y sus datos]
```

La demo de Pages contiene una copia estática del portal. El montaje local utiliza su propia tarjeta SD y los firmwares de ESP32 y UNO; actualiza cada componente siguiendo la guía correspondiente. El capítulo [09-instalacion-y-despliegue.md](09-instalacion-y-despliegue.md) concreta la puesta en marcha.

### Calidad y límites arquitectónicos

- Actualización de contenido turístico
- Energía, SD, impresora y consumibles
- Confundir información de ejemplo con orientación validada
- Operación del portal cautivo en equipos de visitantes

El rendimiento y la capacidad dependen del entorno de ejecución. Consulta las guías de instalación y las limitaciones de cada plataforma antes de desplegar.

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
