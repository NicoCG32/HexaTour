# Frontend (Interfaz) – Gestión de contenidos

Este README describe cómo actualizar el contenido que consume el portal cautivo de HexaTour. Está enfocado en la **base de datos JSON** y las imágenes dentro de la carpeta www.

> Importante:
> - Todo en **UTF-8 sin BOM**.
> - No alterar la estructura de carpetas.
> - Los nombres de archivo deben coincidir con el **slug**.

## Estructura relevante

```
www/
	db/
		index.json
		categories/
		poi/
	img/
```

Nota: la base actual se mantiene en `db/` y las imagenes en `img/`.

## Categorías disponibles

- campings
- ferias
- hospedajes
- pisqueras
- plazas
- restaurantes
- rios
- servicios
- universidad

## Slug (identificador)

Reglas:
- Solo minúsculas.
- Sin espacios ni acentos.
- Debe coincidir exactamente entre `db/poi`, `db/categories` y `img`.

Ejemplo de slug: restaurante1 (los slugs son numericos por categoria).

## Actualizar un POI existente

1. Edita la ficha JSON en www/db/poi/<categoria>/<slug>.json.
2. Si cambia el nombre visible, actualiza tambien www/db/categories/<categoria>.json.
3. Si cambian imagenes, reemplaza los archivos en www/img/<categoria>/.

Ejemplo rapido (restaurante1):
- Ficha: www/db/poi/restaurantes/restaurante1.json
- Lista: www/db/categories/restaurantes.json
- Imagenes: www/img/restaurantes/restaurante1.jpg (y variantes)

## Agregar un nuevo POI

### 1) Agregar a la lista de categoria
Archivo:
```
www/db/categories/<categoria>.json
```
Agrega un item:
```
{"slug":"<slug>","name":"Nombre visible"}
```

### 2) Crear la ficha JSON
Archivo:
```
www/db/poi/<categoria>/<slug>.json
```
Campos tipicos:
```
{
	"slug": "<slug>",
	"name": "Nombre visible",
	"category": "<categoria>",
	"fields": {
		"descripcion": "",
		"tpie": "",
		"tveh": "",
		"apertura": "",
		"cierre": "",
		"alertas": ""
	},
	"route": {
		"text": ""
	},
	"images": {
		"main": "img/<categoria>/<slug>.jpg",
		"main_640": "img/<categoria>/<slug>-640.jpg",
		"main_1280": "img/<categoria>/<slug>-1280.jpg",
		"route": "img/<categoria>/ruta<slug>.jpg",
		"route_640": "img/<categoria>/ruta<slug>-640.jpg",
		"route_1280": "img/<categoria>/ruta<slug>-1280.jpg"
	}
}
```

### 3) Actualizar index global
Archivo:
```
www/db/index.json
```
Actualiza el `count` de la categoria si corresponde.

### 4) Imágenes
Archivos requeridos:
```
<slug>.jpg
<slug>-640.jpg
<slug>-1280.jpg
ruta<slug>.jpg
ruta<slug>-640.jpg
ruta<slug>-1280.jpg
```

## Ajuste de logo para PDF de ruta

El PDF puede incluir un logo si existe en:
```
www/img/map/logo.jpg
```
`logo.jpg` se usa en el PDF de ruta generado por el ESP32.

`logoHexaTour.png` se usa como logo principal en el portal cautivo.

## Compresión (GZ)

Si usas archivos comprimidos en el ESP32, regenera los .gz despues de cambios en JSON o imagenes:

```powershell
Get-ChildItem -Path "Frontend (Interfaz)\www\db" -Filter *.gz -Recurse | Remove-Item -Force
Get-ChildItem -Path "Frontend (Interfaz)\www\img" -Filter *.gz -Recurse | Remove-Item -Force
Add-Type -AssemblyName System.IO.Compression.FileSystem
Get-ChildItem -Path "Frontend (Interfaz)\www\db" -Filter *.json -Recurse | ForEach-Object {
	$src = $_.FullName; $dst = $src + ".gz"
	$input=[IO.File]::OpenRead($src); $output=[IO.File]::Create($dst)
	$gzip=New-Object IO.Compression.GzipStream($output,[IO.Compression.CompressionMode]::Compress)
	$input.CopyTo($gzip); $gzip.Dispose(); $input.Dispose(); $output.Dispose()
}
$imgExt = @('*.jpg','*.jpeg','*.png','*.webp','*.svg')
foreach($ext in $imgExt){
	Get-ChildItem -Path "Frontend (Interfaz)\www\img" -Filter $ext -Recurse | ForEach-Object {
		$src = $_.FullName; $dst = $src + ".gz"
		$input=[IO.File]::OpenRead($src); $output=[IO.File]::Create($dst)
		$gzip=New-Object IO.Compression.GzipStream($output,[IO.Compression.CompressionMode]::Compress)
		$input.CopyTo($gzip); $gzip.Dispose(); $input.Dispose(); $output.Dispose()
	}
}
```

## Testeo en PC (antes de copiar a la SD)

1. Abre una terminal en la carpeta www.
2. Inicia el backend local (mock) para simular la API del ESP32:
	- Python: python LocalBackend/server.py --root "Frontend (Interfaz)/www" --port 8000
3. Abre en el navegador:
	- Visitante: http://localhost:8000/visitor/
	- Operador: http://localhost:8000/main/
4. Revisa que los cambios se vean y que los datos carguen bien.

Si no ves los cambios, limpia cache:
- En PC (Chrome/Edge): recarga forzada con Ctrl+Shift+R o abre DevTools y activa Disable cache mientras pruebas.
- Borra datos del sitio para localhost (Site settings -> Clear data).

## Testeo local (servidor del ESP32)

1. Copia la carpeta www a la SD.
2. Enciende el equipo y conéctate al Wi-Fi HexaTour.
3. Abre el portal:
	- Visitante: http://192.168.4.1/visitor/
	- Operador: http://192.168.4.1/main/
4. Verifica que los cambios aparezcan en el POI editado.

Si no ves los cambios, limpia cache:
- En PC (Chrome/Edge): recarga forzada con Ctrl+Shift+R o abre DevTools y activa Disable cache mientras pruebas.
- Borra datos del sitio para 192.168.4.1 (Site settings -> Clear data).
- En celular: usa modo incognito o borra cache del navegador antes de probar.

## Errores comunes

- El slug no coincide entre `db/categories` y `db/poi`.
- Falta una ruta o imagen declarada en `images`.
- Archivos en otra codificacion que no sea UTF-8 sin BOM.
- Si se siente lento, verifica que los .gz esten presentes y prueba limpiar cache.
- JSON invalido (coma final o comillas faltantes) en fichas o listas.
- Rutas de imagen con mayusculas o nombres distintos a los archivos reales.
- Cambios en JSON o imagenes sin regenerar los .gz correspondientes.

## Checklist rápido

- Item en db/categories/<categoria>.json
- Ficha db/poi/<categoria>/<slug>.json
- Ruta en route.text
- Imagenes en img/<categoria>


