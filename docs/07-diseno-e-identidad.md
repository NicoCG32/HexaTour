# 07 · Interfaz, identidad y accesibilidad

La interfaz intenta ser sencilla: elegir una categoría, identificar un lugar y consultar sus indicaciones. Hay dos recorridos diferenciados, **visitante** y **operador**, que comparten el catálogo pero no las mismas acciones.

## Decisiones visibles

- Las páginas están realizadas en HTML, CSS y JavaScript, sin framework de interfaz ni servicio de fuentes externo requerido para el funcionamiento local.
- Los botones y fichas mantienen una estructura reconocible en ambas vistas.
- La demo debe llevar un **aviso persistente** que la distinga del montaje físico, con mensajes claros para impresión simulada, PDF deshabilitado y urgencias no enviadas.
- El diseño utiliza los recursos incluidos en [`branding/`](../branding/README.md), con banners para tema claro/oscuro, logos, isotipo e iconos. La presentación principal selecciona el banner con `<picture>`.

## Criterios de revisión

Antes de presentar el prototipo, comprueba la navegación por teclado, el orden de foco, el contraste, la lectura desde teléfono, los mensajes de error y el comportamiento cuando falta una ficha o imagen.

Para modificar los archivos, consulta la [guía web](../web/README.md), los [estilos del portal](../web/www/assets/css/base.css) y el [catálogo de marca](../branding/README.md).
