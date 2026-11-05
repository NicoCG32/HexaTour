# 01 · Arquitectura de HexaTour, por niveles

El proyecto se organiza en cuatro niveles: contexto, componentes físicos, software y despliegue. Cada diagrama describe el montaje o una de sus modalidades de prueba.

## Nivel 1 · Contexto

```mermaid
flowchart LR
  VIS["Visitante · navegador"] -->|"Wi-Fi local / HTTP"| TOTEM["HexaTour · punto local"]
  OPE["Operador · navegador"] -->|"Portal /main y solicitudes"| TOTEM
  TOTEM -->|"HTML, fichas, indicaciones"| VIS
  TOTEM -->|"Indicaciones impresas"| PAPEL["Ticketera térmica"]
  MANT["Responsable del punto"] -->|"Actualiza SD, firmware y consumibles"| TOTEM
  classDef human fill:#eaf3f6,stroke:#386477,color:#163849;
  classDef device fill:#203f57,stroke:#203f57,color:#ffffff;
  classDef output fill:#f5eee0,stroke:#ac8b4e,color:#5b451c;
  class VIS,OPE,MANT human;
  class TOTEM device;
  class PAPEL output;
```

No se necesita conexión a Internet para consultar el contenido almacenado localmente. La aplicación de SMS, cuando está configurada, depende del dispositivo del visitante y de su servicio de mensajería; **no la envía el ESP32**.

## Nivel 2 · Contenedores y hardware

```mermaid
flowchart TB
  B["Navegador · HTML / CSS / JS"] -->|"HTTP local"| E["ESP32-S3 · AP Wi-Fi, DNS y servidor web"]
  subgraph Equipo["Equipo HexaTour"]
    E <-->|"Archivos y catálogos"| SD[("Tarjeta SD · /www")]
    E --> LCD["LCD 16 × 2 · I²C"]
    E <-->|"UART · STATUS / PRINT / DONE"| UNO["Arduino UNO · firmware impresora"]
    UNO -->|"Serial TTL"| T["Impresora térmica"]
  end
  classDef core fill:#234761,stroke:#234761,color:white;
  classDef storage fill:#e7f1ee,stroke:#377d70,color:#214d44;
  classDef peripheral fill:#f6efe3,stroke:#b58d50,color:#614920;
  class E,UNO core;
  class SD storage;
  class LCD,T peripheral;
```

El **ESP32-S3** hospeda el portal y los endpoints `/api/print-ruta` y `/api/route-pdf`. La **SD** contiene el HTML, scripts, JSON e imágenes. El **UNO** no sirve páginas: recibe una orden serial y controla la impresora. La pantalla LCD informa estados del dispositivo.

El mapa de conexiones resume los pines declarados por los sketches:

![Conexiones principales del ESP32-S3, Arduino UNO, LCD, módulo SD e impresora](diagramas/HexaTourConexionesRevisadas.svg)

**Cableado:** [plano Draw.io original](diagramas/HexaTourCircuito.drawio) · [SVG](diagramas/HexaTourCircuito.svg) · [pines y alimentación](../firmware/README.md#pines-usados). Verifica alimentación y niveles eléctricos en el montaje antes de energizarlo.

## Nivel 3 · Componentes y responsabilidades de software

```mermaid
flowchart LR
  subgraph Frontend["Interfaz en navegador"]
    Pages["Landing / visitante / operador"] --> JS["JavaScript · common + scripts de vista"]
  end
  subgraph Embedded["ESP32 · firmware"]
    HTTP["WebServer · rutas y API"] --> JSON["Lectura de archivos y fichas SD"]
    HTTP --> PDF["Generación de PDF"]
    HTTP --> QUEUE["Máquina de estados de impresión"]
  end
  JS -->|"GET JSON e imágenes"| HTTP
  JS -->|"Imprimir / descargar PDF"| HTTP
  JSON --> SD[("/www/db + /www/img")]
  PDF --> SD
  QUEUE -->|"Serial2"| Uno["UNO · control de ticketera"]
  classDef c fill:#254964,stroke:#254964,color:#fff;
  class HTTP,PDF,QUEUE,Uno c;
```

La navegación y los botones están definidos en páginas HTML. El archivo [`db/index.json`](../web/www/db/index.json) **no genera por sí solo los botones de categorías**. El navegador obtiene listas y fichas JSON con [`common.js`](../web/www/assets/js/common.js). Los scripts [`visitor-lugar.js`](../web/www/assets/js/visitor-lugar.js) y [`main-lugar.js`](../web/www/assets/js/main-lugar.js) resuelven las acciones de cada perfil.

## Nivel 4 · Tres despliegues distintos

```mermaid
flowchart TB
  SRC["Código y contenido del repositorio"] --> LOCAL["Montaje físico"]
  SRC --> MOCK["PC · simulador Python"]
  SRC --> BUILD["Empaquetador de demo"]
  LOCAL --> FW["ESP32 + UNO + SD + impresora"]
  MOCK --> PY["Servidor local con API simulada"]
  BUILD --> PAGES["GitHub Pages · archivos estáticos"]
  classDef source fill:#e8eef4,stroke:#72879a,color:#1d3447;
  classDef physical fill:#dfeee9,stroke:#3a806f,color:#1a5143;
  classDef demo fill:#f5efe2,stroke:#ae8e56,color:#60491c;
  class SRC source;
  class LOCAL,FW physical;
  class MOCK,PY,BUILD,PAGES demo;
```

La demo estática se genera desde `web/www` y usa controles explícitos de simulación; **no contiene un servidor Python ni una API de impresión**. El simulador permite probar la web y endpoints en un PC. El montaje real depende de SD, alimentación y placas; publicar una versión en Pages no actualiza su contenido.

## Fronteras de confianza y limitaciones

1. **Panel de operador:** el ESP32 aplica HTTP Basic al servir `/main/`; eso **no equivale** a autorizar todas las operaciones. Los handlers de impresión y PDF no se protegen por el mismo chequeo. Las credenciales se encuentran definidas en el firmware y deben cambiarse antes de una instalación expuesta.
2. **Red local:** el montaje usa HTTP; las contraseñas de ejemplo y la autenticación básica no son suficientes para operar en un entorno no confiable.
3. **Catálogo:** un JSON correcto técnicamente no equivale a indicaciones reales verificadas; hay que revisarlas antes de instalar el punto.
4. **Salida física:** la aceptación HTTP es anterior al protocolo `STATUS?` → `PRINT` → `DONE`. Un timeout después de enviar puede dejar desconocido si se imprimió.
5. **Prueba del montaje:** la [guía de compilación](../firmware/Compilacion.md#montaje-original-y-revalidación) registra las comprobaciones físicas pendientes con la base actual.

La [arquitectura ampliada](Arquitectura.md) documenta endpoints y contrato serial; [flujos y estados](03-flujo-de-usuario.md) muestra las secuencias completas; [formato de datos](Formato-de-datos.md) define las validaciones.
