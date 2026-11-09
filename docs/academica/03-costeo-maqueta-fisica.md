# 03 · Montaje real de la maqueta y costo referencial de reposición

[← Índice académico](README.md) · [Viabilidad y costos](../18-analisis-economico-clp-usd.md) · [Arquitectura](../01-arquitectura-general.md) · [Informe original 2025](../informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf)

> **Reconstrucción al 9 de noviembre de 2026.** Este capítulo incorpora información directa entregada por **Pablo Guzmán**, responsable técnico, acerca de lo que efectivamente se utilizó en la **maqueta universitaria**. Los precios de tiendas son **referencias de reposición en 2026**, NO importes que el grupo pagó en 2025. No se han suministrado facturas o modelos originales de tableta, Arduino y otros módulos. **Precisión confirmada posteriormente:** la tableta era **propiedad personal de Pablo y fue prestada temporalmente al proyecto**, sin compra específica del equipo; **la fabricación de la estructura fue un aporte sin cobro de carpintería** por un integrante y su colaborador. El no haber pagado la mano de obra no elimina su costo económico en caso de reproducción profesional.

## 1. Así funcionaba el montaje de la presentación

La **pantalla del tótem era una tableta convencional** que abría, en su navegador, el **portal local con usuario de administración/operador**. No era una pantalla táctil industrial específica, ni hay evidencia de un controlador de pantalla escrito para un modelo comercial concreto. **La tableta actuaba como cliente web**, no como servidor del catálogo. El **ESP32-S3** proporcionaba la red local/portal con contenido desde la tarjeta SD; el **Arduino UNO** se encargaba del firmware relacionado con la impresora TTL.

El montaje **utilizó** un ESP32-S3, Arduino UNO, pantalla LCD, protoboard y cables típicos de kits, módulo y tarjeta SD, impresora térmica TTL, **una tableta personal prestada temporalmente por Pablo Guzmán** y una estructura de madera pintada. **No hubo desembolso del grupo para adquirir esa tableta**; su valor de reposición sigue siendo relevante para replicar la maqueta. El **precio aproximado de adquisición de la impresora en AliExpress fue CLP $23.000**. **La madera más la pintura no superaron CLP $60.000**: no se conoce el gasto exacto. **Ese tope no incluye el valor económico de la carpintería**, que fue aportada sin cobro al proyecto académico.

