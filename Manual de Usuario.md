# Manual de Usuario – HexaTour

Este manual explica cómo utilizar el tótem HexaTour en modo visitante y operador. El sistema funciona sin Internet y entrega orientación turística mediante un portal cautivo y tickets impresos.

## Hardware del prototipo
- Tableta (monitor principal)
- ESP32‑S3
- Arduino UNO
- Impresora térmica con TTL
- Pantalla LCD 2x16 (I2C)
- Módulo SD
- Tarjeta SD

## Conexiones y alimentación (resumen)
- La impresora térmica debe usar **su propia fuente** según lo indicado por el fabricante. En este prototipo se utilizó un transformador de 9V independiente.
- **No** alimentar la impresora desde el ESP32 ni desde el UNO.
- Unificar **tierra (GND)** entre todos los módulos para que la comunicación serial funcione correctamente.
- Usar **divisores de voltaje o resistencias** en las líneas de comunicación para proteger niveles de 3,3V (ESP32‑S3) frente a 5V (UNO) y 9V (impresora).
- Verificar polaridad y tensiones antes de energizar para evitar daños.

## Pines utilizados
Para el detalle de pines y conexiones exactas del firmware, ver la sección “Pines usados” en [Backend (UNO y ESP32)/README.md](Backend%20(UNO%20y%20ESP32)/README.md).

## 1. Requisitos previos
- El tótem debe estar encendido.
- La tarjeta SD debe estar insertada y con la carpeta www cargada.
- La impresora térmica debe tener papel.

## 2. Modo operador (administración)
El modo operador permite revisar la interfaz interna y el contenido.

1. Conéctate al Wi‑Fi HexaTour.
2. Abre el navegador y visita http://192.168.4.1/main/.
3. Ingresa las credenciales:
	- Usuario: operator
	- Contraseña: HexaTour2025!

## 3. Impresión de indicaciones (Sólo para el modo operador)
1. Dentro de un POI, presiona “Imprimir indicaciones”.
2. Espera a que la impresora genere el ticket.
3. Retira el ticket y sigue los pasos indicados.

Si la impresora está ocupada, el sistema mostrará “Impresora ocupada”. Espera unos segundos e intenta de nuevo.

## 4. Acceso al portal cautivo (visitante)
1. Enciende el tótem y espera la pantalla “Listo para usar”.
2. En tu celular, busca la red Wi‑Fi: HexaTour.
3. Conéctate usando la contraseña: hexatour123.
4. El portal se abrirá automáticamente. Si no aparece, abre el navegador y visita http://192.168.4.1/visitor/.

## 5. Navegación básica (visitante)
1. En la pantalla principal elige una categoría (por ejemplo: restaurantes, campings, ríos).
2. Selecciona un punto de interés (POI).
3. Revisa la información del lugar (descripción, tiempos, horarios, alertas).
4. Opcional: imprime la ruta con el botón de impresión.

## 6. Descarga de PDF (ruta ampliada)
1. En la vista del POI, selecciona la opción “Ver/Descargar ruta”.
2. El sistema abrirá un PDF con indicaciones y, si existe, la imagen de ruta.
3. Puedes guardar el PDF en el teléfono para consultarlo sin conexión.

## 7. Actualizacion de contenidos
Para editar, agregar o corregir datos de lugares, usa la base JSON en /www/db y sigue la guia en [Frontend (Interfaz)/README.md](Frontend%20(Interfaz)/README.md).

## 8. Recomendaciones de uso
- Evita retirar la SD con el equipo encendido.
- Mantén la impresora con papel térmico y sin obstrucciones.
- Actualiza el contenido de POI según la guía en [Frontend (Interfaz)/README.md](Frontend%20(Interfaz)/README.md).

## 9. Solución rápida de problemas
- No aparece el portal cautivo: abre el navegador y escribe http://192.168.4.1/visitor/.
- “Error SD”: verificar formato FAT32 y estructura /www en la tarjeta.
- No imprime: revisar que la impresora tenga papel y esté encendida.
- Si el portal se siente lento: limpiar cache del navegador y verificar que la SD tenga los archivos .gz en /www/db y /www/img.
- Si el PDF no muestra logo: verifica que exista /www/img/map/logo.jpg.

## 9.1 Errores comunes (clave y solucion)

- Clave: PORTAL_NO_ABRE
	Solucion: conecta al Wi-Fi HexaTour y abre http://192.168.4.1/visitor/ manualmente.
- Clave: ERROR_SD
	Solucion: verifica FAT32, carpeta /www en la SD y vuelve a insertar la tarjeta.
- Clave: DATOS_NO_CARGAN
	Solucion: confirma que /www/db contiene index.json, categories/ y poi/; limpia cache.
- Clave: IMAGEN_FALTANTE
	Solucion: revisa que existan los archivos en /www/img/<categoria>/ y sus .gz.
- Clave: PDF_SIN_LOGO
	Solucion: asegura /www/img/map/logo.jpg y su .gz.
- Clave: NO_IMPRIME
	Solucion: revisa papel, encendido de impresora y conexion serial con el UNO.

## 10. Alcance
Este manual cubre la operación del prototipo con ESP32 + Arduino UNO.
Funcionalidades proyectadas (NFC, voz, multilenguaje) pueden no estar disponibles en esta versión.
