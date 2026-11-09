# 19 · Mercado, posicionamiento y estrategia de validación de HexaTour

[← Índice](README.md) · [Análisis económico](18-analisis-economico-clp-usd.md) · [Propuesta del producto](00-problematica-cliente-y-valor.md) · [Plan de piloto](20-validacion-operativa-y-pilotos.md)

> **Investigación externa y estrategia, no resultados de ventas.** Datos sectoriales publicados ≠ demanda demostrada para un tótem. Las cifras de audiencia turística y ofertas comerciales se refieren a fenómenos diferentes; no deben multiplicarse para inventar ingresos, cuota de mercado o TAM.

## 1. Qué problema resuelve en términos concretos

HexaTour no pretende «digitalizar el turismo» en abstracto. Propone algo específico: **ofrecer indicaciones predefinidas e información local desde un punto de consulta, aunque el visitante no tenga datos móviles**, y permitir una salida tangible mediante ticket térmico. Esto puede interesar a recintos con señal débil, visitantes que desean instrucciones impresas y prestadores que deben mantener mensajes coherentes.

**Lo que sí existe en el repositorio:** portal con vistas de visitante y operador, catálogo JSON/imagenes sobre SD para ESP32-S3, AP Wi-Fi y DNS cautivo, controlador de impresión ESP32↔UNO y endpoint PDF en firmware; también simulador Python y demo de GitHub Pages. El contenido actual son **ejemplos, no rutas verificadas**. La prueba física integral con el entorno compilado actual sigue pendiente.

## 2. Señales públicas de relevancia territorial — con fecha y alcance

### Ruralidad y turismo: la oportunidad existe, pero no mide ventas

