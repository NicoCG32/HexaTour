# README – Guía para Agregar un Nuevo POI al Portal HexaTour

Consideración: La tarjeta SD debe estar en formato FAT32, en caso de formatear.

Este documento explica paso a paso cómo agregar un **Punto de Interés (POI)** a HexaTour, manteniendo la compatibilidad con el frontend y el firmware del ESP32.
La estructura relevante se encuentra en:

```
www/
 ├─ datos/
 ├─ rutas/
 └─ img/
```

> **Importante:**  
> - Todo debe quedar en **UTF-8 sin BOM**.  
> - No alterar la estructura de carpetas.  
> - Los nombres de archivo deben ser **idénticos al slug**, sin mayúsculas, tildes ni espacios.

## 1. Categorías disponibles

El sistema utiliza las siguientes categorías:

- campings
- ferias
- hospedajes
- pisqueras
- plazas
- restaurantes
- rios
- servicios
- universidad

## 2. Slug del POI

El **slug** es el identificador único del POI.  
Ejemplo: `restaurantea`, `campinga`, `rioa`.

Reglas:
- Solo letras minúsculas.
- Sin espacios ni acentos.
- Debe coincidir exactamente en datos, rutas e imágenes.

## 3. Archivos a modificar o crear

Supongamos que agregas `restaurantee`.

### 3.1. `_index.txt`

Ruta:
```
www/datos/restaurantes/_index.txt
```

Agregar una línea:
```
restaurantee
```

### 3.2. `nombres.txt`

Ruta:
```
www/datos/restaurantes/nombres.txt
```

Formato:
```
restaurantee|Restaurante Costa Elquina de Coquimbo
```

### 3.3. Datos del POI

Archivo:
```
www/datos/restaurantes/restaurantee.txt
```

Ejemplo:
```
descripcion=Restaurante Costa Elquina de Coquimbo ofrece pescados y mariscos típicos de la región.
tpie=15 min
tveh=5 min
apertura=12:00
cierre=23:00
alertas=Recomendable reservar fines de semana.
```

### 3.4. Rutas del POI

Archivo:
```
www/rutas/restaurantes/indicacionesrestauranteeruta.txt
```

Ejemplo:
```
Inicio en la plaza principal de Coquimbo.
Toma la avenida costera hacia el norte.
Continúa recto siguiendo la señalética turística.
Encontrarás el restaurante a mano derecha.
```

### 3.5. Imágenes

Debes crear:

```
restaurantee.jpg
restaurantee-640.jpg
restaurantee-1280.jpg
rutarestaurantee.jpg
rutarestaurantee-640.jpg
rutarestaurantee-1280.jpg
```

## 4. Versiones GZ (para ESP32)

Cada archivo nuevo/modificado debe comprimirse:

Ejemplo:
```
gzip -kf datos/restaurantes/restaurantee.txt
gzip -kf rutas/restaurantes/indicacionesrestauranteeruta.txt
gzip -kf img/restaurantes/restaurantee.jpg
```

## 5. Testeo del POI

### 5.1. Test local
Para hacer un testeo correctamente se debe abrir un servidor en local para que el frontend pueda leer los datos, aquí un ejemplo con python:

```
cd www
python -m http.server 8080
```
Probar:
```
http://localhost:8080/visitor/index.html
```

### 5.2. Test en el ESP32
- Subir carpeta `www`.
- Conectarse al portal cautivo.
- Validar datos, imágenes y rutas.

## 6. Checklist

- [x] Slug en `_index.txt`
- [x] Nombre en `nombres.txt`
- [x] Archivo `<slug>.txt`
- [x] Archivo `indicaciones<slug>ruta.txt`
- [x] Imágenes
- [x] GZ generados
- [x] Pruebas locales
- [x] Pruebas en ESP32


