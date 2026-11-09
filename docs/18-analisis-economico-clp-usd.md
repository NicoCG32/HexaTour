# 18 · Estudio de costos, rentabilidad y sostenibilidad de HexaTour

> **Prefactibilidad razonada, 8 de noviembre de 2026.** HexaTour fue un prototipo académico, no una empresa con ventas acreditadas. Distingo **hechos del repositorio**, **antecedentes académicos**, **precios externos**, **escenarios ilustrativos** y **resultados reales pendientes**. Ningún número construido aquí equivale a dinero gastado, venta realizada, oferta comercial o beneficio logrado.

[← Índice](README.md) · [Estudio de mercado](19-mercado-y-validacion-comercial.md) · [Montaje](../firmware/README.md) · [Atribución y antecedentes](academica/README.md) · [Pruebas para un piloto](20-validacion-operativa-y-pilotos.md)

## 1. Tesis económica: no vender un microcontrolador, resolver una tarea

Un visitante busca información y orientación en un territorio donde el acceso a Internet puede ser difícil. Una organización local debe mantener esa información vigente, y tal vez imprimir indicaciones para que el visitante se las lleve. **HexaTour busca reducir la dependencia de una conexión externa**, proporcionando catálogo local servido por un ESP32-S3, navegación desde el celular y ticket térmico mediante un Arduino UNO.

La ventaja de arquitectura es razonable: **no hay API de rutas, mapas ni plataforma SaaS obligatoria para servir el contenido preparado en SD**. Pero ahorrar una cuota remota **no implica operación gratuita**: energía, hardware, consumibles, estructura física, renovación de fichas, señalética, validación de rutas, garantías y visitas de mantenimiento siguen teniendo costo.

**No planteamos sustituir a Google Maps, señalética normativa ni personal de rescate.** La información es **predefinida, no calcula trayectos reales**, y la funcionalidad SMS solo puede preparar un mensaje en el dispositivo del visitante, sin que el sistema asegure su envío. Para justificar económicamente un punto físico, necesitamos evaluar utilidad **en un recinto concreto**, no extrapolar el turismo regional a ventas.

## 2. Antecedente económico primario: Informe N.º 2 de HexaCorp (2025)

**Fuente primaria verificada:** [`docs/informes/Informe N°2. Hexatour, la solución.pdf`](informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf), **sección 9.4 «Análisis de costos (Preliminar)»**, **páginas impresas 17–18 (páginas 18–19 del PDF)**. Se cotejó el PDF completo compartido posteriormente con el PDF ya guardado en GitHub: **los bytes son idénticos (blob Git `27f8a8afd9b884a89a002bf8c5999a88cb0e28d0`)**. Por tanto ya es posible citar el informe original con precisión.

### 2.1 Costos preliminares de 2025 por versión

| Modelo **propuesto** en el informe | Partes destacadas | Rango histórico estimado **CLP** | Página |
| --- | --- | ---: | --- |
| **A.1 · Interior con pantalla táctil de 7”** | ESP32, pantalla, impresora térmica, NFC, fuente y mueble MDF/PLA | **$380.000–$850.000** | 17 / PDF 18 |
| **A.2 · Interior con pantalla simple y botonera** | LCD 20×4, keypad 4×4, impresora, NFC, ESP32, fuente y mueble | **$239.000–$471.000** | 17 / PDF 18 |
| **B.1 · Exterior con táctil de alto brillo de 15–22”** | Pantalla ≈1.000 nits, gabinete IP, sellos/visera, UPS, ventilación, impresora, NFC | **$2.655.000–$5.831.000** | 17 / PDF 18 |
| **B.2 · Exterior con pantalla simple y botonera** | LCD/keypad o pantalla simple, gabinete IP, UPS, ventilación/filtros, impresora y NFC | **$1.921.000–$3.963.000** | 17 / PDF 18 |

**Esta es la cotización preliminar del equipo en 2025, no el costo real del montaje construido.** El informe no acompaña en esa tabla facturas, lista de precios unitarios, cotizaciones vigentes, horas técnicas facturadas, desglose de impuestos ni margen comercial. **Tampoco es un precio de venta**. Sus cuatro configuraciones son **alternativas conceptuales**; el repositorio actual utiliza **ESP32-S3 + Arduino UNO y portal desde SD**, y no contiene una implementación final certificada de las cuatro.

