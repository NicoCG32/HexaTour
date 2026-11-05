# Demo sin hardware

[Índice técnico](README.md) · [Arquitectura](Arquitectura.md) · [Modo con mock](../tools/backend-local/README.md)

La [demo pública en Pages](https://nicocg32.github.io/HexaTour/) activa el modo demo en todas sus entradas. También puedes probar el portal localmente.

## Ejecutar y activar

Desde la raíz del repositorio, con Python 3.10 o posterior:

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory web/www
```

Abre http://localhost:8000/?demo=1. La landing conduce a la vista visitante. También puedes entrar directamente a http://localhost:8000/visitor/?demo=1 o http://localhost:8000/main/?demo=1.

El aviso **Demo sin hardware** confirma el modo activo. El parámetro `demo=1` se conserva al elegir categorías, pulsar Volver y cambiar entre Visitante/Operador desde los enlaces del aviso. No hay persistencia en el navegador: una URL sin ese parámetro abre el modo habitual. El servidor de este comando sirve archivos estáticos y no implementa las APIs físicas.

## Recorrido

1. Elegir una categoría y un lugar para ver campos e imagen principal.
2. Pulsar Ruta para cargar su imagen de indicaciones.
3. En Operador, pulsar **Simular impresión**: aparece un mensaje local y no se envía trabajo a una API o ticketera.
4. En Visitante, el botón **PDF no disponible en demo** está deshabilitado. La imagen de ruta sigue disponible; la descarga PDF habitual requiere ESP32 o mock.
5. En Urgencia de cualquiera de las vistas, seleccionar un servicio muestra una demostración local. No abre SMS ni realiza llamadas/envíos.

Los controles funcionan por teclado y los resultados locales tienen estado accesible. Las fichas se presentan como ejemplos sin verificación de indicaciones, horarios y tiempos; el aviso visible aclara que no deben usarse para orientación ni atención de urgencias. [Alcance y procedencia del contenido](Contenido-demo.md).

## Modo habitual

Sin `demo=1`, se conservan las solicitudes de impresión y PDF al servidor. El operador muestra un aviso local de urgencia con texto que explica que no hay llamada ni envío. El visitante muestra SMS no configurado mientras teléfono y punto estén vacíos; sólo con configuración local válida puede abrir la app después de confirmar. [Configuración SMS](../web/README.md#urgencias).

No usar el servidor estático del primer comando para comprobar esas APIs. Para hacerlo, utiliza el [backend mock](../tools/backend-local/README.md); para impresión real y portal cautivo, utiliza el montaje.

## Rutas y publicación

La navegación deriva la raíz web de la ubicación del script compartido. Las páginas, fichas e imágenes conservan la base del sitio, tanto en raíz como bajo `/HexaTour/`.

Al servir el checkout `web/www`, la demo se activa por URL. La [copia pública generada](Despliegue.md#generar-y-revisar-localmente) inserta `hexatour-mode=demo` en las cinco entradas: `common.js` fuerza demo incluso sin parámetro o con `demo=0`. Conserva SMS vacío y excluye firmware, herramientas e informes. Pages publica esa copia mediante el [workflow manual](Despliegue.md#workflow-de-pages).
