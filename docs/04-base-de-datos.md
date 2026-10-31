# 04 — Dominio, entidades y persistencia

## Dominio y representación de datos

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

El diagrama describe relaciones del dominio. Los adaptadores y el esquema de persistencia determinan cómo se mantienen esas relaciones al guardar o recuperar datos.

### Consistencia y evolución

- Un slug/categoría debe resolver a una ficha y sus recursos.
- Agregar categoría al JSON no garantiza un botón nuevo si los HTML lo declaran de forma fija.
- El modo demo debe impedir que un mensaje simulado se interprete como impresión real.
- La falta de PDF o mensajería en la demo se comunica, no se sustituye por una petición fallida al equipo privado.
- Los archivos comprimidos son artefactos derivados; sus fuentes sin comprimir deben permitir reproducir el montaje.

Antes de cambiar el formato de almacenamiento, comprueba la migración y la restauración con una copia de prueba. Conserva la versión del respaldo y verifica su compatibilidad con la aplicación que lo abrirá.

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