El [Plan Turismo en Territorios Rurales 2024–2035](https://www.subturismo.gob.cl/wp-content/uploads/2025/07/plan-turismo-y-desarrollo-rural.pdf), publicado por la Subsecretaría de Turismo, señala **brechas de infraestructura, formalización y comercialización** en territorios rurales. Según clasificación comunal con datos del **Censo 2017**, el plan identifica **12 comunas rurales y 3 urbanas para la Región de Coquimbo**; **no** significa que las doce necesiten o comprarían un HexaTour. El plan indica que más del **50 % de los viajes turísticos internos** llegan a comunas rurales: **no equivale a personas sin señal móvil ni demanda por un kiosco**.

El [MOP documenta](https://planeamiento.mop.gob.cl/document/analisis-requerimientos-de-infraestructura-mop-de-apoyo-al-turismo/) déficits de infraestructura turística y metodologías de priorización territorial, sin constituir un programa de adquisición de HexaTour. La [CEPAL](https://www.cepal.org/es/publicaciones/69126-estrategia-transformacion-digital-chile-digital-2035-plan-conectividad-efectiva) describe brechas de conectividad efectiva, que hacen pertinente evaluar experiencias **offline-first**. Ninguna de esas fuentes mide conversiones o utilidad específica del dispositivo.

Como magnitud sectorial, el [SIET de SERNATUR](https://datosturismo.sernatur.cl/siet/) registra **6.004.567 llegadas de turistas extranjeros en Chile en 2025**. Es tráfico turístico a nivel país, **no compradores potenciales de HexaTour** y tampoco conteo de visitantes rurales de la Región de Coquimbo. No utilizar esta cifra para proyectar unidades ni revenue.

**[Interpretación]** La oportunidad de mercado no es «toda persona que visita Chile», sino un conjunto menor de **instituciones o prestadores con un punto de atención definido y un costo real de orientación no resuelto**.

## 3. Segmentos que merecen una entrevista

| Segmento comprador posible | Motivación verificable a explorar | Quién aprueba y paga | Qué puede bloquear la compra |
| --- | --- | --- | --- |
| **Centro de interpretación / museo local** | Preguntas repetidas sobre recintos, rutas y horarios | Administrador / sostenedor | Ya dispone de guías, señalética o atención suficiente |
| **Prestador turístico rural** | Información de experiencias y acceso sin internet móvil del visitante | Dueño / cooperativa | Baja afluencia, mantenimiento, limitaciones de energía |
| **Camping o parque privado** | Indicaciones para servicios internos y orientación de acceso | Administración | Información cambia frecuentemente, responsabilidad por rutas |
| **Municipio u oficina turística** | Complementar información presencial en punto delimitado | Área turismo/compras con procedimientos propios | Presupuesto, licitación, accesibilidad, garantías, seguridad |
| **Feria / evento temporal** | Portal de información local por tiempo limitado | Organizador | Costo de logística mayor que utilidad, competencia con QR/señalética |
| **Proyecto educativo / exhibición** | Mostrar IoT, UX y redes locales en talleres | Docente / institución | Necesita guías y mantenimiento más que tótem permanente |

**No hay contratos ni validación de disposición a pagar documentados**. El primer nicho debe elegirse por acceso real a instalaciones y posibilidad de medir utilidad, no por TAM proyectado desde población.

## 4. Alternativas reales y por qué algunas ganan

| Alternativa del visitante/recinto | Ventajas | Desventajas potenciales frente al problema específico | Condición bajo la que gana |
| --- | --- | --- | --- |
| **Señalética física / folletos** | Funciona sin energía ni móvil, costo y mantenimiento previsibles | Contenido menos fácil de cambiar; no ofrece catálogo amplio | Pocos destinos y rutas estables |
| **QR a sitio web / Google Maps** | Familiar y posible navegación en vivo con conectividad | Puede depender de Internet o mapas descargados | Buena señal o contenido previamente disponible en móvil |
| **Personal de informaciones** | Atención flexible, personalizada | Horarios y carga de trabajo | Consultas complejas, inclusión o afluencia baja |
| **Tótem comercial con pantalla integrada** | Hardware diseñado para uso intensivo, soporte y garantías según proveedor | Precio y soporte de plataforma a comparar; no necesariamente offline | Recinto con flujo elevado y presupuesto, requisitos profesionales |
| **HexaTour, adaptación validada** | Catálogo local y ticket, código MIT, arquitectura sin SaaS obligatorio | Necesita validación física, contenido, seguridad, mantenimiento, homologación de hardware | Información local estable, fallo frecuente de conectividad y responsable presente |

**No presentar HexaTour como un sustituto universal.** Para muchas ubicaciones, **un cartel actualizado y folletos** pueden ser más eficientes económica y ecológicamente.

## 5. Referencias de productos: nichos y barreras

Dos proveedores chilenos anuncian precios de vitrinas (consulta de noviembre de 2026): [Tottem Chile](https://tottem.cl/totem-autoservicio/) publica un tótem de **24” mural con impresora a CLP 1.090.000 + IVA** y pedestal de **24” a CLP 1.190.000 + IVA**; [EC Group](https://www.ecgroup.cl/producto-detalle/totem-administrador-de-fila-nuevo.php) publica uno de **15” para gestión de filas a CLP 1.790.000 + IVA**. Sus características, software, garantías y costos no son iguales a HexaTour. **No afirmar que HexaTour cuesta un porcentaje menor** sin fabricar y cotizar un prototipo con tamaño, montaje, fiabilidad y soporte equivalentes.

**Posicionamiento que sí merece prueba:** orientación territorial **local, portátil/adaptable y mantenible sin conexión de datos externa**, con contenido propio del recinto, soporte profesional disponible como servicio opcional y un sistema de indicaciones impresas. La presencia de una **impresora física** es un diferenciador funcional que aumenta costo y riesgo; un piloto puede comparar versión con y sin ticketera.

## 6. Propuesta de valor por comprador

**Para el visitante:** información seleccionada localmente y una salida impresa, siempre que el contenido haya sido validado. Medir tiempo para encontrar ficha, tasa de éxito y comprensión de indicaciones.

**Para el operador:** un punto con catálogo definido que reduce tareas repetidas de orientación *si la consulta realmente se completa*. Medir preguntas que siguen requiriendo asistencia, tiempos de actualización, fallos e impresiones fallidas.

**Para la entidad que paga:** costo total y continuidad de un servicio que resulta útil en condiciones del recinto. Medir costo por consulta útil, garantías, tiempo de personal **realmente liberado** y satisfacción, sin monetizar por defecto el valor de cada visita.

## 7. Modelos de monetización compatibles con MIT

1. **Equipo y puesta en marcha:** venta o arriendo de un módulo adaptado con instalación y prueba.
2. **Contenido territorial:** revisión, redacción y producción de fichas/indicaciones con responsables locales y atribución.
3. **Mantenimiento:** actualizaciones, papel, visitas, diagnóstico, capacitación y recambio de componentes, cuando se contraten.
4. **Desarrollo a medida:** integración de catálogos, accesibilidad, bilingüismo u otros requisitos **solo si se implementan**.
5. **Taller educativo:** formación sobre ESP32, interfaces offline, protocolos e información local.

La [licencia MIT](../LICENSE) autoriza reutilizar el código propio bajo sus condiciones, **incluido uso comercial y redistribución**. No basar un modelo en regalías obligatorias, exclusividad del firmware o cobros por licencias que MIT no exige. Sí puede cobrarse por **trabajo y servicios** adicionales, y por equipos y contenidos sobre los que existan los derechos correspondientes.

## 8. TAM, SAM, SOM: no convertir turistas en ingresos

- **TAM teórico (dirección del problema):** tipos de recintos que pueden beneficiarse de información local offline. **Sin número acreditado**.
- **SAM abordable (primer nicho):** recintos accesibles para entrevistar, con presupuesto y responsables operativos, dentro de una zona y período definidos. **Pendiente de listado verificable**.
- **SOM obtenible:** piloto(s) y contratos realmente negociables bajo capacidad de fabricación y soporte. **Cero ventas/contratos confirmados en los documentos revisados**.

Una proyección rigurosa sería `recintos potenciales × tasa de elegibilidad observada × tasa de compra observada × precio neto realmente negociado`, con sensibilidad de fallos, costos, plazos y cancelaciones. **No se cuenta hoy con estas tasas**. Los volúmenes de turistas de SERNATUR **no** se pueden tratar como un mercado transaccional directo.

## 9. Riesgos que pesan más que el marketing

- **Orientación incorrecta:** horarios, rutas o puntos de inicio erróneos; necesita revisión con fuente, fecha y responsable.
- **Seguridad y abuso:** credenciales de ejemplo y endpoints físicos con autorización insuficiente. No poner en servicio público tal como está.
- **Impresión:** `200` de API es aceptación, no éxito del ticket; `DONE` no inspecciona papel ni calidad.
- **Disponibilidad:** SD corrupta, energía, temperatura, vandalismo, incompatibilidades de portal cautivo; sin SLAs medidos.
- **Accesibilidad:** el portal por teléfono no sirve a todos; se necesita cartelería legible y rutas de acceso alternativas.
- **Dependencia de conocimiento local:** el software puede estar bien, pero si el destino no mantiene los contenidos, su utilidad decae.
- **Comercialización pública:** compras y permisos son procesos institucionales, no una venta automática por alineación con políticas públicas.

## 10. Guion de validación de demanda

Primero elegir **un recinto concreto** y registrar sin sesgo al menos estos aspectos cualitativos: conectividad real, preguntas frecuentes, visitantes sin smartphone, posibilidad de impresión, soporte técnico disponible, frecuencia con que cambian rutas y responsable de aprobar cada ficha. Después probar una versión **sin equipo costoso**, por ejemplo una página local con contenido revisado y un flujo de impresión simulado; medir si la gente llega y entiende.

**Solo después** solicitar cotización de instalación y preguntar por precio aceptable, presupuesto disponible, ciclo de compra, garantía y quién actualiza. Si la respuesta indica que señalética simple es suficiente, **no forzar el tótem como solución**.

### Síntesis persuasiva, pero verificable

> **HexaTour convierte una idea de innovación turística rural en un sistema local auditable: un visitante encuentra contenidos sin depender de Internet y puede conservar indicaciones impresas.** Su combinación de Wi-Fi local, contenido SD, Arduino/ESP32 y licencia MIT permite estudiar adaptaciones sin cuota obligatoria de nube. **El negocio todavía debe demostrarse** frente a alternativas simples, con un punto instalado seguro, contenido autorizado, demanda observada, operación sostenible y margen real.

**Fuentes consultadas:** [Subsecretaría de Turismo, plan rural 2024–2035](https://www.subturismo.gob.cl/wp-content/uploads/2025/07/plan-turismo-y-desarrollo-rural.pdf); [SIET de SERNATUR](https://datosturismo.sernatur.cl/siet/); [CEPAL, Chile Digital 2035](https://www.cepal.org/es/publicaciones/69126-estrategia-transformacion-digital-chile-digital-2035-plan-conectividad-efectiva); [MOP, apoyo al turismo](https://planeamiento.mop.gob.cl/document/analisis-requerimientos-de-infraestructura-mop-de-apoyo-al-turismo/); [Tottem Chile](https://tottem.cl/totem-autoservicio/); [EC Group](https://www.ecgroup.cl/producto-detalle/totem-administrador-de-fila-nuevo.php). La interpretación es propia de esta auditoría; ninguna de estas entidades valida o respalda comercialmente HexaTour.
