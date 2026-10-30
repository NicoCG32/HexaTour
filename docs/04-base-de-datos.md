# 04 — Dominio, entidades y persistencia

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** técnica.

## Dominio y representación de datos

Revisión documental: 2026-10-29. Base `3ebc11f12a86` en `main`; árbol inicialmente limpio. La inspección de fuentes no sustituye pruebas de ejecución.

**Estado y alcance:** Prototipo académico cerrado con demo sin hardware y compilación de firmware documentadas. La impresión, SD y portal cautivo pertenecen al montaje local; la demo simula o deshabilita esas acciones.

### Entidades y conceptos

| Entidad / concepto | Identidad y significado                        | Representación / estado                       |
| ------------------ | ---------------------------------------------- | --------------------------------------------- |
| Categoría          | Identificador/carpeta y lista de lugares       | JSON estático                                 |
| POI                | Slug, nombre, campos y referencias de imágenes | Ficha JSON                                    |
| Ruta               | Texto/imagen de indicaciones del lugar         | Contenido de la ficha                         |
| TrabajoImpresión   | Petición, disponibilidad y confirmación        | Estado operativo del montaje                  |
| Configuración      | Parámetros de equipo y acciones                | Firmware/archivo local; sin secretos públicos |

### Relaciones de dominio

```text
[Categoría] -- 1:N --> [POI]
[POI] -- contiene --> [Ruta]
[POI] -- referencia --> [Imagen]
[TrabajoImpresión] -- usa --> [Ruta]
```

| Origen           | Cardinalidad / relación | Destino | Semántica                                    |
| ---------------- | ----------------------- | ------- | -------------------------------------------- |
| Categoría        | 1:N                     | POI     | La lista debe resolver a fichas existentes   |
| POI              | contiene                | Ruta    | Texto e imagen según contenido disponible    |
| POI              | referencia              | Imagen  | Nombre y archivo deben coincidir             |
| TrabajoImpresión | usa                     | Ruta    | El contenido consultado origina la solicitud |

### Persistencia y garantías

Archivos JSON e imágenes en SD bajo /www; no hay base SQL ni RLS. Los conteos/listas y las fichas deben ser coherentes. El mock usa las fuentes del sitio; una simulación no certifica DNS cautivo, autenticación del operador ni ejecución serial real.

La cardinalidad de dominio no prueba que exista una FK física. Revisar adaptadores/migraciones para identificar qué se valida por esquema, por caso de uso o por lectura. No usar «RLS» para almacenamiento que no dispone de esas políticas.

### Consistencia y evolución

- Un slug/categoría debe resolver a una ficha y sus recursos.
- Agregar categoría al JSON no garantiza un botón nuevo si los HTML lo declaran de forma fija.
- El modo demo debe impedir que un mensaje simulado se interprete como impresión real.
- La falta de PDF o mensajería en la demo se comunica, no se sustituye por una petición fallida al equipo privado.
- Los archivos comprimidos son artefactos derivados; sus fuentes sin comprimir deben permitir reproducir el montaje.

Cambios de formato, referencias y restauración se comprueban con datos de prueba. El respaldo/artefacto debe indicar versión; la documentación no autoriza transformar datos reales ni rebajar un esquema para abrirlo con un ejecutable anterior.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
