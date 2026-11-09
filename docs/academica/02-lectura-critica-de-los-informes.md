# 02 · Lectura crítica y trazabilidad del Informe N.º 2 (HexaCorp, 2025)

[← Académica](README.md) · [Informe original PDF](../informes/Informe%20N%C2%B02.%20Hexatour%2C%20la%20soluci%C3%B3n.pdf) · [Economía y costos](../18-analisis-economico-clp-usd.md) · [Piloto](../20-validacion-operativa-y-pilotos.md)

> **Auditoría posterior del informe histórico, 9 de noviembre de 2026.** Se leyó y cotejó el PDF íntegro **«Hexatour, la solución para: Limitaciones de orientación en la experiencia turística rural en la Región de Coquimbo»** (28 páginas, Coquimbo, 2025) que ya estaba en el repositorio y fue nuevamente suministrado para esta auditoría. **El PDF aportado es idéntico en bytes al del repositorio** (Git blob `27f8a8afd9b884a89a002bf8c5999a88cb0e28d0`). La documentación histórica se **conserva sin cambios**. Las observaciones de 2026 son análisis posterior, no correcciones retroactivas al equipo.

## 1. Qué pretendía demostrar el trabajo

La propuesta de HexaCorp aborda la **orientación turística rural** frente a baja conectividad, señalética limitada y concentración de recorridos en pocos destinos, mediante un **tótem offline-first** con catálogo local y posibles alternativas táctiles, físicas e impresas.

**Fuente:** informe, **§1–2 (PDF páginas 3–4)** y **§4 (PDF páginas 6–7)**. La investigación original menciona **56 %** de conectividad deficiente como principal problema, **38 %** de señalética y **6 %** de concentración, además de **21,54 %** de tiempo promedio sin Internet reportado en trayectos. Estas cifras son **resultados internos del trabajo de HexaCorp** citados desde el Informe N.º 1; **no son porcentajes representativos de toda la región**. No se dispone aquí de una auditoría completa del tamaño muestral, instrumento y sesgo de selección de la encuesta; no extrapolarlos a población, ventas ni ROI.

La sección **§5 (PDF página 8)** presenta **SERNATUR Región de Coquimbo como «cliente ideal» conceptual**. **No** acredita aprobación institucional, patrocinio, compra, contrato, presupuesto adjudicado o convenio. Es un perfil de diseño de propuesta.

## 2. Equipo de trabajo y roles que reconoce el informe

**Fuente:** portada y §3 «Equipo y roles», **PDF páginas 1 y 5**.

| Integrante | Carrera indicada | Rol académico declarado |
| --- | --- | --- |
| **Benjamín Esquivel** | ICCI | Director del Proyecto |
| **Camila Morales** | ICCI | Analista de Investigación e Innovación |
| **Carolina Castillo** | ICI | Coordinadora de Operaciones |
| **Melanie Abdala** | ICI | Responsable de Comunicación y Difusión |
| **Pablo Guzmán** | ICCI | Desarrollador Tecnológico y Presentador |
| **Valentina González** | ICI | Directora Financiera y Estrategia de Recursos |

Profesor del curso: **Alejandro Paolini Godoy**, paralelo **C2**, Universidad Católica del Norte.

La documentación del repositorio [registra](README.md) el aporte tecnológico de **Pablo** al circuito, firmware de **ESP32-S3 y UNO**, portal e integración; atribuye a **Benjamín Esquivel y su padre** la **maqueta física de exposición**. Las otras personas participaron principalmente en investigación, informes y presentaciones. **Los roles listados en la entrega no prueban contratos de empleo, que todos programaron firmware ni la titularidad exclusiva del informe**.

## 3. De la elección de idea al diseño del tótem

El equipo comparó **dispensador de mapas, audioguía NFC, tótem interactivo, alertas para senderos y una «piedra Wi-Fi»**, aplicando una matriz de priorización y SCAMPER. **Fuente:** §7–8, **PDF páginas 10–13**.

