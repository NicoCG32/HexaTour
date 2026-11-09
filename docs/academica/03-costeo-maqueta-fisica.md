# 03 · Montaje real de la maqueta y costo referencial de reposición

[← Índice académico](README.md) · [Viabilidad y costos](../18-analisis-economico-clp-usd.md) · [Arquitectura](../01-arquitectura-general.md) · [Informe original 2025](../informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf)

> **Reconstrucción al 9 de noviembre de 2026.** Este capítulo incorpora información directa entregada por **Pablo Guzmán**, responsable técnico, acerca de lo que efectivamente se utilizó en la **maqueta universitaria**. Los precios de tiendas son **referencias de reposición en 2026**, NO importes que el grupo pagó en 2025. No se han suministrado facturas o modelos originales de tableta, Arduino y otros módulos.

## 1. Así funcionaba el montaje de la presentación

La **pantalla del tótem era una tableta convencional** que abría, en su navegador, el **portal local con usuario de administración/operador**. No era una pantalla táctil industrial específica, ni hay evidencia de un controlador de pantalla escrito para un modelo comercial concreto. **La tableta actuaba como cliente web**, no como servidor del catálogo. El **ESP32-S3** proporcionaba la red local/portal con contenido desde la tarjeta SD; el **Arduino UNO** se encargaba del firmware relacionado con la impresora TTL.

El montaje **utilizó** un ESP32-S3, Arduino UNO, pantalla LCD, protoboard y cables típicos de kits, módulo y tarjeta SD, impresora térmica TTL, tableta y una estructura de madera pintada. El **precio aproximado de adquisición de la impresora en AliExpress fue CLP $23.000**. **La madera más la pintura no superaron CLP $60.000**: no está identificado el gasto exacto dentro de ese límite.

El **montaje de la maqueta física** fue trabajo de **Benjamín Esquivel y su padre**; el diseño del circuito y la integración tecnológica se atribuyen a Pablo según la [documentación académica](README.md). Confirmar el uso de una tableta no cambia esos créditos.

~~~
Tableta convencional (navegador, vista operador)
          |
          | Wi-Fi local, HTTP
          v
ESP32-S3 (AP, portal y endpoints) <--> módulo y tarjeta SD
          |                         |
          +---- LCD I²C             +---- HTML, JS, JSON, imágenes
          |
          +---- UART ---- Arduino UNO ---- serial TTL ---- impresora
~~~