La **construcción física y trabajos de carpintería de la maqueta** estuvieron a cargo de **Benjamín Esquivel y su padre**, **sin cobro al equipo** según la aclaración aportada; el diseño del circuito y la integración tecnológica se atribuyen a Pablo según la [documentación académica](README.md). **Contribución no remunerada no significa que la labor careciera de valor**. **Pablo recuerda aproximadamente un día de construcción**, con **posible segundo día calendario por secado de pintura**. **No** es un registro horario y no se sabe cuántas horas activas aportó cada persona. No se atribuye una jornada laboral completa ni una factura ficticia.

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
| **Tableta Android de entrada, 8,7–10,1″ aprox.** | **Tableta personal de Pablo, prestada sin cobro al grupo**; costo de compra para HexaCorp: **$0 incremental**. Marca, tamaño y valor original desconocidos; valor de reposición no es cero | **$129.990–$189.990** (tabletas económicas [Samsung Galaxy A11, ABC](https://www.abc.cl/); [Lenovo M10/Tab, Falabella](https://www.falabella.com/falabella-cl/shop/tablet-lenovo-m10)) |
| **Kit ESP32-S3, protoboard, jumpers y cable USB-C** | Placa, protoboard y cables confirmados; compra conjunta NO confirmada | **$14.990** ([Pinout](https://pinout.cl/producto/kit-esp32-s3-con-protoboard-830-cables-y-cable-usb-c)) |
| **Arduino UNO compatible** | Placa confirmada; fabricante/costo original no confirmados | **$9.490** ([Neltume Robotics](https://neltumerobotics.cl/productos?category=placas)) |
| **LCD 16×2 I²C** | Pantalla LCD confirmada; dimensiones exactas de la usada no especificadas | **$3.990** ([HUBOT](https://hubot.cl/producto/modulo-display-lcd-1602-con-interfaz-i2c-sku-282-1d1/)) |
| **Lector microSD SPI** | Módulo SD confirmado | **$2.900** ([MechatronicStore](https://www.mechatronicstore.cl/modulo-lector-micro-sd-spi/)) |
| **Tarjeta microSD** | Tarjeta confirmada; capacidad desconocida | **$7.990–$16.990**, referencias 16–32 GB ([pc Factory](https://www.pcfactory.cl/categoria/partes-y-piezas-componentes/almacenamiento/memorias-flash)) |
| **Impresora térmica TTL** | **Costo de compra aproximado**, indicado por Pablo | **~$23.000** en AliExpress (sin boleta adjunta; no es cotización actual) |
| **Madera y pintura del tótem** | **Tope de gasto en materiales**, sin carpintería | **No más de $60.000** |
| **Carpintería, armado y terminaciones** | **Trabajo aportado sin cobro por Benjamín Esquivel y su padre**; aproximadamente 1 día de fabricación y eventual día 2 por secado, sin horas-persona comprobadas | **Desembolso académico por ese trabajo: $0**; **costo económico: pendiente de horas × tarifa o cotización** |

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

**Interpretación:** los elementos enumerados, **antes de madera/pintura**, suman aproximadamente **$192.350–$261.350 CLP** con esas referencias y **asignando valor de reposición a la tableta aunque no se compró para HexaTour**. Con la madera y pintura hasta **$60.000**, la **suma parcial podría alcanzar $321.350**. **No incluye mano de obra de carpintería**, ni otras partidas pendientes: **$321.350 NO es el costo comercial total ni el gasto en efectivo histórico**. El extremo inferior tampoco es un «costo total mínimo»: el costo exacto de la madera **no se conoce**.

**La tableta prestada explica una reducción de desembolso académico, no una reducción del costo de reposición comercial.** No se resta su valor del modelo de reposición; simplemente se registra una salida de caja incremental de **$0** para el equipo en esa partida.

### Carpintería: aporte no remunerado y valoración económica

Para HexaCorp, **el desembolso atribuible a la mano de obra de carpintería fue $0**, porque la construcción fue un aporte de un compañero (Benjamín Esquivel) y su padre. Para **replicar el tótem por encargo**, se requiere presupuestar **corte y armado de madera, refuerzos, fijaciones, lijado, preparación, pintura y terminaciones** según el trabajo efectivamente realizado. **El período recordado es de ~1 día de construcción, posiblemente 2 días calendario contando el secado de pintura; no hay registro de horas por persona ni presupuesto de taller. El secado pasivo no equivale a otra jornada remunerada ni a 8 horas adicionales de carpintería.**

```text
Costo económico de la carpintería =
  (horas-persona de Benjamín + horas-persona del colaborador) ×
  tarifa referencial/hora aplicable
  + cualquier traslado, alquiler de herramientas o consumible adicional
  [descontar los materiales ya incluidos en "madera y pintura"]

Costo económico de la maqueta =
  suma de materiales y equipos a precio de reposición
  + valor de mano de obra de carpintería
  + trabajo técnico/ensayos y otros costos no incluidos
```

**Referencia pública solo orientativa:** una guía de [Obra Maestra, tabla de mano de obra 2026](https://obramaestra.com/guias/cuanto-cobrar-mano-de-obra-construccion-chile) publica **$10.000–$15.000 CLP por hora de carpintero**. Como contraste, [2x3 (30-05-2026)](https://www.2x3.cl/p/precios-carpintero) publica **$50.000–$150.000 CLP por trabajo general**, condicionado al tipo de encargo. **Son referencias externas generales, no cotizaciones específicas del tótem ni remuneraciones que recibieron sus constructores**.

| Horas-persona **hipotéticas** de carpintería en total | A $10.000/h, ejemplo | A $15.000/h, ejemplo |
| --- | ---: | ---: |
| 8 h-persona (ejemplo: 2 personas × 4 h activas) | $80.000 | $120.000 |
| 12 h-persona (ejemplo: 2 personas × 6 h activas) | $120.000 | $180.000 |
| 16 h-persona (ejemplo: 2 personas × 8 h activas) | $160.000 | $240.000 |

**Las horas de la tabla son hipótesis para valorar un trabajo que, según el recuerdo del responsable técnico, se realizó en aproximadamente un día.** No se afirma que Benjamín y su padre trabajaran efectivamente 8, 12 o 16 horas-persona. Sumar el tiempo **activo de ambos** si se recupera; **no** multiplicar «2 días de calendario» × «2 personas» × «8 horas», porque el posible segundo día correspondió al **secado**. Si la tarifa de taller incluye pintura/materiales, evitar duplicarlos. Una réplica comercial precisa presupuestos de carpintería con fotos, dimensiones y terminaciones.

**Ejemplo de sensibilidad matemática:** con **8–16 horas-persona hipotéticas de trabajo activo**, aplicando la banda referencial $10.000–$15.000/h, la carpintería representaría **$80.000–$240.000**. Sumada al rango de **canasta parcial** de $192.350–$321.350, daría **$272.350–$561.350 antes de fuentes, transporte, trabajo técnico y otros pendientes**. **No es una factura histórica ni una estimación de horas realmente observadas.** Que la pintura se seque al día siguiente puede alargar el **plazo calendario** sin generar una jornada equivalente de **mano de obra activa**.

## 3. Por qué el costo total de fabricar y operar sigue sin estar cerrado

Faltan precios confirmados de **fuente independiente para impresora**, alimentación de tableta, cable USB del UNO si no estaba disponible, adaptaciones de niveles 5 V/3,3 V, conectores/tornillos/soporte, transporte, energía, herramientas, fallos, consumibles y **horas de montaje y programación**. Algunos podrían estar incluidos en kits o reaprovechados; no se deben sumar dos veces, pero tampoco tratarlos como cero por defecto.

Hay **tres contabilidades distintas**:

- **Desembolso histórico académico:** la tableta personal de Pablo se **prestó temporalmente** y **no se compró para el equipo ($0 adicional)**. Benjamín y su padre realizaron carpintería **sin cobrar ($0 desembolsado por ese trabajo)**. Sí se informa la compra aproximada de la impresora (**~$23.000**) y **un gasto conjunto de madera/pintura que no excedió $60.000**, pero faltan montos efectivos de otros materiales.
- **Costo económico de reproducción:** incorporar tableta a valor de reposición, **carpintería y terminaciones a valor económico** —con un día aproximado de construcción como referencia temporal, no como total de horas-persona—, demás partes, electricidad, herramientas y trabajo tecnológico. Las aportaciones gratuitas **no son recursos cuyo uso carezca de costo de oportunidad**.
- **Costo de producto comercial instalado:** añade fabricación repetible, contenido validado, seguridad, garantía, soporte, instalación y permisos. No se reduce a la tabla anterior.

## 4. Relación con los cuatro presupuestos del informe de 2025

El [Informe N.º 2 de HexaCorp, sección 9.4.1](../informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf) estimaba **$239.000–$471.000** por la versión interior con botonera, **$380.000–$850.000** por la táctil de 7″, y **$1.921.000–$5.831.000** por variantes exteriores. Eran **configuraciones alternativas proyectadas**, no el inventario de la maqueta real.

La maqueta con una **tableta personal prestada por Pablo**, integrada como terminal convencional, puede resultar **más sencilla de replicar** que una pantalla táctil integrada fabricada a medida: aprovecha navegador, panel táctil y Wi-Fi de un equipo de consumo. Sin embargo, **sus referencias de componentes de 2026, su tabla parcial de materiales y los presupuestos conceptuales de 2025 no son directamente equiparables**; por eso no se declara un porcentaje de ahorro ni un ROI.

## 5. Formulación válida para presentar HexaTour

> Para la maqueta académica utilicé **una tableta personal prestada temporalmente** como terminal para la vista de administración del portal local, **sin compra para el equipo**. La impresora térmica TTL costó cerca de **$23.000 CLP**, y la **madera y pintura no superaron $60.000 CLP**. **Benjamín Esquivel y su padre realizaron gratuitamente la carpintería del cuerpo físico** en **aproximadamente un día**, con posible segundo día de **secado de pintura**; eso permitió presentar el prototipo con menor desembolso, pero **no elimina el valor económico del trabajo activo**. A precios referenciales de 2026, la canasta de componentes con tableta de reposición suma **$192.350–$261.350 antes de madera/pintura**, y hasta **$321.350 con el tope de esos materiales, sin carpintería ni otros pendientes**. **No es costo total comercial ni rentabilidad observada.**

**Fuentes de referencia consultadas en noviembre de 2026:** [tabletas Lenovo en Falabella](https://www.falabella.com/falabella-cl/shop/tablet-lenovo-m10), [catálogo Falabella](https://www.falabella.com/falabella-cl/category/cat7230007/Tablets), [kit ESP32-S3 Pinout](https://pinout.cl/producto/kit-esp32-s3-con-protoboard-830-cables-y-cable-usb-c), [UNO compatible Neltume](https://neltumerobotics.cl/productos?category=placas), [LCD HUBOT](https://hubot.cl/producto/modulo-display-lcd-1602-con-interfaz-i2c-sku-282-1d1/), [lector MechatronicStore](https://www.mechatronicstore.cl/modulo-lector-micro-sd-spi/), [memorias pc Factory](https://www.pcfactory.cl/categoria/partes-y-piezas-componentes/almacenamiento/memorias-flash). Los precios son referenciales y pueden variar por proveedor, impuestos y disponibilidad.
