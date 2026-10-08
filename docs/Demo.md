# Demo sin hardware

[Índice técnico](README.md) · [Arquitectura](Arquitectura.md) · [Modo con mock](../tools/backend-local/README.md)

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

La navegación deriva la raíz web de la ubicación del script compartido. Se comprobó una entrada en raíz y otra bajo `/HexaTour/` en un servidor estático temporal: la landing, los enlaces de vista, las fichas y las imágenes conservan su base.

Al servir el checkout `web/www`, la demo se activa por URL. La [copia pública generada](Despliegue.md#generar-y-revisar-localmente) inserta `hexatour-mode=demo` en las cinco entradas: `common.js` fuerza demo incluso sin parámetro o con `demo=0`. Conserva SMS vacío y excluye firmware, herramientas e informes. El workflow de Pages está preparado con ejecución manual; aún no hay hosting público validado.

## Comprobación realizada

La revisión local del 2026-10-07 cubrió las 27 fichas en ambas vistas y bases (108 recorridos), campos contrastados con sus JSON, imágenes principales y rutas decodificadas, 54 impresiones simuladas y PDF deshabilitado. Se probaron las tres urgencias en ambas vistas/bases y el estado SMS no configurado en visitante habitual. Ningún recorrido pidió `/api/*` ni abrió SMS.

Los menús y una ficha representativa de cada vista/base se comprobaron a 320, 390 y 1280 píxeles sin desbordamiento horizontal. Categoría, ficha, Ruta, Simular impresión, Volver y cambio de vista se activaron con Enter; Tab entre enlaces de vista mostró foco visible. Esto comprueba anchos de navegador, no dispositivos móviles físicos ni una auditoría completa de accesibilidad.

Los 273 archivos estáticos sin `.gz` respondieron correctamente desde ambas bases (546 solicitudes de recursos). La prueba no registró errores de consola ni respuestas HTTP de error. El smoke de la API mock había pasado 3/3; sus componentes no cambiaron en esta revisión.

Esto no valida impresión física, SMS con destinatario configurado, compilación del firmware, exactitud turística ni un hosting público. La procedencia gráfica declarada por el responsable está registrada en [Contenido de la demo](Contenido-demo.md#recursos-gráficos); no fue una comprobación independiente de titularidad. El empaquetado y recorrido público siguen pendientes.
