# 18 — Escenarios económicos CLP / USD

<!-- DOCUMENTACION:nivel-2026-10-29:BEGIN -->

**Nivel:** desarrollo del proyecto.

## Escenarios económicos de HexaTour

**Finalidad:** presupuestar decisiones futuras, no tasar el repositorio ni declarar costos/ventas históricos. Alcance modelado: **Reproducción de un punto y medición de operación/mantenimiento**. No hay precio de instalación, operador contratado ni mantenimiento vendido confirmados. Equipamiento y consumibles requieren cotización; la reserva es ilustrativa.

### Moneda y supuestos

Conversión: **USD 1 = CLP 994,29**, valor del **27-10-2026** en la [tabla oficial SII](https://www.sii.cl/valores_y_fechas/dolar/dolar2026.htm), último día con cifra visible al consultar el 29-10-2026. No se atribuye ese valor al día 29 ni a una transacción bancaria. CLP = USD × R; USD = CLP / R, con R = 994,29.

Para valorizar esfuerzo se supone **CLP 15.000/h** (USD 15,09/h). Es una tasa elegida para comparar escenarios, no sueldo de mercado, tarifa profesional ni compromiso del responsable. Rangos de horas, mantenimiento y reservas también son supuestos; no se deducen de SCT, commits o líneas de código.

### Inversión del siguiente alcance

| Concepto                        | Base del escenario                       | CLP                     | USD                   |
| ------------------------------- | ---------------------------------------- | ----------------------- | --------------------- |
| Tiempo del siguiente alcance    | 16–40 h a CLP 15.000/h                   | CLP 240.000–CLP 600.000 | USD 241,38–USD 603,45 |
| Reserva de materiales           | Supuesto; equipo existente no valorizado | CLP 200.000             | USD 201,15            |
| Total de inversión de escenario | No es inversión histórica ni cotización  | CLP 440.000–CLP 800.000 | USD 442,53–USD 804,59 |

### Operación mensual

Servicios obligatorios en el escenario local: USD 0/mes; no significa costo total cero. Equipo, tiempo, consumibles, distribución, almacenamiento y servicios opcionales deben presupuestarse cuando se necesiten.

| Concepto                        | Base                               | CLP/mes    | USD/mes   |
| ------------------------------- | ---------------------------------- | ---------- | --------- |
| Mantenimiento de escenario      | 3 h/mes                            | CLP 45.000 | USD 45,26 |
| Servicios externos de escenario | Ver composición; no factura actual | CLP 0      | USD 0,00  |
| Costo mensual modelado          | Tiempo + servicios                 | CLP 45.000 | USD 45,26 |

No se suman aquí impuestos, comisiones, dominio, sobreconsumo, reposición extraordinaria o equipo no valorizado. Costos de nube por proyecto/organización y cuotas gratuitas deben revisarse para la cuenta concreta. Una cuota de nube no sustituye la arquitectura ni la validación necesarias para escalar.

### Justificación y retorno

Ejemplo **hipotético**, no resultado medido: evitar 2 h/mes a la misma tasa representa CLP 30.000 / USD 30,17 de tiempo valorizado, no ingresos. Frente al costo modelado, el saldo de ese ejemplo es CLP -15.000 / USD -15,09 al mes. El punto de equilibrio por ahorro temporal sería 3.00 h/mes; debe comprobarse con uso real, pérdidas evitadas o un beneficio distinto.

Capacidad de encontrar indicaciones, cobertura sin internet y tasa de acciones físicas completadas; mantenimiento por punto de información.

ROI sólo se calcula cuando beneficios y costos comparables estén medidos: (beneficio − costo) / costo, indicando período y si el tiempo valorizado realmente se convierte en ahorro. Un costo de caja bajo no acredita rentabilidad ni valor comercial de la idea.

### Sensibilidad y decisión

- Con R ±10 %, cambia en ±10 % el costo CLP de servicios fijados en USD; el gasto local CLP no cambia por ese supuesto.
- Separar creación puntual de mantenimiento recurrente y reserva física de consumo.
- Registrar facturas/uso, horas observadas y aceptación antes de reemplazar estos escenarios por un presupuesto comprometido.
- Las monedas ficticias de un videojuego, saldos de clientes e inventario de una empresa no son ingresos del software.

### Referencias de servicios

[Supabase](https://supabase.com/pricing): Free y Pro desde USD 25/mes; [Vercel](https://vercel.com/pricing): Hobby y Pro desde USD 20/mes. Son referencias consultadas, no planes asignados al proyecto. [Gemini](https://ai.google.dev/gemini-api/docs/pricing) y [Firebase](https://firebase.google.com/pricing) requieren revisar producto/modelo, cuotas y condiciones antes de cuantificar consumo. El plan actual de Lovable u otro proveedor no se deduce de estas tarifas.

## Fuentes de implementación y contratos

[README.md](../README.md) · [docs/Arquitectura.md](Arquitectura.md) · [docs/Formato-de-datos.md](Formato-de-datos.md) · [docs/Despliegue.md](Despliegue.md) · [firmware/README.md](../firmware/README.md) · [tools/backend-local/README.md](../tools/backend-local/README.md).
<!-- DOCUMENTACION:nivel-2026-10-29:END -->
