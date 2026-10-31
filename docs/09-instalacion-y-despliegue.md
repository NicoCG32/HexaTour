# 09 — Puesta en marcha y distribución

## Puesta en marcha y distribución por plataforma

**Disponibilidad:** Prototipo de orientación turística con portal local, firmware y demo web. La demo permite recorrer la interfaz sin hardware y simula o deshabilita las acciones físicas.

**Destinos:** Montaje ESP32/UNO + Demo web estática.

Montaje/portal con toolchains propios; seguir las versiones y rutas de las guías específicas.

Los comandos de backend, firmware y simulación se describen en las guías relacionadas. Elige la modalidad que corresponda a tu montaje o entorno de demostración.

### Secuencia de puesta en marcha

1. Preparar el runtime/editor y la configuración que indiquen las fuentes enlazadas; usar valores de prueba y restaurar el lockfile apropiado.
2. Ejecutar la modalidad local y sus comprobaciones existentes desde la carpeta indicada por esa guía. No confundir preview web con el runtime nativo o montaje físico.
3. Construir/instalar el artefacto de ese target y comprobar recorrido principal, error relevante y reapertura/actualización antes de declararlo entregado.

Ejecuta los comandos de comprobación antes de distribuir una compilación. Puedes consultar sus resultados remotos en la pestaña Actions del repositorio.

### Datos, servicios y distribución

Archivos JSON e imágenes en SD bajo /www; no hay base SQL ni RLS. Los conteos/listas y las fichas deben ser coherentes. El mock usa las fuentes del sitio; una simulación no certifica DNS cautivo, autenticación del operador ni ejecución serial real.

La demo de Pages contiene una copia estática del portal. El montaje local utiliza su propia tarjeta SD y los firmwares de ESP32 y UNO; actualiza cada componente siguiendo la guía correspondiente.

GitHub Releases distribuye los archivos de cada versión. Los servicios de servidor se despliegan por separado; consulta la guía de la plataforma para instalar o alojar la aplicación.

### Recuperación

Conservar el artefacto anterior y su procedencia. Retroceder código no revierte automáticamente datos o migraciones. Revisar compatibilidad de guardado/snapshot y restauración antes de instalar una versión antigua. Consulta las notas de la versión para conocer los requisitos y límites de la entrega.

## Código y documentación relacionada

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
