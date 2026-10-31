# 07 — Diseño y accesibilidad

## Identidad y experiencia de uso

Portal de lectura simple con identidad turística y distinción de visitante/operador. Los estados de acción disponible, simulada o deshabilitada deben ser inequívocos. La usabilidad en un teléfono del visitante es parte del producto, no sólo de la presentación académica.

### Criterios verificables

- Estados vacíos, carga, confirmación y error distinguibles por texto además de color.
- Orden de foco, teclado y nombres accesibles cuando la plataforma los utilice.
- Legibilidad y controles suficientes para el dispositivo objetivo; considerar área segura y ciclo de vida en móvil.
- Evitar que animación, espera o respuesta tardía apliquen efectos ajenos a la selección vigente.

Comprueba estos criterios en los recorridos principales y en los tamaños de pantalla de la plataforma que vas a utilizar.

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).

## Recursos de identidad y distribución

[Catálogo de originales y variantes](../branding/README.md) · [Manifest de identidad](../branding/manifest.json).

El portal mantiene el isotipo cuadrado en el espacio reservado al logo y añade favicon/Apple Touch a sus páginas. Las rutas relativas funcionan en SD, mock y demo; no cambian las categorías ni sus pictogramas.

Los banners de presentación se seleccionan por tema en el README. Las aplicaciones incorporan sólo los recursos necesarios, con dimensiones/proporción estables; las variantes y originales permanecen en branding. La identidad visual no amplía funcionalidades ni cambia las condiciones de uso.
