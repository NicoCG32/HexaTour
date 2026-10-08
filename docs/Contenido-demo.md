# Contenido de la demo

[Índice técnico](README.md) · [Ejecutar la demo](Demo.md) · [Editar las fichas](Formato-de-datos.md)

## Alcance de los datos

El catálogo contiene nueve categorías y 27 fichas de prototipo. Se muestran como **datos de ejemplo**: horarios, tiempos de traslado, alertas e indicaciones no están verificados para orientar un viaje ni atender urgencias. El aviso de demo hace visible este alcance en todas sus páginas.

Las fichas actuales no registran fuentes ni fechas de verificación. Sus rutas textuales usan instrucciones genéricas y puntos de partida diferentes; no deben interpretarse como navegación calculada desde el equipo o la ubicación del visitante. Servicios contiene dos fichas con el nombre Posta Rural Monte Patria: en demo los botones las distinguen como ejemplos 1 y 3, conservando sus archivos y datos originales.

Para convertir una ficha en información operativa, registrar una fuente identificable y fecha de revisión de nombre/ubicación, horarios, tiempos, alertas e indicaciones; contrastar también su imagen de ruta. Modificar la ficha y su lista de categoría conjuntamente cuando corresponda. La coherencia de archivos no demuestra exactitud turística.

## Recursos gráficos

El responsable del proyecto declaró el **2026-10-07** que las fotografías, mapas e iconos de [web/www/img](../web/www/img) son propios del proyecto. La revisión técnica cuenta 221 archivos gráficos, incluidos originales, variantes, logos y mapa general; todos se decodificaron correctamente. Las 162 referencias gráficas de las fichas apuntan a archivos presentes.

Este registro se basa en esa declaración de procedencia. No define una licencia general para redistribuir el proyecto ni sustituye las licencias de componentes de terceros. Si se incorporan recursos ajenos, registrar autor, origen, permiso/licencia y atribución junto a su ruta antes de incluirlos en la demo.

## SMS y acciones

El portal ya no contiene un destinatario SMS de prueba. La configuración local `URGENCIA_SMS` de [visitor-lugar.js](../web/www/assets/js/visitor-lugar.js) tiene teléfono y punto vacíos. Sin ambos valores válidos, muestra **SMS no configurado** y no abre ninguna aplicación.

En demo, la urgencia siempre produce un mensaje local, incluso si existe una configuración local. La impresión también es simulada y el PDF aparece explícitamente no disponible. La configuración de un montaje no debe incorporarse al artefacto público.

## Preparación de publicación

El contenido es presentable como demostración de prototipo, con el aviso de ejemplos visible. Antes de publicar, el empaquetado debe activar demo en **todas** las entradas HTML, incluso con enlaces directos o sin `demo=1`; comprobar sólo la landing no basta. La distribución debe contener únicamente la raíz web revisada, sin configuración SMS local, firmware, herramientas ni informes.

El [empaquetador y workflow manual de Pages](Despliegue.md) están preparados: la copia generada fuerza demo y conserva SMS vacío. La publicación aún no se ha ejecutado. Servir directamente el checkout mantiene el modo habitual en URLs sin `demo=1`. La [guía de demo](Demo.md) describe el recorrido local y sus límites.