La tabla impresa informa **6,19** para «Tótem interactivo», sobre **6,13** de la audioguía NFC. Hay una **inconsistencia aritmética que conviene dejar visible**: la fila «PONDERACIÓN» muestra **0,2 + 0,3 + 0,3 + 0,3 = 1,1**, aunque totaliza **1**. Al aplicar literalmente esos pesos a los cuatro valores del tótem (6,60; 5,20; 6,10; 6,80), la suma sin normalizar es **6,75** y la normalizada por **1,1** sería **6,14**, no **6,19**. **No se modifica el 6,19 original ni se inventa la fórmula que produjo ese resultado**: para reconstruir la selección con rigor se requiere revisar el archivo fuente de la matriz, sus celdas/fórmulas y reglas de normalización.

La metodología permite explicar por qué el equipo se inclinó por una solución híbrida. **No** constituye por sí misma validación de mercado, precisión de una ruta turística o rentabilidad observada.

## 4. Arquitectura propuesta en 2025 frente a lo que está implementado

| Dimensión | Informe original (fuente) | Estado trazable del repositorio |
| --- | --- | --- |
| **Tipo de equipo** | Tótem robusto «tipo cajero» y alternativas mesa/exterior, §8–9 | **Maqueta universitaria** y firmware para placas; ninguna variante comercial exterior certificada |
| **Microcontrolador del producto conceptual** | **ESP32-WROOM-32**, §9.3, PDF **16** | Firmware dirigido a **ESP32-S3** y un **Arduino UNO** para ticketera |
| **Interfaz** | Pantalla táctil o botonera, §9.3, PDF **16–17** | Portal HTML/JS visible en móvil, demo web y simulador; pantalla táctil del tótem comercial no verificada |
| **Catálogo** | SD con fichas/rutas predefinidas; red Wi-Fi local | JSON, imágenes y páginas reales en `web/www`; datos **de ejemplo**, no verificados en terreno |
| **Impresión** | Componentes descritos en §9.3, pero **§10.3 también la considera fuera de la demo** | Código con ESP32→UNO→ticketera, sin revalidación física de los binarios octubre 2026 |
| **NFC/QR** | Acceso por etiquetas NFC/QR como opción del concepto | No presumir que todo lector, etiqueta, QR y flujo descrito esté instalado y validado físicamente |
| **Solar y exterior** | Autonomía solar, gabinete IP, UPS y ventilación como propuestas | No hay demostración actual de autonomía ni gabinete exterior certificado |
| **Accesibilidad/idiomas** | Voz, buzzers, multilenguaje como futuras etapas, §9.1, PDF 15 | No describir esas propuestas como capacidades terminadas |
| **Efecto turístico** | Reducir desorientación y visibilizar servicios locales | No hay piloto en terreno que pruebe impacto en tiempos, afluencia o gasto |

**Inconsistencia interna del informe a aclarar, no a ocultar:** el apartado **§10.2 (PDF 22)** propone una **impresora térmica operativa**, mientras **§10.3 de la misma página** sitúa la impresora física «fuera de esta demo» y describe un ticket por **impresión en pantalla**. La frase correcta para el portafolio es que **se propuso la impresión y existe firmware posterior que la implementa, pero no está documentado aquí un ensayo físico integrado con la compilación actual**.

El informe es una propuesta de producto amplio; el repositorio materializa una **arquitectura concreta y una demo**, no todos los recursos conceptuales de un gabinete exterior.

## 5. Presupuesto histórico: cuatro variantes reales del informe

**Fuente:** §9.4.1 «Por tipo de HexaTour», página impresa **17 / PDF 18**.

| Modelo propuesto (2025) | Costo preliminar **CLP** |
| --- | ---: |
| **Interior · táctil 7”** | **$380.000–$850.000** |
| **Interior · pantalla simple + botonera** | **$239.000–$471.000** |
| **Exterior · táctil alto brillo 15–22”** | **$2.655.000–$5.831.000** |
| **Exterior · pantalla simple + botonera** | **$1.921.000–$3.963.000** |

Son **estimaciones del informe**, no facturas ni versiones producidas y vendidas. No se sabe qué partidas de mano de obra, instalación, fabricación, traslado, garantía, impuestos, actualización del contenido u otros costos se contemplaron exactamente en cada intervalo. No convertirlas en precio final a cliente. [El análisis económico](../18-analisis-economico-clp-usd.md) incorpora una sensibilidad separada y evita utilizar el mismo costo para un módulo interior y un exterior.

