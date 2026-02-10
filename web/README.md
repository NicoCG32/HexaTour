# Web - Gestion de contenidos

Este README describe como actualizar el contenido que consume el portal cautivo de HexaTour. El foco esta en la base de datos JSON y los assets dentro de [web/www](web/www).

> Importante
> - Todo en UTF-8 sin BOM.
> - No alteres la estructura de carpetas.
> - Los nombres de archivo deben coincidir con el slug.

## Tabla de contenidos

- [Guia rapida](#guia-rapida)
- [Estructura](#estructura)
- [Paginas del portal](#paginas-del-portal)
- [Flujo de datos](#flujo-de-datos)
- [JS principal](#js-principal)
- [Endpoints usados](#endpoints-usados)
- [Urgencias](#urgencias)
- [Actualizar contenidos](#actualizar-contenidos)
- [Compresion GZ](#compresion-gz)
- [Testeo local](#testeo-local)
- [FAQ](#faq)

## Guia rapida

1. Edita la base JSON y las imagenes en [web/www/db](web/www/db) y [web/www/img](web/www/img).
2. Si usas .gz, regeneralos (ver [Compresion GZ](#compresion-gz)).
3. Prueba en PC con el backend mock (ver [Testeo local](#testeo-local)).
4. Copia [web/www](web/www) a la SD.

## Estructura

```
www/
  db/
    index.json
    categories/
    poi/
  img/
```

Archivos clave:
- [web/www/db/index.json](web/www/db/index.json)
- [web/www/db/categories](web/www/db/categories)
- [web/www/db/poi](web/www/db/poi)

## Paginas del portal

- Visitante: [web/www/visitor/index.html](web/www/visitor/index.html) y [web/www/visitor/lugar.html](web/www/visitor/lugar.html)
- Operador: [web/www/main/index.html](web/www/main/index.html) y [web/www/main/lugar.html](web/www/main/lugar.html)
- Landing: [web/www/index.html](web/www/index.html)

## Flujo de datos

1. El usuario elige una categoria.
2. Se carga la lista de categoria desde:

```
db/categories/<categoria>.json
```

3. Al seleccionar un item, se carga la ficha desde:

```
db/poi/<categoria>/<slug>.json
```
4. Se renderizan campos, imagen principal y ruta.
5. En operador, se puede descargar PDF; en visitante, se puede imprimir.

```mermaid
flowchart LR
  Browser[Usuario en portal] --> ESP32[Servidor ESP32 (portal cautivo)]
  ESP32 --> SD[SD: /www, db, img]
  Browser --> API[/api/print-ruta o /api/route-pdf/]
  API --> ESP32
  ESP32 --> UNO[UNO impresora]
```

## JS principal

- Utilidades globales: [web/www/assets/js/common.js](web/www/assets/js/common.js)
- Visitante:
  - [web/www/assets/js/visitor-index.js](web/www/assets/js/visitor-index.js)
  - [web/www/assets/js/visitor-lugar.js](web/www/assets/js/visitor-lugar.js)
- Operador:
  - [web/www/assets/js/main-index.js](web/www/assets/js/main-index.js)
  - [web/www/assets/js/main-lugar.js](web/www/assets/js/main-lugar.js)
- Landing: [web/www/assets/js/landing.js](web/www/assets/js/landing.js)

## Endpoints usados

- `GET /api/print-ruta?cat=<categoria>&slug=<slug>&name=<nombre>&file=<cat/slug>`
  - Usado por [web/www/assets/js/visitor-lugar.js](web/www/assets/js/visitor-lugar.js) para imprimir indicaciones.
- `GET /api/route-pdf?cat=<categoria>&slug=<slug>&name=<nombre>&file=<cat/slug>&dl=1`
  - Usado por [web/www/assets/js/main-lugar.js](web/www/assets/js/main-lugar.js) para descargar PDF de la ruta.

## Urgencias

En categoria Urgencia:
- Visitante: muestra botones que despliegan mensaje local.
- Operador: abre la app de SMS con un mensaje prellenado.
  - Edita el numero en [web/www/assets/js/main-lugar.js](web/www/assets/js/main-lugar.js).

## Actualizar contenidos

### Actualizar un POI existente

1. Edita la ficha JSON del POI. Ruta esperada:

```
www/db/poi/<categoria>/<slug>.json
```

2. Si cambia el nombre visible, actualiza la lista de categoria:

```
www/db/categories/<categoria>.json
```

3. Si cambian imagenes, reemplaza archivos en:

```
www/img/<categoria>/
```

### Agregar un nuevo POI

1. Agrega el item en la lista de categoria:

```
www/db/categories/<categoria>.json
```

2. Crea la ficha del POI:

```
www/db/poi/<categoria>/<slug>.json
```

3. Actualiza el conteo en [web/www/db/index.json](web/www/db/index.json).
4. Agrega las imagenes requeridas en:

```
www/img/<categoria>/
```

### Logo del PDF

El PDF puede incluir un logo si existe en:
- [web/www/img/map/logo.jpg](web/www/img/map/logo.jpg)

El archivo [web/www/img/map/logoHexaTour.png](web/www/img/map/logoHexaTour.png) se usa como logo principal en el portal.

## Compresion GZ

Si usas archivos comprimidos en el ESP32, regenera los .gz despues de cambios en JSON o imagenes:

```powershell
Get-ChildItem -Path "web\www\db" -Filter *.gz -Recurse | Remove-Item -Force
Get-ChildItem -Path "web\www\img" -Filter *.gz -Recurse | Remove-Item -Force
Add-Type -AssemblyName System.IO.Compression.FileSystem
Get-ChildItem -Path "web\www\db" -Filter *.json -Recurse | ForEach-Object {
  $src = $_.FullName; $dst = $src + ".gz"
  $input=[IO.File]::OpenRead($src); $output=[IO.File]::Create($dst)
  $gzip=New-Object IO.Compression.GzipStream($output,[IO.Compression.CompressionMode]::Compress)
  $input.CopyTo($gzip); $gzip.Dispose(); $input.Dispose(); $output.Dispose()
}
$imgExt = @('*.jpg','*.jpeg','*.png','*.webp','*.svg')
foreach($ext in $imgExt){
  Get-ChildItem -Path "web\www\img" -Filter $ext -Recurse | ForEach-Object {
    $src = $_.FullName; $dst = $src + ".gz"
    $input=[IO.File]::OpenRead($src); $output=[IO.File]::Create($dst)
    $gzip=New-Object IO.Compression.GzipStream($output,[IO.Compression.CompressionMode]::Compress)
    $input.CopyTo($gzip); $gzip.Dispose(); $input.Dispose(); $output.Dispose()
  }
}
```

## Testeo local

1. Inicia el backend local:
  - Python: python "tools/backend-local/server.py" --root "web/www" --port 8000
2. Abre en el navegador:
   - Visitante: http://localhost:8000/visitor/
   - Operador: http://localhost:8000/main/

Si no ves los cambios, limpia cache y recarga.

## FAQ

**No se ven los cambios**
- Limpia cache del navegador y verifica que los .gz esten regenerados.

**JSON invalido**
- Revisa comas finales y comillas faltantes en los archivos de categoria o POI.
