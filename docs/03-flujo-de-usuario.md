# 03 · Recorridos, secuencias y estados

## Recorrido del visitante

```mermaid
flowchart TD
  A["Abrir portal local o demo"] --> B["Elegir categoría"]
  B --> C["Leer lista JSON"]
  C --> D["Seleccionar lugar"]
  D --> E["Cargar ficha e imagen"]
  E --> F{"¿Qué quiere hacer?"}
  F -->|"Ver indicaciones"| G["Mostrar imagen de ruta"]
  F -->|"Descargar PDF"| H{"¿Qué modalidad?"}
  H -->|"Montaje"| I["ESP32 genera PDF"]
  H -->|"Simulador"| J["PDF simplificado de prueba"]
  H -->|"Demo"| K["PDF no disponible"]
  F -->|"Urgencia"| L["Mostrar aviso / SMS preparado sólo si hay configuración"]
  classDef step fill:#e8f2f6,stroke:#477d94,color:#18394b;
  classDef limit fill:#fff1dd,stroke:#b6863e,color:#5a421b;
  class A,B,C,D,E,G,I,J,L step;
  class K limit;
```

En demo, la opción de urgencia muestra un aviso local. En el montaje puede abrir un SMS preparado si existe configuración; el usuario realiza el envío desde su aplicación. Las rutas mostradas son predefinidas.

## Recorrido del operador e impresión física

```mermaid
sequenceDiagram
  autonumber
  actor O as Operador
  participant W as Navegador
  participant E as ESP32 / API
  participant SD as Tarjeta SD
  participant U as Arduino UNO
  participant T as Ticketera
  O->>W: Elegir categoría y lugar
  W->>E: Solicitar lista y ficha
  E->>SD: Leer JSON e imágenes
  SD-->>E: Contenido
  E-->>W: Datos del lugar
  O->>W: Solicitar impresión
  W->>E: GET /api/print-ruta?cat=...&slug=...
  E->>SD: Obtener route.text
  alt Ruta inexistente / ocupado / SD fallida
    E-->>W: HTTP de error
  else Trabajo aceptado
    E-->>W: HTTP 200 «print job accepted»
    Note over W,E: La aceptación no demuestra que el ticket esté listo
    E->>U: STATUS?
    U-->>E: STATUS|1 o STATUS|0
    alt Disponible
      E->>U: PRINT|id|texto
      U->>T: Imprimir (bloqueante)
      U->>U: Retorno de imprimirTexto()
      U-->>E: DONE|id
    else Ocupado o sin respuesta
      Note over E,U: Cancelación o timeout en firmware
    end
  end
```

El ESP32 envía `STATUS?`, espera hasta **3 s** por respuesta, envía `PRINT` si corresponde y espera hasta **10 s** por `DONE`. El UNO emite `DONE` al terminar su rutina de impresión; no comprueba el papel ni la calidad del ticket. La aplicación no dispone de una consulta web posterior del estado final.

## Máquina de estados del ESP32

```mermaid
stateDiagram-v2
  [*] --> ESP_IDLE
  ESP_IDLE --> ESP_PREGUNTA_STATUS: API acepta trabajo
  ESP_PREGUNTA_STATUS --> ESP_ESPERA_STATUS: Enviar STATUS?
  ESP_ESPERA_STATUS --> ESP_ENVIA_PRINT: STATUS disponible
  ESP_ESPERA_STATUS --> ESP_IDLE: Ocupado o timeout 3 s
  ESP_ENVIA_PRINT --> ESP_ESPERA_DONE: Enviar PRINT
  ESP_ESPERA_DONE --> ESP_IDLE: DONE con id correcto
  ESP_ESPERA_DONE --> ESP_IDLE: Timeout 10 s (resultado incierto)
```

Los identificadores son los nombres del `enum Estado` definido en [`HexaTour.ino`](../firmware/esp32/HexaTour/HexaTour.ino). El manejo de mensajes incorrectos y reintentos debe estudiarse en el firmware antes de modificar estos estados.

## Estados del Arduino UNO

```mermaid
stateDiagram-v2
  [*] --> Disponible
  Disponible --> Disponible: STATUS? / responder STATUS|1
  Disponible --> Imprimiendo: PRINT con id nuevo
  Disponible --> Disponible: PRINT duplicado / ignorar
  Imprimiendo --> Disponible: Terminar impresión y emitir DONE
```

El UNO ignora una orden si está ocupado o si su `jobId` coincide con el último aceptado. Mientras se ejecuta `imprimirTexto()`, la lectura de mensajes queda bloqueada.

## Estado de la demo

La demo insertada por el empaquetador identifica su modo con `meta[name="hexatour-mode"]`; en desarrollo también puede activarse mediante `?demo=1`. La impresión muestra una confirmación local de simulación, el PDF se deshabilita y urgencias no contacta con nadie. La navegación conserva el modo de demostración.

[Arquitectura](01-arquitectura-general.md) · [Protocolo serial](../firmware/README.md#protocolo-serial-esp32-uno) · [Comportamiento de la demo](Demo.md)