### Operación histórica descrita

**Fuente:** §9.4.2, página impresa **18 / PDF 19**.

- **Papel:** tickets estimados de **15 cm** con rollo de **80 m**, rendimiento teórico aproximado de **533 tickets**; para **30/60/100 tickets por día**, la estimación del informe es **2/4/6 rollos mensuales** sobre 30 días.
- **Energía:** operación hipotética de **10 h/día**, consumo interior **~6–12 kWh/mes** y exterior de alto brillo **~24–30 kWh/mes**, sin aporte solar. **No medición del montaje físico**.
- **Preventivo:** **1–2 h mensuales**, **3–4 h trimestrales** y revisiones semestrales/anuales según equipo.
- **Contenido:** revisión mensual o quincenal en alta demanda; **2–4 h/mes** para edición, **1–2 h/mes** para carga/pruebas y **2–4 h de terreno cuando aplique**, según el informe.
- **Repuestos:** impresora, ventilación, UPS/fuente, sellos y **10–20 tags NFC** propuestos como stock.

**Faltan precios unitarios por rollo, tarifa eléctrica local y valor hora, por tanto el informe no acredita un OPEX CLP mensual completo ni flujo de caja.** [Modelo OPEX y rentabilidad](../18-analisis-economico-clp-usd.md).

## 6. Metas de éxito ≠ resultados medidos

**Fuente:** §9.7 «KPI's – Hexatour», página impresa **20 / PDF 21**:

| KPI del informe | Meta original | Evidencia hoy |
| --- | --- | --- |
| Reducción de tiempo de desorientación | **30 % menos** | Meta sin ensayo antes/después acreditado |
| Satisfacción | **≥80 %** de encuestados con **≥8/10** | No hay resultados de usuarios finales del tótem en repositorio |
| Retorno o recomendación | **≥70 %** favorable | Sin seguimiento medido documentado |
| Interacción con funciones avanzadas | **≥50 %** de usuarios | Sin registro de uso real en terreno |

Estas metas son útiles **para diseñar el piloto**. No se deben publicar como «redujimos el tiempo un 30 %» ni «80 % de satisfacción». El [plan de validación](../20-validacion-operativa-y-pilotos.md) define mediciones que permitan evaluarlas sin confundir una demostración con un indicador experimental.

## 7. Rentabilidad empresarial, valor público y evidencia

**La relevancia social** es plausible: una interfaz local podría ayudar a orientación donde hay señal deficiente, si está ubicada y mantenida correctamente. **La rentabilidad empresarial** requiere conocer costo efectivo integral, precio neto aceptado, operación, garantías, demanda y período de evaluación. Ni la tabla de cuatro costos ni los porcentajes de investigación del problema establecen por sí solos un ROI, una venta o un ahorro real.

La sección **§5** define a **SERNATUR como comprador ideal conceptual**, sin que ello signifique licitación, convenio o compromiso. Para una propuesta profesional, comenzar por **piloto pequeño de interior** con un operador real y medir tareas, costos, desgaste y actualizaciones. Una variante exterior requiere tratar por separado estructura, IP, UPS, protección, instalación y permisos.

**Licenciamiento:** el código original publicado tiene [MIT](../../LICENSE); eso **no transforma automáticamente el informe de seis autores, entrevistas, imágenes ajenas y maqueta física en materiales MIT**. Diferenciar aportes y derechos antes de una explotación comercial.

## 8. Fuentes auditables y faltantes reales

**Verificadas:** PDF idéntico al del repositorio, secciones y páginas citadas, nombres/roles, cuatro presupuestos, parámetros operativos y metas académicas. **Pendientes reales:** lista de precios por componente, facturas, condiciones tributarias, fórmulas de matriz original en su XLSX, estimación de horas reales del montaje, pruebas del portal físico/ticketera y datos de pilotaje con visitantes.

No es necesario pedir de nuevo el Informe N.º 2: su información primaria ya está integrada, sin modificarlo. **Para precisar el costeo, el siguiente dato útil son las boletas/BOM o cotizaciones con fecha**, no más supuestos.

[Regresar al capítulo académico](README.md) · [Rentabilidad](../18-analisis-economico-clp-usd.md) · [Mercado](../19-mercado-y-validacion-comercial.md).
