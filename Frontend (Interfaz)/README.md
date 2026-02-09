# Frontend (Interfaz) – Gestión de contenidos

Este README describe cómo actualizar el contenido que consume el portal cautivo de HexaTour. Está enfocado en **datos, rutas e imágenes** dentro de la carpeta www.

> Importante:
> - Todo en **UTF-8 sin BOM**.
> - No alterar la estructura de carpetas.
> - Los nombres de archivo deben coincidir con el **slug**.

## Estructura relevante

```
www/
	datos/
	rutas/
	img/
```

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
- Debe coincidir exactamente en datos, rutas e imágenes.

Ejemplo de slug: restaurantee.

## Actualizar un POI existente

1. Edita los datos en www/datos/<categoria>/<slug>.txt.
2. Si cambia el nombre visible, actualiza www/datos/<categoria>/nombres.txt.
3. Si cambian las indicaciones, actualiza www/rutas/<categoria>/indicaciones<slug>ruta.txt.
4. Si cambian imágenes, reemplaza los archivos correspondientes en www/img/<categoria>/.

Ejemplo rapido (restaurantee):
- Datos: www/datos/restaurantes/restaurantee.txt
- Nombre: www/datos/restaurantes/nombres.txt
- Ruta: www/rutas/restaurantes/indicacionesrestauranteeruta.txt
- Imagenes: www/img/restaurantes/restaurantee.jpg (y variantes)

## Agregar un nuevo POI

### 1) Registrar el slug
Archivo:
```
www/datos/<categoria>/_index.txt
```
Agrega una línea con el slug.

### 2) Nombre visible
Archivo:
```
www/datos/<categoria>/nombres.txt
```
Formato:
```
<slug>|Nombre visible
```

### 3) Ficha del POI
Archivo:
```
www/datos/<categoria>/<slug>.txt
```
Campos típicos:
```
descripcion=
tpie=
tveh=
apertura=
cierre=
alertas=
```

### 4) Ruta
Archivo:
```
www/rutas/<categoria>/indicaciones<slug>ruta.txt
```

### 5) Imágenes
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
Si no se encuentra, el PDF se genera sin logo.

## Compresión opcional (GZ)

Si se usan versiones comprimidas en el ESP32, generar .gz para nuevos archivos.

## Testeo en PC (antes de copiar a la SD)

1. Abre una terminal en la carpeta www.
2. Inicia un servidor local. Opciones comunes:
	- Python: python -m http.server 8000
	- Node.js: npx serve .
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

- El slug no coincide en datos/rutas/imagenes.
- Se omite el slug en _index.txt.
- Archivos en otra codificacion que no sea UTF-8 sin BOM.

## Checklist rápido

- Slug en _index.txt
- Nombre en nombres.txt
- Ficha <slug>.txt
- Ruta indicaciones<slug>ruta.txt
- Imágenes en img/<categoria>