La menor estimación corresponde al **modelo interior con botonera**. En cambio, los modelos exteriores incorporan pantalla/gabinete robusto, UPS y protección, que elevan significativamente la inversión. **No presupuestar un exterior completo con el costo del interior** ni asumir que el modelo físico académico acredita grado IP o uso en vía pública.

### 2.2 Operación y mantenimiento tal como lo plantea el informe (2025)

El apartado **9.4.2**, página impresa **18 (PDF 19)**, contiene parámetros de planificación útiles. **Son supuestos y procedimientos propuestos**, no consumos de laboratorio ni tickets observados:

| Concepto | Hipótesis del informe | Cómo convertirla en gasto verificable |
| --- | --- | --- |
| **Ticket térmico** | Ticket de **15 cm**; rollo de **80 m** ≈ **533 tickets** | Rollos consumidos × precio efectivo por rollo, con merma y fallos |
| **30 tickets/día × 30 días** | **2 rollos/mes**, aproximadamente | `ceil(900/533)` = 2 |
| **60 tickets/día × 30 días** | **4 rollos/mes**, aproximadamente | `ceil(1800/533)` = 4 |
| **100 tickets/día × 30 días** | **6 rollos/mes**, aproximadamente | `ceil(3000/533)` = 6 |
| **Electricidad interior** | **6–12 kWh/mes**, uso **10 h/día**, sin solar | kWh medidos × tarifa efectiva CLP/kWh |
| **Electricidad exterior, alto brillo** | **24–30 kWh/mes**, uso **10 h/día**, sin solar | kWh medidos × tarifa efectiva CLP/kWh |
| **Preventivo mensual** | **1–2 h/mes** | Horas reales × tarifa técnica + insumos |
| **Preventivo trimestral** | **3–4 h/trimestre** | Prorratear cuando corresponda; registrar limpieza/controles |
| **Contenido** | Editar **2–4 h/mes**; cargar y probar **1–2 h/mes**; traslado **2–4 h** cuando aplique | Tarifas diferenciadas de editor/técnico, viajes y periodicidad |
| **Repuestos** | Cabezal/cutter, ventiladores/filtros, fuente/UPS, **10–20 tags NFC**, tornillería/sellos | Provisiones de stock, sustituciones reales y fallas registradas |

La lectura aritmética es simple: **80 metros / 0,15 metros = 533,33 tickets teóricos por rollo**. La cuenta supone tickets de exactamente 15 cm, sin encabezados de desperdicio, atascos ni corte fallido; en terreno el rendimiento puede ser menor. Del mismo modo, **6–12 kWh/mes en 300 h** equivale a **20–40 W promedio**, y **24–30 kWh/mes** a **80–100 W promedio**; son **potencias implícitas de los escenarios**, no lecturas reales del hardware.

**[Derivación sin tiempos medidos]** Si se prorratea también el mantenimiento trimestral, sin viajes ni averías, la planificación sugiere **aprox. 5–9,33 h/mes por punto** entre preventivo mensual (1–2), trimestral (1–1,33) y actualización de contenidos (3–6). **No son horas facturadas, remuneraciones ni un contrato existente.** Falta agregar instalación inicial, garantía, incidencias, anualidades y desplazamientos cuando existan.

**Gasto mensual mínimo a cotizar**, sin inventar precio de papel, electricidad ni valor hora:

```text
OPEX mensual (CLP) ≈
  (rollos reales × precio por rollo)
  + (kWh medidos × tarifa CLP/kWh)
  + (horas de mantenimiento × valor hora técnico)
  + (horas de edición × valor hora editor)
  + traslado/viáticos cuando aplique
  + repuestos efectivamente gastados y reservas justificadas
```

Sin tarifa eléctrica local, precio de rollo, incidencias y horas observadas **no existe un OPEX total en pesos acreditado**.

### 2.3 Tres advertencias al comparar el informe con el repositorio