**Administración ≠ seguridad completa:** que la tableta usara una cuenta o acceso administrativo no significa que todas las APIs estuviesen correctamente protegidas. El firmware vigente documenta Basic Auth para /main/ pero no asegura de forma equivalente las operaciones físicas. [Fronteras de confianza](../01-arquitectura-general.md#fronteras-de-confianza-y-limitaciones).

## 2. BOM retrospectiva: lo usado frente a lo que costaría reponerlo

| Componente | Evidencia disponible | Referencia de compra o costo (CLP) |
| --- | --- | ---: |
| **Tableta Android de entrada, 8,7–10,1″ aprox.** | Uso comprobado por testimonio; marca, tamaño y precio exacto original desconocidos | **$129.990–$189.990** (tabletas económicas [Samsung Galaxy A11, ABC](https://www.abc.cl/); [Lenovo M10/Tab, Falabella](https://www.falabella.com/falabella-cl/shop/tablet-lenovo-m10)) |
| **Kit ESP32-S3, protoboard, jumpers y cable USB-C** | Placa, protoboard y cables confirmados; compra conjunta NO confirmada | **$14.990** ([Pinout](https://pinout.cl/producto/kit-esp32-s3-con-protoboard-830-cables-y-cable-usb-c)) |
| **Arduino UNO compatible** | Placa confirmada; fabricante/costo original no confirmados | **$9.490** ([Neltume Robotics](https://neltumerobotics.cl/productos?category=placas)) |
| **LCD 16×2 I²C** | Pantalla LCD confirmada; dimensiones exactas de la usada no especificadas | **$3.990** ([HUBOT](https://hubot.cl/producto/modulo-display-lcd-1602-con-interfaz-i2c-sku-282-1d1/)) |
| **Lector microSD SPI** | Módulo SD confirmado | **$2.900** ([MechatronicStore](https://www.mechatronicstore.cl/modulo-lector-micro-sd-spi/)) |
| **Tarjeta microSD** | Tarjeta confirmada; capacidad desconocida | **$7.990–$16.990**, referencias 16–32 GB ([pc Factory](https://www.pcfactory.cl/categoria/partes-y-piezas-componentes/almacenamiento/memorias-flash)) |
| **Impresora térmica TTL** | **Costo de compra aproximado**, indicado por Pablo | **~$23.000** en AliExpress (sin boleta adjunta; no es cotización actual) |
| **Madera y pintura del tótem** | **Tope de gasto informado**, no monto exacto | **No más de $60.000** |

**No duplicar el costo de la protoboard ni de los cables**, que el kit ESP32-S3 de referencia ya incluye. Tampoco hay constancia de que el prototipo original utilizara esas marcas o capacidades: se seleccionaron para reproducir la función, no para inventar una factura.

### Cálculo reproducible de la suma PARCIAL

~~~text
Subtotal referencial con tableta económica:
129.990 + 14.990 + 9.490 + 3.990 + 2.900 + 7.990 + 23.000
= $192.350 CLP

Subtotal referencial con tableta más costosa y SD 32 GB:
189.990 + 14.990 + 9.490 + 3.990 + 2.900 + 16.990 + 23.000
= $261.350 CLP

Sumar madera y pintura: M, con 0 < M <= $60.000
Extremo máximo de ESTA SUMA PARCIAL con M=$60.000:
$261.350 + $60.000 = $321.350 CLP
~~~

**Interpretación:** los elementos enumerados, **antes de madera/pintura**, suman aproximadamente **$192.350–$261.350 CLP** con esas referencias. Con la madera y pintura hasta **$60.000**, la **suma parcial podría alcanzar $321.350**. El extremo inferior no es un «costo total mínimo» del proyecto: el costo exacto de la madera **no se conoce**.

**Ejemplo solamente matemático:** si la madera y pintura hubiesen costado $40.000 —**dato NO aportado**— la suma sería $232.350–$301.350. Ese ejemplo no es una afirmación de pago.

## 3. Por qué el costo total de fabricar y operar sigue sin estar cerrado

Faltan precios confirmados de **fuente independiente para impresora**, alimentación de tableta, cable USB del UNO si no estaba disponible, adaptaciones de niveles 5 V/3,3 V, conectores/tornillos/soporte, transporte, energía, herramientas, fallos, consumibles y **horas de montaje y programación**. Algunos podrían estar incluidos en kits o reaprovechados; no se deben sumar dos veces, pero tampoco tratarlos como cero por defecto.

Hay **dos contabilidades distintas**:

- **Gasto histórico en efectivo de HexaCorp:** lo efectivamente comprado para la entrega. La tableta puede haber sido comprada, prestada o reutilizada, pero **no se indicó su modalidad de adquisición**. Solo el monto aproximado de la impresora y el límite de madera/pintura constan como antecedentes de costo.
- **Costo de reposición del prototipo:** valor de adquirir componentes equivalentes en 2026, **incluida una tableta** aun cuando se utilizara una prestada. Sirve para estudiar viabilidad material de la maqueta.
- **Costo de producto comercial instalado:** añade fabricación repetible, contenido validado, seguridad, garantía, soporte, instalación y permisos. No se reduce a la tabla anterior.

## 4. Relación con los cuatro presupuestos del informe de 2025

El [Informe N.º 2 de HexaCorp, sección 9.4.1](../informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf) estimaba **$239.000–$471.000** por la versión interior con botonera, **$380.000–$850.000** por la táctil de 7″, y **$1.921.000–$5.831.000** por variantes exteriores. Eran **configuraciones alternativas proyectadas**, no el inventario de la maqueta real.

La maqueta con una **tableta convencional** puede resultar **más sencilla de replicar** que una pantalla táctil integrada fabricada a medida: aprovecha navegador, panel táctil y Wi-Fi de un equipo de consumo. Sin embargo, **sus referencias de componentes de 2026, su tabla parcial de materiales y los presupuestos conceptuales de 2025 no son directamente equiparables**; por eso no se declara un porcentaje de ahorro ni un ROI.

## 5. Formulación válida para presentar HexaTour

> Para la maqueta académica usamos una tableta convencional como interfaz de administración del portal local. El resto del sistema se implementó con ESP32-S3, Arduino UNO, LCD, tarjeta SD, cables/protoboard y una impresora térmica TTL adquirida por cerca de **$23.000 CLP**. La estructura de madera y pintura **no superó $60.000 CLP**. Con precios de reposición consultados en Chile en noviembre de 2026, los componentes cotizados suman **$192.350–$261.350 antes de madera/pintura**, y podrían llegar a **$321.350** con el tope de esta última partida. **No incluye todo el costo de fabricar un producto comercial ni acredita rentabilidad.**

**Fuentes de referencia consultadas en noviembre de 2026:** [tabletas Lenovo en Falabella](https://www.falabella.com/falabella-cl/shop/tablet-lenovo-m10), [catálogo Falabella](https://www.falabella.com/falabella-cl/category/cat7230007/Tablets), [kit ESP32-S3 Pinout](https://pinout.cl/producto/kit-esp32-s3-con-protoboard-830-cables-y-cable-usb-c), [UNO compatible Neltume](https://neltumerobotics.cl/productos?category=placas), [LCD HUBOT](https://hubot.cl/producto/modulo-display-lcd-1602-con-interfaz-i2c-sku-282-1d1/), [lector MechatronicStore](https://www.mechatronicstore.cl/modulo-lector-micro-sd-spi/), [memorias pc Factory](https://www.pcfactory.cl/categoria/partes-y-piezas-componentes/almacenamiento/memorias-flash). Los precios son referenciales y pueden variar por proveedor, impuestos y disponibilidad.
