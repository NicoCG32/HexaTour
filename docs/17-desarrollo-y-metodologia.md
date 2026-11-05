# 17 · Cómo desarrollé HexaTour y cómo continuar

## El proyecto académico y el reparto del trabajo

HexaTour nació en **Proyecto Diseño e Innovación** como propuesta del equipo **HexaCorp**. A partir de investigación sobre la orientación turística en sectores rurales, el grupo comparó alternativas y propuso un tótem de información local con posibilidad de imprimir indicaciones.

Me encargué del desarrollo tecnológico: diseñé el circuito, escribí el firmware del ESP32-S3 y del Arduino UNO, desarrollé el portal web e integré las comunicaciones y periféricos.

Benjamín Esquivel y su padre construyeron la maqueta física. Los demás compañeros participaron principalmente en investigación, informes y presentaciones. El [contexto académico](academica/README.md) reúne los aportes y los roles del equipo.

## Desarrollo tecnológico y estado del repositorio

El código está organizado en portal, catálogo JSON, firmware de las dos placas, simulador Python, validador de datos y empaquetador de la demo. El circuito y las [guías de compilación](../firmware/Compilacion.md) permiten preparar el montaje con versiones fijadas.

Para continuar el desarrollo:

1. **Definir contenido y recorrido:** qué lugares se presentan y qué indicaciones puede recibir el visitante.
2. **Mantener consistencia:** categoría, slug, ficha, imágenes y botones deben concordar.
3. **Probar sin hardware:** ejecutar el simulador, revisar la navegación y correr las pruebas Python.
4. **Compilar cada placa:** construir ambos sketches y comprobar pines, bibliotecas, protocolo y límites.
5. **Volver al montaje físico:** contrastar UART, impresión, LCD, SD y portal cautivo con una versión concreta.
6. **Registrar resultados:** anotar versiones y resultados de las pruebas en el simulador y en el equipo.

## Trabajo pendiente

La siguiente etapa requiere repetir la prueba física con la base de compilación actual, revisar el acceso a las APIs y validar el contenido con responsables locales. Los criterios están en la [guía de puesta en marcha](09-instalacion-y-despliegue.md).

[Reglas del sistema](05-motor-o-nucleo-de-negocio.md) · [Verificación y montaje](09-instalacion-y-despliegue.md) · [Proyección](15-escalabilidad-y-nuevos-mercados.md)
