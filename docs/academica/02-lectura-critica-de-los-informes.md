# 02 · Trazabilidad de informes, prototipo, costos y autoría académica

[← Equipo y anexos](README.md) · [Informe 1 y 2](README.md#entregables-de-esa-etapa) · [Rentabilidad](../18-analisis-economico-clp-usd.md) · [Plan técnico de validación](../20-validacion-operativa-y-pilotos.md)

> **Notas posteriores de auditoría, 8-11-2026.** Los PDF y DOCX del curso se conservan sin modificarlos. **Sus archivos binarios están presentes en GitHub, pero no se pudo extraer directamente su texto completo mediante la conexión disponible**. No corresponde atribuirles citas textuales, montos, testimonios de entrevistas o resultados no inspeccionados.

## Origen documental

HexaTour nació en 2025 en la asignatura **Proyecto Diseño e Innovación**, Universidad Católica del Norte, a través del equipo **HexaCorp**. El repositorio reúne:
- **Informe N.º 1**: investigación sobre dificultades de orientación rural en la Región de Coquimbo.
- **Informe N.º 2**: propuesta de solución HexaTour, roles, alternativas de tótem y planificación.
- Anexos: **entrevistas en bruto, cliente ideal, mapa de empatía, matriz de priorización y Carta Gantt**.
- Fuentes editables DOCX junto a los PDF, sin modificar.

**La presencia de un anexo demuestra que se archivó, no que esta auditoría haya leído/validado sus contenidos completos.** La referencia de [costos anterior](../18-analisis-economico-clp-usd.md) menciona estimaciones preliminares para distintas variantes de tótem, **pero no transcribimos valores como históricos** hasta cotejarlos con las páginas originales.

## Equipo académico y atribución que debe preservarse

| Integrante | Rol listado en la documentación académica |
| --- | --- |
| **Benjamín Esquivel** | Director del Proyecto |
| **Carolina Castillo** | Coordinadora de Operaciones |
| **Camila Morales** | Analista de Investigación e Innovación |
| **Melanie Abdala** | Responsable de Comunicación y Difusión |
| **Pablo Guzmán** | Desarrollador Tecnológico y Presentador |
| **Valentina González** | Directora Financiera y Estrategia de Recursos |

En la documentación existente, **Pablo Guzmán** aparece como responsable del **diseño electrónico, firmware ESP32-S3 y Arduino UNO, portal web e integración**. **Benjamín Esquivel y su padre** construyeron la **maqueta física de presentación**. El resto de HexaCorp trabajó principalmente en **investigación, informes y presentaciones**. Se trata de una relación de aportes **según la documentación vigente**, no de una verificación forense de todos los archivos ni un reparto de derechos.

**No atribuir la maqueta a Pablo, ni tratar el código como trabajo técnico igualitario de seis personas, ni borrar los créditos de quienes investigaron el problema.** El profesor del curso fue **Alejandro Paolini Godoy** (paralelo C2). Los roles de gestión anotados en el informe no certifican constitución de empresa ni contratos.

## Qué se construyó y qué faltaba comprobar

| Capa del proyecto | Evidencia de código/archivo | Precaución de interpretación |
| --- | --- | --- |
| Problema turístico | Informes, entrevistas y anexos del curso | Revisión completa de métodos y resultados de entrevistas pendiente |
| Circuito y hardware | `docs/diagramas/HexaTourCircuito.drawio`, mapa de pines y manual | Esquema/maqueta no acreditan certificación eléctrica ni intemperie |
| ESP32-S3 y UNO | Sketches y protocolo STATUS/PRINT/DONE | Compilación de octubre 2026 no equivale a funcionamiento físico actual |
| Portal cautivo | HTML, JS, JSON en SD; AP y DNS en firmware | La demo pública de Pages **no es** un ESP32 operativo |
| Simulador de PC | Python y tests | Impresión y PDF simulados no acreditan ticket/PDF real |
| Contenido turístico | Catálogo demostrativo, 9 categorías y 27 fichas | **Datos de ejemplo**, no indicaciones verificadas |
| Inversión y rentabilidad | Referencias a presupuestos preliminares en informes | Faltan cifras primarias leídas, comprobantes, costos laborales, ventas y ROI real |
| SMS/urgencia | Opción de enlace local configurado desde UI | No envía ni asegura asistencia automáticamente |

## Principio económico para este proyecto universitario

La «conveniencia» se puede estudiar en dos planos diferentes:

1. **Público/social:** utilidad de facilitar información turística a un visitante con conectividad limitada, respeto a la información local y autonomía del recinto, **si se observa en pilotos**.
2. **Privado/comercial:** precio neto aceptado, menos **componentes + estructura + horas + contenido + soporte + garantías + energía + consumibles**, con demanda real.

Es un error sumar supuestos beneficios sociales como ingresos de la empresa, o comparar la maqueta académica con equipos profesionales como si tuvieran la misma protección y garantía. También es incorrecto inferir el precio exacto final del informe sin haber verificado su tabla de costos.

## Tabla de cotejo pendiente con el informe final

Cuando se disponga del contenido íntegro de Informe N.º 2, completar **sin adivinar**:

| Dato del informe | Evidencia todavía requerida |
| --- | --- |
| Presupuesto de cada variante de tótem | Página, tabla, moneda, ítems y fecha |
| Costos de materiales realmente pagados | Boletas y registro de aportes/préstamos |
| Proyección de venta/renta | Página exacta, si se trata de hipótesis o de medición |
| Ahorro o beneficio prometido | Método y población, escenario de comparación |
| Decisiones de priorización | Alternativas evaluadas, ponderaciones y responsables |
| Entrevistas y hallazgos | Tamaño de muestra, preguntas y alcance de las conclusiones |

Ninguna de estas celdas debe rellenarse con estimaciones inventadas. Los nuevos capítulos de [costos](../18-analisis-economico-clp-usd.md) y [mercado](../19-mercado-y-validacion-comercial.md) se presentan por separado, con hipótesis explícitas y fuentes externas, **no como resultados originales del equipo de HexaCorp**.

## Licencias y alcance de la reutilización

El [código propio está publicado bajo MIT](../../LICENSE); permite uso, modificación, distribución y venta del **software original licenciado** respetando aviso y texto. Esto no determina automáticamente los permisos sobre fotografías, entrevistas, figuras de informes grupales, maqueta física ni bibliotecas ajenas. El trabajo académico posee autores y créditos que deben reconocerse; vender un servicio de instalación no exige afirmar propiedad individual de todos esos materiales.

[Créditos completos](README.md) · [Licencia y terceros](../../LICENSING.md).