1. **Proyecto académico vs producto final:** el informe especifica un **ESP32-WROOM-32** para un modelo de producto en su sección **9.3 (página impresa 15 / PDF 16)**, mientras que el firmware disponible está diseñado para **ESP32-S3**, y además se emplea un **Arduino UNO** para la impresión. **No son BOM ni arquitecturas equivalentes de fabricación.**
2. **Funciones conceptuales vs demo:** en sección **10.2** aparece una impresora térmica en el montaje previsto, pero la sección **10.3** también clasifica la impresora física «fuera de esta demo» y describe una **impresión por pantalla** (página impresa 21 / PDF 22). Esta tensión histórica debe declararse, no resolverla inventando una prueba funcional del prototipo de 2025.
3. **Resultado económico y metas:** una tabla de costos de compra no es un balance, y los objetivos de reducción de desorientación/satisfacción de la **sección 9.7 (PDF 21)** son **metas, no mejoras medidas**.

[Lectura crítica completa del informe académico](academica/02-lectura-critica-de-los-informes.md).

## 2.4 Materiales de la maqueta REAL: tableta convencional y periféricos

Un antecedente **posterior al informe de 2025** cambia la lectura de la viabilidad del prototipo: según el responsable tecnológico, **la maqueta presentada usó una tableta convencional para abrir el portal local con una cuenta de administración/operador**. No fue necesario desarrollar ni comprar una pantalla táctil industrial específica para esa muestra; la tableta era **un navegador cliente del ESP32-S3**, no el servidor del catálogo.

La maqueta también utilizó **ESP32-S3, Arduino UNO, LCD, protoboard/jumpers de kit, módulo y tarjeta SD, ticketera TTL y madera/pintura**. Dos antecedentes de costo **directos del montaje**: **impresora térmica TTL ~CLP $23.000** adquirida en AliExpress y **madera más pintura ≤CLP $60.000**. **La tableta era propiedad personal de Pablo Guzmán y fue prestada temporalmente al equipo**, sin desembolso de HexaCorp para comprar una nueva. **La carpintería de la maqueta fue aportada sin remuneración por Benjamín Esquivel y su padre**; Pablo recuerda **aproximadamente un día de construcción, quizá un segundo día calendario por secado de pintura**, no dos jornadas activas completas. Ambos son aportes no monetarios para la entrega académica, no recursos gratuitos de replicar comercialmente. Benjamín Esquivel y su padre construyeron la maqueta física; Pablo Guzmán desarrolló la integración tecnológica según [créditos de HexaCorp](academica/README.md).

Se preparó una [**BOM de reposición trazable, elemento por elemento**](academica/03-costeo-maqueta-fisica.md) con referencias chilenas consultadas el **9 de noviembre de 2026**. Para una tableta genérica de entrada, un **kit ESP32-S3 que ya incluye protoboard/jumpers**, UNO compatible, LCD I²C, lector y tarjeta SD, **más los $23.000 referidos por la impresora**, la **suma parcial de referencia, sin madera/pintura**, es **CLP $192.350–$261.350**. Si se agrega el **tope de $60.000** en madera/pintura, el extremo máximo de esa suma parcial alcanza **$321.350**. **No es gasto efectivamente pagado en 2025 ni costo total cerrado**: la tableta fue prestada y la carpintería fue donada. Faltan eventualmente fuentes, cables/soportes especiales, traslados, **valor económico de carpintería** y trabajo técnico. **El tope de $60.000 corresponde exclusivamente a madera y pintura, no a mano de obra**.

| Cifra | Qué representa |
| --- | --- |
| **$23.000 aprox.** | **Compra de la impresora**, informada directamente, sin boleta adjunta |
| **No más de $60.000** | **Límite informado** de madera y pintura, no valor exacto |
| **$0 de compra** | **Tableta personal prestada por Pablo** para HexaCorp: desembolso incremental por esa tableta; su valor económico **no es cero** |
| **$0 pagado** | **Mano de obra de carpintería** aportada por Benjamín y su padre a la maqueta académica; valor de reproducción aún no medido |
| **$129.990–$189.990** | **Reemplazo estimado de tableta** con precios observados de 2026, no gasto del equipo ni precio de adquisición original |
| **$192.350–$261.350** | Suma de una canasta de **componentes referenciales** con impresora informada, **antes de madera/pintura** |
| **$321.350** | Máximo aritmético de esa **canasta parcial** si madera/pintura alcanzara su tope; **no** máximo del costo total del proyecto |

### Mano de obra de la maqueta: no desembolsada, pero económicamente significativa

