# 05 — Reglas y núcleo

## Núcleo e invariantes

- Un slug/categoría debe resolver a una ficha y sus recursos.
- Agregar categoría al JSON no garantiza un botón nuevo si los HTML lo declaran de forma fija.
- El modo demo debe impedir que un mensaje simulado se interprete como impresión real.
- La falta de PDF o mensajería en la demo se comunica, no se sustituye por una petición fallida al equipo privado.
- Los archivos comprimidos son artefactos derivados; sus fuentes sin comprimir deben permitir reproducir el montaje.

### Entradas, decisión y efectos

El recorrido de [03-flujo-de-usuario.md](03-flujo-de-usuario.md) proporciona entradas al núcleo. Las reglas anteriores determinan lo aceptado y sus efectos; UI y proveedores externos no deben sustituir silenciosamente esas decisiones. El modelo de [04-base-de-datos.md](04-base-de-datos.md) identifica los estados/referencias afectados.

Los documentos especializados enlazados detallan las fórmulas, parámetros y efectos de cada operación.

### Pruebas con propósito

Para comprobar el núcleo, cubre una operación válida, una entrada rechazada y la reapertura o repetición de la operación. Los comandos de prueba están en [instalación y despliegue](09-instalacion-y-despliegue.md).

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
