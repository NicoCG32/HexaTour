# 18 · Estudio de costos, rentabilidad y sostenibilidad de HexaTour

> **Prefactibilidad razonada, 8 de noviembre de 2026.** HexaTour fue un prototipo académico, no una empresa con ventas acreditadas. Distingo **hechos del repositorio**, **antecedentes académicos**, **precios externos**, **escenarios ilustrativos** y **resultados reales pendientes**. Ningún número construido aquí equivale a dinero gastado, venta realizada, oferta comercial o beneficio logrado.

[← Índice](README.md) · [Estudio de mercado](19-mercado-y-validacion-comercial.md) · [Montaje](../firmware/README.md) · [Atribución y antecedentes](academica/README.md) · [Pruebas para un piloto](20-validacion-operativa-y-pilotos.md)

## 1. Tesis económica: no vender un microcontrolador, resolver una tarea

Un visitante busca información y orientación en un territorio donde el acceso a Internet puede ser difícil. Una organización local debe mantener esa información vigente, y tal vez imprimir indicaciones para que el visitante se las lleve. **HexaTour busca reducir la dependencia de una conexión externa**, proporcionando catálogo local servido por un ESP32-S3, navegación desde el celular y ticket térmico mediante un Arduino UNO.

La ventaja de arquitectura es razonable: **no hay API de rutas, mapas ni plataforma SaaS obligatoria para servir el contenido preparado en SD**. Pero ahorrar una cuota remota **no implica operación gratuita**: energía, hardware, consumibles, estructura física, renovación de fichas, señalética, validación de rutas, garantías y visitas de mantenimiento siguen teniendo costo.

**No planteamos sustituir a Google Maps, señalética normativa ni personal de rescate.** La información es **predefinida, no calcula trayectos reales**, y la funcionalidad SMS solo puede preparar un mensaje en el dispositivo del visitante, sin que el sistema asegure su envío. Para justificar económicamente un punto físico, necesitamos evaluar utilidad **en un recinto concreto**, no extrapolar el turismo regional a ventas.

## 2. Qué dice —y qué no podemos concluir aún— del informe académico

Los documentos [Informe 1 e Informe 2 de HexaCorp](academica/README.md) registran la investigación y estimaciones preliminares sobre diversas formas de tótem durante el curso. El repositorio conserva originales PDF y DOCX en `docs/informes/`.

**Límite de esta revisión:** se verificó la existencia de esos archivos y las referencias documentales que los describen, **pero la conexión de GitHub no permitió extraer su contenido binario textual**. Por tanto **no transcribo importes, supuestas ventas, porcentajes de retorno ni BOM como si hubieran sido leídos y verificados en el informe final**. Las tablas a continuación son **modelos nuevos, explícitamente hipotéticos**; se reemplazarán por cifras históricas comprobadas cuando se revise el informe original de forma íntegra. [Trazabilidad académica](academica/02-lectura-critica-de-los-informes.md).

### El perímetro del costo importa

Tres productos de distinto tamaño no pueden compararse usando solo el precio de las dos placas:

| Variante | Qué cambia en costo | Estado |
| --- | --- | --- |
| **Portal local en equipos existentes** | Placas, SD, conexión, alimentación, preparación de contenido y soporte; la pantalla la aporta el visitante | Arquitectura en código; necesita ensayo integrado |
| **Módulo con ticketera y LCD de estado** | Se agregan UNO, impresora térmica, fuente adecuada, papel, cableado, estructura y mantenimiento | Firmware y esquema disponibles; prueba física con la compilación actual pendiente |
| **Tótem autónomo completo** | Además pantalla/terminal, estructura robusta, protección contra intemperie, instalación eléctrica y accesibilidad física | **No existe una especificación comercial validada**; no deducirla de la maqueta universitaria |

La [maqueta presentada en el curso](academica/README.md) no constituye por sí misma un producto industrial para intemperie, instalado o con garantía.

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

ROI real =
  (beneficio neto atribuible de un período - inversión inicial)
  / inversión inicial
  [no confundir ingresos brutos o margen con beneficio neto]
```

### Sensibilidad ilustrativa — NO precios históricos ni estimaciones verificadas

Para hacer el análisis falsable utilizo **[SUPUESTOS]**: costo variable **CLP 650.000** por un punto instalado básico con contenido inicial, y costos fijos de arranque/validación comercial **CLP 1.000.000** para el período. **No se pueden deducir estos montos de los informes binarios que no se pudieron leer.** La estructura, pantalla, garantía y demás condiciones exactas se desconocen.

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

1. **Consultar íntegramente el Informe N.º 2** y registrar cada presupuesto histórico con página, fecha, unidad, alcance y composición. No reescribir el PDF original.
2. Recuperar **BOM, boletas y fotos** del montaje académico y aclarar si pantalla/tableta, estructura, impresora, fuentes y materiales fueron prestados, donados o comprados.
3. Construir una **cotización actual comparable**, con 2–3 proveedores por componente y destino en Chile; moneda, IVA y plazos.
4. Cronometrar ensamblaje, recarga de catálogo, corrección de fichas e instalación.
5. Medir consumo eléctrico real, páginas y papel por ticket, fallos y vida útil.
6. Entrevistar posibles compradores (museo local, centro de interpretación, prestador rural) antes de fijar un precio.
7. Probar un **piloto integrado** y contar resultados, abandonos, tareas completadas, impresión real y mantenimiento.
8. Solo entonces construir ingresos, escenarios de pérdida, sensibilidad, flujo de caja y ROI del proveedor y del comprador por separado.

## Conclusión defendible

**HexaTour es una arquitectura potencialmente costo-efectiva para orientación local de información predefinida, donde un punto con contenido en SD y Wi-Fi propio puede reducir la dependencia de servicios remotos.** La función de impresión y la posibilidad de reutilizar el código MIT abren un camino hacia productos y servicios adaptados al territorio. **No está demostrada su rentabilidad económica**, porque faltan presupuesto histórico verificado, lista de materiales actual, pruebas físicas integradas y precio/disposición de pago. La apuesta razonable es empezar con **un piloto de información útil**, no con la promesa de vender una red de tótems.

### Procedencia y referencias

- **Fuentes propias:** [Informe N.º 2 (PDF)](informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf) — **existencia verificada; importe no extraído**, [firmware/README](../firmware/README.md), [estado funcional](02-funcionalidades.md), [protocolo de impresión](03-flujo-de-usuario.md), [licencia](../LICENSING.md).
- **Contexto territorial:** [Plan de Turismo en Territorios Rurales 2024–2035, Subsecretaría de Turismo](https://www.subturismo.gob.cl/wp-content/uploads/2025/07/plan-turismo-y-desarrollo-rural.pdf); [DataTurismo SERNATUR](https://www.sernatur.cl/dataturismo/); [CEPAL: conectividad efectiva Chile Digital 2035](https://www.cepal.org/es/publicaciones/69126-estrategia-transformacion-digital-chile-digital-2035-plan-conectividad-efectiva).
- **Precios externos consultados, no equiparables:** [Tottem Chile](https://tottem.cl/totem-autoservicio/), [EC Group](https://www.ecgroup.cl/producto-detalle/totem-administrador-de-fila-nuevo.php).
