#include <SoftwareSerial.h>
// #include "Adafruit_Thermal.h"
#include "../librerias/Adafruit_Thermal_Printer_Library/Adafruit_Thermal.h"

// ---- Serial hacia ESP32 ----
#define ESP_RX 10    // UNO RX  <- TX ESP32 (a través de divisor)
#define ESP_TX 11    // UNO TX  -> RX ESP32

// ---- Serial hacia impresora térmica ----
#define PRINTER_RX 2 // UNO RX  <- TX impresora
#define PRINTER_TX 3 // UNO TX  -> RX impresora

// El descuento se calcula en el ESP32 y se envia en el texto

SoftwareSerial link(ESP_RX, ESP_TX);               // Canal UNO <-> ESP32
SoftwareSerial mySerial(PRINTER_RX, PRINTER_TX);   // Canal UNO <-> impresora
Adafruit_Thermal printer(&mySerial);

// ---- Estado ----
bool ocupado   = false;  // true mientras se imprime, false cuando está libre
int  lastJobId = -1;     // último id de trabajo aceptado (para evitar duplicados simples)

String cmdBuffer;

// El ESP32 envia texto con saltos codificados como "\n"; este helper los expande a lineas reales.
void printEncodedLines(const String &textoCodificado) {
  String linea = "";
  for (int i = 0; i < (int)textoCodificado.length(); i++) {
    char c = textoCodificado[i];
    if (c == '\\' && (i + 1) < (int)textoCodificado.length() && textoCodificado[i + 1] == 'n') {
      printer.println(linea);
      linea = "";
      i++;
    } else {
      linea += c;
    }
  }
  if (linea.length() > 0) {
    printer.println(linea);
  }
}

// --- Función de impresión con respeto a saltos de línea ---
void imprimirTexto(const String &textoCodificado) {
  // Cambiamos el "escucha" al puerto de la impresora
  mySerial.listen();

  printer.wake();
  printer.setDefault();

  // 1) Cuerpo principal del ticket (texto desde ESP32)
  printer.justify('L');      // alineado a la izquierda
  printer.setSize('S');      // tamaño pequeño
  printer.boldOn();

  String descuentoMsg = "";
  String linea = "";
  for (int i = 0; i < (int)textoCodificado.length(); i++) {
    char c = textoCodificado[i];
    if (c == '\\' && (i + 1) < (int)textoCodificado.length() && textoCodificado[i + 1] == 'n') {
      if (linea.startsWith("__DESCUENTO__=")) {
        descuentoMsg = linea.substring(String("__DESCUENTO__=").length());
      } else {
        printer.println(linea);
      }
      linea = "";
      i++;
    } else {
      linea += c;
    }
  }

  if (linea.length() > 0) {
    if (linea.startsWith("__DESCUENTO__=")) {
      descuentoMsg = linea.substring(String("__DESCUENTO__=").length());
    } else {
      printer.println(linea);
    }
  }

  printer.boldOff();

  // (opcional) Dejar una línea en blanco antes del mensaje final
  printer.println();

  // 2) Mensaje final de cortesía: derecha + inverso
  printer.justify('C');      // alineado al centro
  printer.setSize('L');      // tamaño pequeño
  printer.inverseOn();
  printer.println(F("GRACIAS POR USAR HEXATOUR"));
  printer.inverseOff();

  if (descuentoMsg.length() > 0) {
    printer.println();
    printer.justify('L');
    printer.setSize('S');
    printer.boldOn();
    printEncodedLines(descuentoMsg);
    printer.boldOff();
  }

  // 3) Alimentar papel y dormir
  printer.feed(3);
  printer.sleep();

  // Al terminar, volvemos a escuchar al ESP32
  link.listen();
}


// --- Procesamiento de mensajes del ESP32 ---
void procesarMensaje(const String &msg) {
  Serial.print("UNO recibio: ");
  Serial.println(msg);

  // Consulta de estado
  if (msg == "STATUS?") {
    int disponible = ocupado ? 0 : 1;
    link.print("STATUS|");
    link.println(disponible);
    Serial.print("UNO -> ESP32: STATUS|");
    Serial.println(disponible);
    return;
  }

  // Orden de impresión: PRINT|id|textoCodificado
  if (msg.startsWith("PRINT|")) {
    int firstSep = msg.indexOf('|', 6); // buscar segundo '|'
    if (firstSep < 0) return;

    String idStr = msg.substring(6, firstSep);
    String texto = msg.substring(firstSep + 1);
    int jobId = idStr.toInt();

    // 1) Si ya hay impresión en curso, SE IGNORA la nueva solicitud
    if (ocupado) {
      Serial.println("UNO: ocupado, se ignora nueva orden PRINT");
      return;
    }

    // 2) Protección básica contra re-envío del mismo id
    if (jobId == lastJobId) {
      Serial.println("UNO: trabajo duplicado (mismo id), se ignora");
      return;
    }

    // 3) Aceptamos el trabajo y marcamos ocupado
    ocupado   = true;
    lastJobId = jobId;

    Serial.print("UNO: imprimiendo trabajo id = ");
    Serial.println(jobId);

    // Ejecutar impresión (bloqueante; no se atienden más mensajes durante esto)
    imprimirTexto(texto);

    // Al terminar, se marca como libre
    ocupado = false;

    // Notificar fin al ESP32
    link.print("DONE|");
    link.println(jobId);
    Serial.print("UNO -> ESP32: DONE|");
    Serial.println(jobId);
  }
}

void setup() {
  // Debug hacia PC
  Serial.begin(115200);

  // Enlace hacia ESP32
  link.begin(9600);

  // Enlace hacia impresora
  mySerial.begin(9600);

  // Inicialización impresora: primero escuchar a la impresora
  mySerial.listen();
  delay(3000);
  printer.begin();

  // Por defecto, escuchar al ESP32
  link.listen();


  Serial.println("UNO: listo, impresora inicializada");
}

void loop() {
  // Lectura de comandos desde el ESP32
  if (link.isListening()) {
    while (link.available()) {
      char c = link.read();
      if (c == '\n') {
        cmdBuffer.trim();
        if (cmdBuffer.length() > 0) {
          procesarMensaje(cmdBuffer);
        }
        cmdBuffer = "";
      } else {
        cmdBuffer += c;
      }
    }
  }
}
