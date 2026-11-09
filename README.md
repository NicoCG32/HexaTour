<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="branding/banners/hexatour-banner-oscuro.webp">
    <img src="branding/banners/hexatour-banner-claro.webp" alt="HexaTour, orientación turística local" width="100%">
  </picture>

# HexaTour

**Orientación turística donde la conexión no llega.**

[![Estado](https://img.shields.io/badge/Estado-Prototipo_académico-266A85?style=flat-square)](docs/02-funcionalidades.md) [![Plataformas](https://img.shields.io/badge/ESP32--S3_%7C_Arduino_UNO-196F71?style=flat-square)](docs/01-arquitectura-general.md) [![Licencia](https://img.shields.io/badge/Código-MIT-7C6850?style=flat-square)](LICENSING.md)

[![ESP32 S3](https://img.shields.io/badge/ESP32%20S3-B42B2B?style=for-the-badge&logo=espressif&logoColor=FFFFFF)](#tecnologías) [![Arduino](https://img.shields.io/badge/Arduino-007D85?style=for-the-badge&logo=arduino&logoColor=FFFFFF)](#tecnologías) [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=20232A)](#tecnologías) [![Python 3](https://img.shields.io/badge/Python%203-3776AB?style=for-the-badge&logo=python&logoColor=FFFFFF)](#tecnologías)

[**Explorar la demo**](https://nicocg32.github.io/HexaTour/) · [**Documentación**](docs/README.md) · [**Arquitectura**](docs/01-arquitectura-general.md) · [**Costos y viabilidad**](docs/18-analisis-economico-clp-usd.md) · [**Montaje**](firmware/README.md)
</div>

---

## Resumen ejecutivo

HexaTour es un prototipo de orientación turística rural que permite consultar lugares e indicaciones sin Internet. Un ESP32-S3 sirve el portal y el contenido desde una tarjeta SD; un Arduino UNO controla la impresión térmica. El repositorio incluye el firmware, el portal, diagramas y herramientas para reproducirlo. La demo web permite explorar la experiencia sin hardware con datos de ejemplo.

## Estado real del proyecto

| Nivel | Qué significa en esta versión |
| --- | --- |
| ✅ **Implementado** | Firmware ESP32-S3/Arduino UNO, portal de información y contenido en SD; hay simulador local y [demo estática](https://nicocg32.github.io/HexaTour/) para explorar la experiencia sin hardware. |
| 🧪 **En validación** | El montaje físico integrado, impresión real, comportamiento del portal cautivo en distintos teléfonos y seguridad de los endpoints requieren pruebas reproducibles. |
| 🧭 **Posible evolución** | Instalación en otros recintos, actualización de contenidos locales y operación sostenida, sujetas a validación con responsables del lugar. |

<details>
<summary><strong>Cómo leer este estado</strong></summary>

Una función **implementada** existe en el código o en los artefactos del proyecto, pero eso no acredita automáticamente todas sus pruebas. «En validación» identifica capacidades todavía sujetas a comprobaciones; «pendiente» no es una promesa de entrega. El alcance se contrasta con el código, los informes originales y las releases de cada versión.

</details>

## Sobre el proyecto

HexaTour surgió en 2025, durante **Proyecto Diseño e Innovación** de la Universidad Católica del Norte. El equipo **HexaCorp** investigó las dificultades de orientación en sectores rurales de la Región de Coquimbo y propuso un punto de información local con indicaciones en pantalla y papel. El [contexto formativo](docs/academica/README.md) reúne al equipo y sus entregas.

## Qué hace hoy

| Modalidad | Funciones |
| --- | --- |
| **Montaje local** | Portal Wi-Fi y fichas desde SD, generación de PDF en ESP32-S3 e impresión mediante Arduino UNO y ticketera. |
| **Simulador Python** | Portal desde un PC, aceptación de impresión simulada y PDF de prueba. |
| **Demo web** | Catálogo de ejemplo, impresión simulada, PDF deshabilitado y avisos de urgencia locales. |

Las indicaciones están redactadas previamente. El catálogo actual contiene datos de ejemplo y la opción de urgencia no presta asistencia. Consulta el [alcance de cada modalidad](docs/02-funcionalidades.md) y las [pruebas pendientes del montaje](firmware/Compilacion.md#montaje-original-y-revalidación).

## Conveniencia y posible rentabilidad

La idea tiene una fortaleza concreta: **servir fichas, fotografías e indicaciones desde una SD por una red Wi-Fi local**, sin exigir Internet al visitante ni un servicio de nube para el catálogo. La posibilidad de imprimir instrucciones añade una alternativa tangible, aunque también requiere energía, papel y mantenimiento.

Para un recinto turístico, **la conveniencia aún debe demostrarse** midiendo tareas completadas, información correcta, fallos y tiempo útil de atención. Para quien lo comercialice, **la rentabilidad requiere medir el costo de fabricar, instalar, actualizar y mantener** el punto. Tener firmware propio con licencia MIT no elimina la factura de la pantalla, la estructura, la ticketera ni el soporte.

**Para la maqueta física presentada en el curso se utilizó una tableta personal de Pablo Guzmán, prestada temporalmente sin compra para HexaCorp**, que abría el portal local como usuario de operador/administración; los demás componentes principales fueron ESP32-S3, Arduino UNO, LCD, protoboard/cables, lector y tarjeta SD, e impresora térmica TTL. La **impresora costó aproximadamente $23.000 CLP** y **madera/pintura no superaron $60.000** según el responsable técnico. **Benjamín Esquivel y su padre aportaron la carpintería del tótem sin cobrar**, reduciendo el gasto de caja sin eliminar su valor económico. Una [estimación de reposición de componentes a precios 2026](docs/academica/03-costeo-maqueta-fisica.md) suma **$192.350–$261.350 antes de madera/pintura**, y llega **hasta $321.350 para esa canasta parcial** usando el tope de materiales, **sin incluir carpintería ni otras partidas pendientes**. Una sensibilidad separada valora la mano de obra sin fingir que se facturó o que conocemos las horas trabajadas. No es el costo histórico exacto ni el precio de un producto comercial.

El **informe final original de 2025** estima cuatro configuraciones: **interior con botonera $239.000–$471.000**, **interior táctil $380.000–$850.000**, **exterior con botonera $1.921.000–$3.963.000** y **exterior táctil $2.655.000–$5.831.000** (CLP, **costos preliminares, no precios de venta ni facturas**). Incluye además hipótesis de consumo eléctrico, rollos de papel y mantenimiento que ahora están contrastadas en el [estudio económico ampliado](docs/18-analisis-economico-clp-usd.md). **No existe rentabilidad comercial demostrada**: faltan costos completos reales, cotizaciones actualizadas, demanda, pruebas integradas y operación observada.

La [investigación de mercado](docs/19-mercado-y-validacion-comercial.md) relaciona el problema con el estudio de HexaCorp y fuentes territoriales externas, sin convertir turistas en compradores. Sus casos de retorno y equilibrio son **simulaciones expresamente identificadas**, no utilidades observadas. [Lectura crítica del informe original](docs/academica/02-lectura-critica-de-los-informes.md).

**Prioridad para justificar una instalación:** [revalidación física, seguridad y piloto supervisado](docs/20-validacion-operativa-y-pilotos.md). Las fichas actuales contienen ejemplos, el botón de urgencia no presta rescate y el montaje con los binarios compilados en 2026 no tiene una validación física integral acreditada.

## Tecnologías

- **Hardware y firmware:** ESP32-S3 y Arduino UNO, programados en Arduino/C++; módulo SD, LCD I²C, UART y ticketera térmica.
- **Interfaz:** HTML, CSS y JavaScript sin framework; páginas de visitante y operador.
- **Contenido:** catálogo de archivos JSON e imágenes, servido localmente desde la SD.
- **Herramientas:** Python para probar las APIs, validar el catálogo y generar el artefacto estático de demostración.

En [arquitectura por niveles](docs/01-arquitectura-general.md) están el contexto, los componentes, el despliegue y los diagramas de comunicación entre placas. El [modelo de datos](docs/04-base-de-datos.md) y los [estados de impresión](docs/03-flujo-de-usuario.md) tienen sus propios diagramas.

## Usar o descargar

[Abrir la demo](https://nicocg32.github.io/HexaTour/) · [Recorrido sin hardware](docs/Demo.md) · [Montaje y compilación](firmware/Compilacion.md).

## Ejecutar desde el código

Desde la raíz del repositorio, con Python 3.10 o superior:

```bash
python tools/backend-local/server.py --root web/www --port 8000
```

Abre [visitante](http://localhost:8000/visitor/) u [operador](http://localhost:8000/main/). El simulador está pensado para pruebas locales y sirve ambas vistas sin autenticación. [Guía del backend local](tools/backend-local/README.md).

Para comprobar el catálogo y las herramientas:

```bash
python -m unittest discover -s test -p 'test_*.py'
```

Para preparar las placas, sigue la [guía de compilación](firmware/Compilacion.md).

## Documentación para cada lector

| Área | Lectura recomendada |
| --- | --- |
| **General** | [Problema y propuesta](docs/00-problematica-cliente-y-valor.md) · [Estado funcional](docs/02-funcionalidades.md) |
| **Técnica** | [Arquitectura](docs/01-arquitectura-general.md) · [Flujos y estados](docs/03-flujo-de-usuario.md) · [JSON y dominio](docs/04-base-de-datos.md) |
| **Desarrollo** | [Proceso](docs/17-desarrollo-y-metodologia.md) · [Costos](docs/18-analisis-economico-clp-usd.md) · [Mercado](docs/19-mercado-y-validacion-comercial.md) · [Pilotos](docs/20-validacion-operativa-y-pilotos.md) |
| **Académica** | [Equipo, curso e informes originales](docs/academica/README.md) · [Trazabilidad de evidencias](docs/academica/02-lectura-critica-de-los-informes.md) |

[**Índice completo**](docs/README.md) · [**Manual técnico del proveedor**](docs/manual-proveedor.md) · [**Recursos gráficos**](branding/README.md)

## Autoría y licencia

**Pablo Guzmán** desarrolló el circuito, el firmware de ambas placas, el portal web y la integración. **Benjamín Esquivel y su padre** construyeron la maqueta de presentación. Los demás integrantes de **HexaCorp** colaboraron principalmente en investigación, informes y presentaciones. [Equipo y aportes](docs/academica/README.md).

Código propio bajo [MIT](LICENSE). [Créditos, terceros y condiciones de reutilización](LICENSING.md).
