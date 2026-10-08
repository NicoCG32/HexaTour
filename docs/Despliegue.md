# Distribuir la demo estática

[Índice técnico](README.md) · [Recorrido de demo](Demo.md) · [Contenido mostrado](Contenido-demo.md)

## Estado

El empaquetado local y el workflow manual de GitHub Pages están preparados. **No hay una publicación ni una URL pública verificada.** La inspección del repositorio el 2026-10-07 indica Pages sin configurar; el workflow todavía debe incorporarse a la rama remota para ejecutarse allí.

El montaje físico usa `web/www` en la SD y conserva sus acciones habituales. La distribución pública usa una copia generada con demo forzada. Un despliegue web no actualiza firmware ni SD.

## Generar y revisar localmente

Desde la raíz del repositorio, con Python 3.10 o posterior y sin instalar paquetes:

```bash
python -m unittest discover -s test -p "test_*.py"
python tools/build_demo.py
python test/validate_data.py --root dist/demo
python -m http.server 8000 --bind 127.0.0.1 --directory dist/demo
```

Abre http://localhost:8000/ y las entradas `/visitor/`, `/main/`, `/visitor/lugar.html?cat=Universidad` y `/main/lugar.html?cat=Universidad`. El aviso Demo sin hardware debe aparecer sin `demo=1`. Prueba también `demo=0`: el artefacto mantiene impresión simulada, PDF no disponible y urgencias sin envío.

[build_demo.py](../tools/build_demo.py) genera `dist/demo`, una carpeta ignorada por Git. Si ya existe, elige otra salida, por ejemplo `python tools/build_demo.py --output dist/demo-revision`; sustituye esa ruta en los comandos de validación y servidor. El script rechaza salidas superpuestas al portal fuente o ya existentes. No modifica `web/www`.

## Qué contiene el artefacto

| Contenido | Tratamiento |
| --- | --- |
| Cinco entradas HTML | Marca `hexatour-mode=demo` insertada; `common.js` la respeta antes del parámetro de URL |
| Seis scripts y cuatro estilos del portal | Copia de una lista explícita de assets |
| JSON de categorías/fichas e imágenes | Catálogo validado, recursos originales; `.gz` opcionales excluidos |
| Configuración SMS | `URGENCIA_SMS` se sustituye por teléfono/punto vacíos sólo en la copia; una declaración no reconocida hace fallar el empaquetado |
| `.nojekyll` | Marcador estático vacío |
| `demo-manifest.json` | Modo, entradas, resumen de catálogo, huella del conjunto fuente seleccionado y hashes SHA-256 de los archivos generados; el propio manifiesto no incluye su hash |

La raíz actual tiene 275 archivos. Se comprueban también scripts, estilos e imágenes referenciados por el HTML. Una nueva entrada HTML o asset debe incorporarse al contrato del empaquetador y comprobarse antes de distribuirlo. Herramientas, pruebas, firmware, documentación, informes, archivos ocultos locales y scripts ajenos a la lista no forman parte del artefacto.

## Workflow de Pages

[pages.yml](../.github/workflows/pages.yml) sólo admite **workflow_dispatch**, sin disparadores push/PR. Su opción `publish` es falsa por defecto:

1. `build` usa Python 3.12, ejecuta las regresiones y genera `dist/demo`. Sube exclusivamente esa carpeta como artefacto `github-pages`, con retención de un día.
2. `deploy` sólo corre si `publish=true` y la rama es `main`. Depende del build aprobado, usa el entorno `github-pages` y expone la URL real como `page_url`.

El permiso global es `contents: read`; `pages: write` e `id-token: write` se conceden sólo al job de publicación. Las acciones oficiales son checkout v6, setup-python v6, upload-pages-artifact v4, configure-pages v5 y deploy-pages v4. [Contrato oficial de workflows Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Activar y publicar

Cuando los cambios revisados estén confirmados y disponibles en `main` remoto:

1. El responsable del repositorio configura **Settings → Pages → Source → GitHub Actions**. El workflow usa `enablement=false` y no activa Pages automáticamente. [Fuente de publicación de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
2. Ejecuta **Actions → Demo estática de HexaTour → Run workflow**, rama `main`, dejando `publish` desmarcado para revisar el build y sus resultados.
3. Tras revisar, ejecuta nuevamente en `main` con `publish` marcado. Las reglas del entorno `github-pages`, si existen, siguen aplicándose.
4. Obtén la URL del job `deploy` y comprueba landing → categoría → ficha → ruta → acción demo, accesos directos sin parámetro, urgencias, teclado y ancho móvil. Ninguna acción debe pedir `/api/*` ni abrir SMS. La validación local bajo `/HexaTour/` no sustituye esta comprobación HTTPS pública.

## Registro y recuperación

Registrar commit publicado, ID de ejecución, URL real, fecha y huella del manifiesto después de comprobar el sitio. La huella de archivos identifica el contenido de una copia; un HEAD anterior no representa cambios locales aún sin confirmar.

Para recuperar una versión, restaurar en `main` el contenido de una fuente previamente verificada, reconstruir/revisar la demo y publicar mediante el mismo workflow. No depender del artefacto remoto como copia permanente: expira al día. Conservar fuente y manifiesto de la versión aprobada. La actualización de SD se realiza por el [procedimiento del montaje](manual-proveedor.md#actualizacion-de-contenidos), independientemente de Pages.