Para la entrega universitaria, **HexaCorp no compró la tableta de Pablo ni pagó la carpintería de Benjamín y su padre**. Esa colaboración hizo que el **gasto de caja** fuera menor que el **costo de reproducción del prototipo**. **No se deben capitalizar ni contabilizar como pago efectuado los aportes personales**; sí corresponde reconocerlos como recursos necesarios para fabricar otra unidad.

**Referencia de mercado, NO cotización del proyecto:** [Obra Maestra 2026](https://obramaestra.com/guias/cuanto-cobrar-mano-de-obra-construccion-chile) publica **$10.000–$15.000 por hora de carpintero**, valores generales de orientación. Si se supone una dedicación *hipotética* de **8 horas-persona**, la carpintería aportaría **$80.000–$120.000 de costo económico**; con **16 horas-persona**, **$160.000–$240.000**. **El tiempo calendario recordado es de alrededor de un día de construcción, quizá otro día por secado; las horas-persona de trabajo activo siguen sin conocerse**. No se atribuyen tarifas cobradas ni un segundo día completo de carpintería por la espera de pintura. Para una cotización real, cuantificar horas-persona de cada uno, grado de terminación y presupuestos de taller, sin sumar dos veces madera, pintura o insumos.

**Sensibilidad para una construcción de aproximadamente un día, NO cronometraje:** según si dos personas hubieran dedicado en total **8–16 horas-persona activas** a la estructura, el costo económico referencial a **$10.000–$15.000/h** sería **$80.000–$240.000**. Al sumar a la canasta parcial de reposición **$192.350–$321.350**, el resultado ilustrativo sería **$272.350–$561.350 antes de fuentes, herramientas, trabajo tecnológico, transporte y otros costos omitidos**. El **secado al día siguiente**, si ocurrió, afecta el **plazo de terminación**, pero no se factura automáticamente como 8 horas activas extra. **No son horas ni pagos históricos verificados, ni un precio de venta acreditado**.

```text
Desembolso académico (tableta): $0 (préstamo temporal)
Desembolso académico (carpintería): $0 (aporte de compañeros)
Valor económico de réplica:
  tableta a costo de reposición + materiales físicos
  + horas-persona de carpintería × tarifa razonada
  + electrónica, integración, seguridad, pruebas y operación
```

[Desglose y escenarios completos](academica/03-costeo-maqueta-fisica.md).

### Implicación en rentabilidad

Esta reconstrucción sustenta la **factibilidad material de un módulo de exhibición interior con tableta estándar**, mucho mejor que extrapolar directamente un gabinete industrial al proyecto académico. **No sustituye los $380.000–$850.000 del «interior táctil 7”» del informe**, porque aquel era un producto conceptual diferente y se costeó en 2025. Tampoco demuestra un beneficio de ventas: para ofrecer HexaTour comercialmente hay que valorar **montaje repetible, horas de programación, estructura instalada, fiabilidad, actualización de fichas, garantía, transporte, electricidad y papel**. La simulación de costo variable **$650.000** del apartado 5 **sigue siendo un escenario comercial completamente hipotético**, no la factura de la maqueta.

## 3. Costos que deben presupuestarse

| Capa | Partidas mínimas | Evidencia para costear |
| --- | --- | --- |
| **Electrónica** | ESP32-S3, Arduino UNO, SD y módulo, LCD I²C, cableado, adaptación de niveles, conectores, impresora compatible | Modelo exacto, boleta/cotización, fecha, impuestos y flete |
| **Alimentación** | Fuentes separadas, cables, protecciones, extensión y consumo real | Especificación de la impresora, voltaje/corriente medidos y revisión de seguridad |
| **Tótem** | Estructura, anclaje, señalética, pantalla si se ofrece, protección contra sol/humedad/vandalismo | Plano, grado de uso, diseño y proveedor |
| **Contenido local** | Investigación de lugares, verificación de rutas/horarios, material visual autorizado, edición de fichas, localización | Horas por ficha y fecha de revisión |
| **Montaje y control de calidad** | Armado, cableado, flasheo, SD, pruebas de teléfonos, comprobación UART y ticket físico | Horas de técnico + bitácora |
| **Instalación** | Transporte, preparación de lugar, permisos, visita, capacitación y documentación entregada | Distancias y tarifa/horas reales |
| **Operación** | Energía, rollos de papel, reparaciones, reemplazos, actualización de fichas y garantías | Consumo eléctrico, tickets/mes, tasa de fallos, soporte contratado |
| **Comercialización** | Prospección, demostraciones, impuestos aplicables, comisiones, pagos y administración | Facturas, contratos y costo de adquisición por cliente |

**No contabilizar dos veces la mano de obra:** si la instalación ya incluye las horas de adaptación de contenido, no sumarlas otra vez dentro del mantenimiento inicial.

## 4. Referencias públicas de precio en Chile — no son equivalencias

Se consultaron ofertas accesibles en noviembre de 2026:

| Producto externo publicado | Precio indicado | Por qué NO demuestra ventaja de costo de HexaTour |
| --- | --- | --- |
| [Tottem Chile: tótem autoservicio mural 24” con impresora integrada](https://tottem.cl/totem-autoservicio/) | **CLP 1.090.000 + IVA** | Incluye pantalla táctil Android, carcasa, impresora y otros accesorios; HexaTour no acredita ese equipamiento ni esa garantía |
| [Tottem Chile: tótem pedestal 24” con impresora integrada](https://tottem.cl/totem-autoservicio/) | **CLP 1.190.000 + IVA** | Incluye estructura y pantalla de pedestal; no se conoce la BOM comparable del prototipo |
| [EC Group: tótem administrador de fila 15” con impresora](https://www.ecgroup.cl/producto-detalle/totem-administrador-de-fila-nuevo.php) | **CLP 1.790.000 + IVA** | Control de turnos, PC y mueble metálico; resuelve **otro problema** y no incluye necesariamente software de la misma finalidad |

Son **precios de vitrina**, no compras realizadas, ni cotizaciones vigentes garantizadas, ni una valoración de HexaTour. Los impuestos se muestran exactamente como los anuncian los proveedores. Una comparación comercial útil debe igualar tamaño de pantalla, accesorios, garantía, protección, uso y servicio. El sistema local podría evitar un computador integrado **en algunas configuraciones**, pero no debemos afirmar un ahorro porcentual hasta construir y cotizar variantes equivalentes.

## 5. Economía unitaria de un punto instalado

```text
Costo variable por instalación (CV) =
  materiales + estructura/pantalla necesaria + ensamblaje + ensayo
  + contenido inicial + transporte + reservas de garantía + costos comerciales variables

Margen de contribución por instalación (MC) =
  precio neto efectivamente cobrado - CV

Punto de equilibrio en unidades =
  redondear hacia arriba(costos fijos del período / MC)
  [solo si MC > 0, y sin confundir ventas con cobros]

Resultado operativo del período =
  instalaciones cobradas × MC - costos fijos del período

ROI sobre la inversión inicial (%) =
  100 × (flujos netos acumulados después de costos recurrentes
          - inversión inicial) / inversión inicial
  [definir horizonte, impuestos, reposiciones y cobros reales]
```

### Sensibilidad ilustrativa — NO precios históricos ni estimaciones verificadas

**[SUPUESTOS NUEVOS, NO DEL INFORME]** El siguiente ejemplo plantea un punto **interior hipotético** con costo variable total **CLP 650.000** (contenido/instalación incluidos, sin desglose empírico) y costos fijos de arranque/validación comercial **CLP 1.000.000** para el período. El valor de $650.000 cae dentro del **rango histórico del interior táctil ($380.000–$850.000)**, pero **eso no prueba que dicho rango incluya el mismo equipo, las horas, las protecciones o el contenido supuesto**. **Este ejercicio NO aplica a las variantes exteriores**, estimadas históricamente entre $1.921.000 y $5.831.000 según modelo. Ningún precio propuesto ha sido validado con compradores.

| Precio neto hipotético del servicio instalado | Margen unitario matemático | Unidades de equilibrio |
| ---: | ---: | ---: |
| CLP 800.000 | CLP 150.000 | **7** |
| CLP 900.000 | CLP 250.000 | **4** |
| CLP 1.100.000 | CLP 450.000 | **3** |

**Cálculo:** con cuatro instalaciones netas a CLP 900.000, la contribución total sería **4 × CLP 250.000 = CLP 1.000.000**, que cubriría exactamente los **costos fijos supuestos**. **No significa utilidad obtenida** ni confirma que existan cuatro compradores. Si el costo variable crece por una pantalla, reparaciones o una carcasa segura, el margen disminuye.

### Sensibilidad por costo variable, precio neto fijo ilustrativo de CLP 900.000

| CV hipotético | MC calculado | Equilibrio con CLP 1.000.000 fijos |
| ---: | ---: | ---: |
| CLP 500.000 | CLP 400.000 | 3 unidades |
| CLP 650.000 | CLP 250.000 | 4 unidades |
| CLP 800.000 | CLP 100.000 | 10 unidades |
| CLP 900.000 | CLP 0 | No existe punto de equilibrio |

**Advertencia tributaria:** precio «neto» y costos «netos» deben compararse sobre la misma base, sin mezclar IVA incluido con montos antes de impuestos. Impuestos a la renta, financiación, inflación y flujo de caja no se han modelado; **no hay cálculo de rentabilidad financiera completa**.

## 6. Posible ingreso recurrente: contenidos y mantenimiento

Una ventaja de HexaTour no es solo instalar una caja, sino **mantener verdaderas las indicaciones**. La tarjeta SD puede contener datos locales sin servicio de nube; alguien debe verificar horarios, rutas, cierres, obras, contactos y alertas, y registrar cuándo y por quién se actualizan.

**[SUPUESTO DIDÁCTICO]** Contrato opcional de CLP 60.000 **netos/mes** por punto para actualización y soporte limitado; costo operacional directo de CLP 30.000/mes. Margen **CLP 30.000/mes por punto**, o **CLP 360.000 por 12 meses** solo si se factura, cobra y conserva el servicio todo el año. No hay contratos, usuarios pagadores, SLA ni métricas de soporte que acrediten esas cifras.

**No se vende «nube obligatoria»**: el mantenimiento remoto requeriría una arquitectura que hoy no existe. El costo real de una visita presencial puede absorber todo el margen; por eso es fundamental medir distancia, frecuencia de cambios y tiempos por ficha.

## 7. Rentabilidad para el comprador: otra pregunta distinta

Para un museo, centro turístico o recinto rural, comprar un punto puede convenir porque reduce consultas repetitivas al personal, permite ofrecer información fuera de horario de atención **si el recinto está abierto**, o entrega instrucciones impresas. **Son hipótesis, no resultados de un piloto**.

```text
Costo total anual para el comprador =
  precio instalado + 12 × mantenimiento mensual
  + energía, papel y otros cargos no incluidos

Horas-equivalentes de equilibrio =
  costo total anual / valor económico por hora
```

**[EJEMPLO HIPOTÉTICO]** A un punto de CLP 900.000 más CLP 60.000/mes, el primer año cuesta **CLP 1.620.000**, antes de energía/papel adicionales. Si la institución atribuye un valor real verificable de **CLP 8.000 por hora liberada**, necesitaría **202,5 horas útiles de trabajo equivalentes/año**, unas **16,9 horas/mes**, para igualar ese costo, **si esas horas efectivamente pueden reasignarse o se evita un costo**. Si no existen ese tiempo ni una métrica de mejora, no hay ROI demostrable.

El beneficio podría ser **accesibilidad, experiencia turística y continuidad informativa** aunque no produzca ahorro monetario directo. Para entidades públicas o educativas eso puede justificar un piloto por valor social, pero **no debe registrarse como utilidad empresarial**.

## 8. Otros factores que alteran la rentabilidad

- **Uso real:** número de visitantes que se conectan, tareas completadas y tickets realmente retirados.
- **Consumibles:** rendimiento por rollo depende de longitud efectiva de cada ticket, errores, reimpresiones y precio comprado; sin esas mediciones no se calcula costo por impresión.
- **Energía:** se necesita potencia media/pico del montaje real, en especial de la ticketera y eventual pantalla; un ESP32 no determina el consumo de todo el tótem.
- **Seguridad:** el backend embebido usa HTTP y la API de imprimir/PDF no queda protegida como `/main/`. Antes de operar con público hay que revisar rutas, credenciales, autenticación y abuso de impresión.
- **Responsabilidad:** instrucciones turísticas erróneas pueden perjudicar visitantes. No prometer asistencia de emergencia ni guiado GPS en vivo.
- **Obsolescencia:** impresora, rollos, soporte de navegador, compatibilidad de portal cautivo y repuestos.
- **MIT:** reutilizar código propio sin regalías es legal bajo su licencia; el negocio se justificaría por equipo, implementación, contenido, operación y soporte diferenciados, no por exclusividad del código.

## 9. Decisiones mínimas para una evaluación real

1. **Hecho:** se revisó íntegramente el **Informe N.º 2** y se incorporaron **cuatro rangos de inversión por variante**, parámetros de papel, energía y dedicación, con páginas exactas. **Pendiente:** boletas y desglose de precios unitarios, impuestos e inclusión real de montaje/soporte. Conservar el PDF sin alteraciones.
2. **Avance documental:** la maqueta usó una **tableta personal prestada por Pablo ($0 de compra para el equipo)**, ESP32-S3, UNO, LCD, SD, ticketera TTL y madera pintada. La impresora costó **~$23.000** y madera/pintura no superaron **$60.000**. **Benjamín y su padre aportaron gratuitamente la carpintería**; se recuerda **un día de construcción, con posible día adicional de secado**, sin horas-persona activas comprobadas. Faltan costo efectivo de estructura, fuentes, accesorios y comprobantes. [BOM y valor económico de carpintería](academica/03-costeo-maqueta-fisica.md).
3. Construir una **cotización actual comparable**, con 2–3 proveedores por componente y destino en Chile; moneda, IVA y plazos.
4. Cronometrar ensamblaje, recarga de catálogo, corrección de fichas e instalación.
5. Medir consumo eléctrico real, páginas y papel por ticket, fallos y vida útil.
6. Entrevistar posibles compradores (museo local, centro de interpretación, prestador rural) antes de fijar un precio.
7. Probar un **piloto integrado** y contar resultados, abandonos, tareas completadas, impresión real y mantenimiento.
8. Solo entonces construir ingresos, escenarios de pérdida, sensibilidad, flujo de caja y ROI del proveedor y del comprador por separado.

## Conclusión defendible

**HexaTour ofrece una arquitectura potencialmente costo-efectiva para orientación local de información predefinida, donde un portal desde SD y Wi-Fi propio puede reducir la dependencia de servicios remotos.** El **informe original identifica un punto de entrada interior de $239.000–$471.000 (botonera) y uno táctil de $380.000–$850.000 en costos preliminares de 2025**. **La maqueta realmente presentada utilizaba una tableta personal prestada por Pablo como terminal, y su carpintería fue un aporte no remunerado de Benjamín y su padre**, y su canasta de componentes referenciales de reposición **suma $192.350–$261.350 antes de madera/pintura (tope $60.000)**, pero el exterior asciende a varios millones de pesos. La impresión y la licencia MIT abren vías de productos/servicios asociados. **La rentabilidad real no está demostrada:** no hay BOM facturada actual, prueba física integrada, precio aceptado ni costos operacionales observados. Empezar por un **piloto de interior o informativo supervisado** suele ser una hipótesis más prudente que prometer un gabinete exterior o una red.

### Procedencia y referencias

- **Fuentes propias:** [Informe N.º 2 (PDF)](informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf) — **verificado directamente: §9.3, §9.4.1–9.4.2 y §10, páginas impresas 15, 17, 18 y 21**, [firmware/README](../firmware/README.md), [estado funcional](02-funcionalidades.md), [protocolo de impresión](03-flujo-de-usuario.md), [licencia](../LICENSING.md).
- **Contexto territorial:** [Plan de Turismo en Territorios Rurales 2024–2035, Subsecretaría de Turismo](https://www.subturismo.gob.cl/wp-content/uploads/2025/07/plan-turismo-y-desarrollo-rural.pdf); [DataTurismo SERNATUR](https://www.sernatur.cl/dataturismo/); [CEPAL: conectividad efectiva Chile Digital 2035](https://www.cepal.org/es/publicaciones/69126-estrategia-transformacion-digital-chile-digital-2035-plan-conectividad-efectiva).
- **Precios externos consultados, no equiparables:** [Tottem Chile](https://tottem.cl/totem-autoservicio/), [EC Group](https://www.ecgroup.cl/producto-detalle/totem-administrador-de-fila-nuevo.php).
