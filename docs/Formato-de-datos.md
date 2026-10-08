# Formato de datos del portal

[Índice técnico](README.md) · [Actualizar contenidos](../web/README.md#actualizar-contenidos) · [Arquitectura](Arquitectura.md)

## Raíz y convenciones

Los datos son archivos JSON UTF-8 sin BOM dentro de [web/www/db](../web/www/db). No requieren un motor de base de datos. En el PC la raíz del sitio es `web/www`; en la SD se conserva como `/www`.

```text
www/
  db/index.json
  db/categories/<categoria>.json
  db/poi/<categoria>/<slug>.json
  img/<categoria>/...
```

Categorías y slugs son identificadores de archivo estables, en minúsculas y sin espacios, tildes ni separadores de ruta. En los datos actuales contienen letras y números. Las etiquetas y nombres visibles pueden contener espacios y acentos. Usar capitalización exacta para que las rutas funcionen también en sistemas sensibles a mayúsculas.

## Catálogo: db/index.json

[Ejemplo completo actual](../web/www/db/index.json).

| Campo | Tipo | Significado |
| --- | --- | --- |
| `version` | Entero | Versión del catálogo; valor actual 1 |
| `categories` | Lista de objetos | Categorías documentadas |
| `categories[].id` | Texto | Identificador/carpeta, por ejemplo `campings` |
| `categories[].label` | Texto | Etiqueta visible, por ejemplo `Campings` |
| `categories[].count` | Entero no negativo | Número de lugares en esa categoría |

Actualmente hay 9 categorías y 27 POI. `Urgencia` es una opción especial de la interfaz, sin categoría ni fichas JSON dentro del catálogo actual. No debe contarse como una décima categoría de datos.

## Lista: db/categories/<categoria>.json

[Ejemplo: campings](../web/www/db/categories/campings.json).

| Campo | Tipo | Significado |
| --- | --- | --- |
| `category` | Texto | Debe coincidir con el nombre del archivo sin `.json` y el id del catálogo |
| `label` | Texto | Etiqueta visible de la categoría |
| `items` | Lista de objetos | Lugares en el orden en que se muestran en la web |
| `items[].slug` | Texto | Referencia a `db/poi/<categoria>/<slug>.json` |
| `items[].name` | Texto | Nombre visible del lugar; mantenerlo igual al de su ficha |

La web consume `items` para construir la lista de lugares. El nombre de la carpeta lo obtiene de la etiqueta elegida mediante `catFolder()` en [common.js](../web/www/assets/js/common.js).

## Ficha: db/poi/<categoria>/<slug>.json

[Ejemplo completo: camping1](../web/www/db/poi/campings/camping1.json).

| Campo | Tipo | Uso |
| --- | --- | --- |
| `slug` | Texto no vacío | Coincide con el nombre de la ficha sin `.json` |
| `name` | Texto no vacío | Título y nombre del POI |
| `category` | Texto no vacío | Coincide con la carpeta de la ficha y el catálogo |
| `fields` | Objeto | Información visible descrita abajo |
| `route` | Objeto | Contiene el texto de indicaciones |
| `route.text` | Texto | Indicaciones para ticket y PDF; admite saltos de línea JSON `\n` |
| `images` | Objeto | Rutas de recursos del sitio |
| `images.main` | Texto | Imagen principal de la ficha |
| `images.route` | Texto | Imagen de la ruta; preferir JPEG para que también la use el PDF del ESP32 |
| `images.main_640`, `images.main_1280` | Texto | Variantes de imagen principal presentes en los datos |
| `images.route_640`, `images.route_1280` | Texto | Variantes de ruta presentes en los datos |

El validador exige `slug`, `name`, `category`, los seis textos de `fields`, `route.text` e imágenes `main` y `route`. Los textos de `fields` y `route.text` admiten valores vacíos: la interfaz muestra `—` o mantiene deshabilitadas las acciones, según el campo. Las variantes 640/1280 son opcionales, pero cuando se declaran deben apuntar a archivos presentes; los scripts de ficha actuales no las seleccionan automáticamente.

| Campo dentro de `fields` | Tipo actual | Presentación |
| --- | --- | --- |
| `descripcion` | Texto | Descripción del lugar |
| `tpie` | Texto | Tiempo a pie, con unidad; por ejemplo `13 min` |
| `tveh` | Texto | Tiempo en vehículo, con unidad |
| `apertura` | Texto | Hora de apertura presentada al usuario |
| `cierre` | Texto | Hora de cierre presentada al usuario |
| `alertas` | Texto | Observaciones mostradas en la ficha |

Los tiempos y horarios se presentan como texto: el portal no los calcula ni interpreta como una agenda. Para campos ausentes o vacíos, `fillPoiFields()` muestra `—`.

## Imágenes y rutas

Las referencias de los datos actuales son relativas a la raíz del sitio, por ejemplo `img/campings/camping1.jpg` e `img/campings/rutacamping1.jpg`. No agregar `web/www` ni `/www` al valor JSON: son ubicaciones del PC y del almacenamiento físico, no parte de esa referencia relativa.

Desde `/visitor/` o `/main/`, `resolveAssetPath()` antepone `../` para llegar a esos recursos. Si falta `images.main`, los scripts prueban `img/<categoria>/<slug>.jpg`; si falta `images.route`, prueban `img/<categoria>/ruta<slug>.jpg`. Una referencia no vacía a un archivo inexistente no activa necesariamente esa alternativa: conservar todos los recursos referenciados.

El ESP32 usa `images.route` para intentar incorporar el JPEG en el PDF. Las variantes y cualquier `.gz` son recursos adicionales; los originales sin comprimir deben permanecer disponibles.

## Coherencia al editar

1. Para un nuevo lugar, añadir el item a su lista, crear la ficha, agregar sus imágenes y actualizar `categories[].count` en el catálogo.
2. Mantener slug y categoría iguales entre catálogo, lista, carpeta y ficha. Evitar duplicados y fichas no listadas.
3. Mantener nombres iguales entre lista y ficha. Comprobar presencia de todas las imágenes referenciadas.
4. Si cambia el slug, actualizar archivo, lista, ficha y recursos/rutas que lo usen; el nombre visible por sí solo no requiere cambiarlo.
5. Para una nueva categoría, además de JSON, revisar los botones en [visitor/index.html](../web/www/visitor/index.html) y [main/index.html](../web/www/main/index.html), y la conversión de etiqueta a carpeta en `common.js`. El índice JSON no genera esos botones.
6. Probar lista → ficha → imagen de ruta y las acciones mediante el [mock local](../tools/backend-local/README.md). Después actualizar la carpeta `/www` de la SD y probar el montaje por separado.

## Validación local

Desde la raíz del repositorio, con Python 3.10 o posterior, sin servidor ni paquetes externos:

```bash
python test/validate_data.py
python -m unittest discover -s test -p "test_*.py"
```

[validate_data.py](../test/validate_data.py) devuelve **0** si el conjunto es coherente y **1** si encuentra errores de contenido. La salida identifica rutas y resume categorías, fichas listadas y referencias gráficas. Para validar una copia de la raíz web o un artefacto preparado:

```bash
python test/validate_data.py --root web/www
```

Sin `--root`, localiza `web/www` respecto al archivo del validador, independientemente de la carpeta de ejecución. Un `--root` relativo se interpreta desde la carpeta actual; debe apuntar al sitio completo, no a `db/`.

Comprueba:

- JSON UTF-8 sin BOM, objetos esperados y ausencia de claves duplicadas o constantes no válidas como NaN.
- Versión positiva, catálogo no vacío, identificadores con letras minúsculas/números, categorías únicas y conteos enteros no negativos.
- Coincidencia de categoría y etiqueta entre catálogo/lista; conteos iguales al tamaño de lista y número de fichas; slugs únicos.
- Correspondencia lista ↔ archivo POI, nombre/slug/categoría de cada ficha y campos obligatorios con los tipos descritos arriba. Los nombres visibles pueden repetirse si los slugs son diferentes.
- Presencia de `images.main`, `images.route` y todos los recursos gráficos declarados, incluidas variantes opcionales. Rutas relativas bajo `img/`, con capitalización exacta incluso en Windows, sin URLs, parámetros, fragmentos, rutas absolutas, escapes `%` ni componentes `.`/`..`; el destino resuelto debe permanecer dentro de la raíz web.
- Ausencia de fichas, listas o carpetas de categorías no declaradas en el catálogo.

[test_validate_data.py](../test/test_validate_data.py) ejerce casos válidos y alteraciones sobre un catálogo temporal, incluidos fallos de la CLI. La prueba de enlace simbólico se omite si el sistema no permite crear uno; esa omisión no equivale a haber comprobado ese caso.

El validador verifica existencia de archivos, no decodificación de imágenes, contenido de `.gz` opcionales, botones HTML/mapeo JS, render visual, exactitud turística ni permisos de uso. El [smoke](../tools/backend-local/README.md#smoke-test) comprueba la API mock y un POI de ejemplo; complementa esta validación sin sustituir el recorrido completo de la demo o la prueba física. Antes de distribuir contenido, revisar también la [procedencia y alcance de los ejemplos](Contenido-demo.md).
