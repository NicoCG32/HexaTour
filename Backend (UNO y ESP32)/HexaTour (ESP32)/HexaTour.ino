#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
// #include <LiquidCrystal_I2C.h>
// #include <ArduinoJson.h>
#include "../librerias/LiquidCrystal_I2C/LiquidCrystal_I2C.h"
#include "../librerias/ArduinoJson/ArduinoJson.h"

#define DNS_PORT 53
#define SERIAL_BAUD 115200

const char* AP_SSID = "HexaTour";
const char* AP_PASS = "hexatour123";

// Ahora (ESP32-S3, SPI3 por defecto)
const int PIN_SCK  = 12;
const int PIN_MISO = 13;
const int PIN_MOSI = 11;
const int PIN_CS   = 10;

const char* MAIN_USER = "operator";
const char* MAIN_PASS = "HexaTour2025!";

DNSServer dns;
WebServer server(80);
bool sd_ok = false;

static const char* START_FILE = "/www/visitor/index.html";

// --------- LCD 16x2 I2C (solo estados) ---------
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Dirección típica 0x27

// --------- Comunicación con Arduino UNO (impresora) ---------
#define RXD2 16  // ESP32 RX2  <- UNO TX (11, con divisor)
#define TXD2 17  // ESP32 TX2  -> UNO RX (10)

// Protocolo serial: mensajes de una linea, separados por '|'. El texto codifica saltos como "\n".

// Máquina de estados para la impresora
enum Estado {
  ESP_IDLE,
  ESP_PREGUNTA_STATUS,
  ESP_ESPERA_STATUS,
  ESP_ENVIA_PRINT,
  ESP_ESPERA_DONE
};

Estado estado = ESP_IDLE;
unsigned long t0 = 0;
const unsigned long TIMEOUT = 3000;        // timeout para STATUS (ms)
const unsigned long TIMEOUT_DONE = 10000;  // timeout para DONE  (ms)

uint32_t nextJobId = 1;      // contador global de trabajos
uint32_t currentJobId = 0;   // id del trabajo en curso
String currentJobText = "";  // texto del trabajo actual
String rxBuffer = "";        // buffer de recepción desde el UNO

// --------- Prototipos ---------
String contentType(const String& path);
bool isSafePath(const String& p);
bool streamFileWithCache(File& file, const String& ctype, bool cache = true);
bool tryServePath(String path, bool cache = true);
void listDir(const char* dirname, uint8_t levels);
bool readFileToString(const char* path, String& out, size_t maxLen = 8192);
String readWholeFile(const String& path);
void sanitizeSegment(String& value);
int discountForCategory(const String& category);
String buildDiscountMessage(int discount);
bool parsePoiRef(const String& fileParam, String& category, String& slug);
bool loadPoiFromDb(const String& category, const String& slug, String& name, String& routeText, String& routeImg);
bool deriveImageFromTxtFile(const String& fileParam, String& folder, String& slug, String& imgPath);
bool readJpegDims(const char* path, int& w, int& h, int& comps);
bool findLogoJpeg(String& logoPath, int& w, int& h, int& comps, size_t& len);
String pdfEscape(String s);

bool checkMainAuth();
void requestAuth();
void handleFileRequest();
void redirectToRoot();
void handlePrintRuta();
void handleApiRoutePdf();
void handleMainRoot();

// LCD estados
void lcdShowStatus(const String& l1, const String& l2 = "");

// UNO / impresora
void enviarLinea(const String& s);
void procesarMensaje(const String& msg);
void handleSerialFromUno();
void handlePrinterStateMachine();

// Decorativo: Animación de cargando
void lcdBootAnimationRandom() {
  const String titulo = "    HexaTour    ";  // 16 caracteres centrados
  int porcentaje = 0;

  // Mostrar un 0% inicial
  lcdShowStatus(titulo, "Cargando   0%");
  delay(500);

  // Mientras no lleguemos a 99, vamos sumando pasos aleatorios
  while (porcentaje < 99) {
    // Paso aleatorio entre 5 y 25 (ajustable)
    int paso = random(5, 26);   // random(5,26) -> [5,25]

    if (porcentaje + paso >= 99) {
      porcentaje = 99;          // forzar llegada a 99
    } else {
      porcentaje += paso;
    }

    String linea2 = "  Cargando " + String(porcentaje) + "%";
    lcdShowStatus(titulo, linea2);

    // Pausa entre “saltos” (ajustable)
    delay(500);
  }

  // Mensaje final “bonito”
  lcdShowStatus(titulo, "      Listo     ");
  delay(800);
}

// ====================== setup / loop ======================
void setup() {
  Serial.begin(SERIAL_BAUD);
  delay(500);

  // WiFi AP
  WiFi.mode(WIFI_AP);
  WiFi.softAP(AP_SSID, AP_PASS);
  IPAddress apIP = WiFi.softAPIP();
  Serial.printf("\nAP SSID: %s\nAP IP: %s\n", AP_SSID, apIP.toString().c_str());

  // SPI + SD
  pinMode(PIN_CS, OUTPUT);
  digitalWrite(PIN_CS, HIGH);
  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_CS);
  sd_ok = SD.begin(PIN_CS, SPI, 1000000);

  if (sd_ok) {
    bool hasVisitor = SD.exists(START_FILE);
    bool hasIndex = SD.exists("/www/index.html");
    (void)hasVisitor;
    (void)hasIndex;
  } else {
    Serial.println("⚠️ SD no montada");
    lcdShowStatus("Error SD", "no montada");
  }

  // DNS cautivo
  dns.start(DNS_PORT, "*", apIP);

  // HTTP

  // APIs
  server.on("/api/print-ruta", HTTP_GET, handlePrintRuta);
  server.on("/api/route-pdf", HTTP_GET, handleApiRoutePdf);

  // Raíces
  server.on("/", HTTP_GET, handleFileRequest);
  server.on("/main", HTTP_GET, handleMainRoot);
  server.onNotFound(handleFileRequest);

  // Endpoints de detección cautiva -> redirigir al portal visitante
  server.on("/generate_204", HTTP_GET, redirectToRoot);  // Android
  server.on("/gen_204", HTTP_GET, redirectToRoot);
  server.on("/hotspot-detect.html", HTTP_GET, redirectToRoot);  // Apple
  server.on("/ncsi.txt", HTTP_GET, redirectToRoot);             // Windows
  server.on("/connecttest.txt", HTTP_GET, redirectToRoot);      // Windows
  server.on("/success.txt", HTTP_GET, redirectToRoot);          // Firefox

  server.begin();
  Serial.println("HTTP listo.");

  // Serial2 hacia Arduino UNO (impresora)
  Serial2.begin(9600, SERIAL_8N1, RXD2, TXD2);
  delay(500);
  Serial.println("UART con UNO listo.");

  // --- LCD I2C: SDA=21, SCL=22 en ESP32 ---
  // Ahora (ESP32-S3)
  Wire.begin(8, 9);  // SDA=8, SCL=9

  lcd.init();
  lcd.backlight();
  lcd.clear();

  // Semilla para números aleatorios (pin analógico flotante)
  randomSeed(analogRead(4));

  // Animación de arranque
  lcdBootAnimationRandom();

  estado = ESP_IDLE;
  currentJobText = "";
  lcdShowStatus("    HexaTour    ", "Listo para usar");
}

void loop() {
  dns.processNextRequest();
  server.handleClient();

  // Comunicación con el UNO (impresora)
  handleSerialFromUno();
  handlePrinterStateMachine();
}

// ====================== LCD: mostrar estados ======================
void lcdShowStatus(const String& l1, const String& l2) {
  String line1 = l1;
  String line2 = l2;

  if (line1.length() > 16) line1 = line1.substring(0, 16);
  if (line2.length() > 16) line2 = line2.substring(0, 16);

  while (line1.length() < 16) line1 += ' ';
  while (line2.length() < 16) line2 += ' ';

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(line1);
  lcd.setCursor(0, 1);
  lcd.print(line2);
}

// ====================== Comunicación con UNO ======================
void enviarLinea(const String& s) {
  Serial2.println(s);
  Serial.print("ESP32 -> UNO: ");
  Serial.println(s);
}

void procesarMensaje(const String& msg) {
  Serial.print("ESP32 recibio: ");
  Serial.println(msg);

  if (msg.startsWith("STATUS|") && estado == ESP_ESPERA_STATUS) {
    int disponible = msg.substring(7).toInt();

    if (disponible == 1 && currentJobText.length() > 0) {
      // Arduino está libre, pasamos a enviar el trabajo
      estado = ESP_ENVIA_PRINT;
      lcdShowStatus("Impresora", "disponible");
    } else {
      // Arduino ocupado o no hay trabajo
      Serial.println("ESP32: UNO ocupado o sin trabajo, se cancela esta solicitud.");
      lcdShowStatus("Impresora", "ocupada");
      delay(5000);
      // Cancelamos el trabajo actual
      currentJobText = "";
      currentJobId = 0;
      estado = ESP_IDLE;
    }
  } else if (msg.startsWith("DONE|") && estado == ESP_ESPERA_DONE) {
    int id = msg.substring(5).toInt();
    if (id == (int)currentJobId) {
      Serial.println("ESP32: impresion completada correctamente.");
      lcdShowStatus("Retire su ticket", " Tenga buen día ");
      delay(10000);
      lcdShowStatus("  HexaTour  ", "Listo para Usar");
      // Trabajo terminado
      currentJobText = "";
      currentJobId = 0;
      estado = ESP_IDLE;
    } else {
      Serial.println("ESP32: DONE con id inesperado.");
    }
  }
}

void handleSerialFromUno() {
  while (Serial2.available()) {
    char c = Serial2.read();
    if (c == '\n') {
      rxBuffer.trim();
      if (rxBuffer.length() > 0) {
        procesarMensaje(rxBuffer);
      }
      rxBuffer = "";
    } else if (c != '\r') {
      rxBuffer += c;
    }
  }
}

void handlePrinterStateMachine() {
  switch (estado) {
    case ESP_IDLE:
      // Nada que hacer si no hay trabajo pendiente
      break;

    case ESP_PREGUNTA_STATUS:
      // Lanzamos una sola consulta de estado
      enviarLinea("STATUS?");
      estado = ESP_ESPERA_STATUS;
      t0 = millis();
      break;

    case ESP_ESPERA_STATUS:
      if (millis() - t0 > TIMEOUT) {
        Serial.println("ESP32: timeout esperando STATUS, se cancela esta impresion.");
        lcdShowStatus("Error impresora", "sin respuesta");
        currentJobText = "";
        currentJobId = 0;
        estado = ESP_IDLE;
      }
      break;

    case ESP_ENVIA_PRINT:
      {
        // Construimos el comando PRINT|id|texto
        String cmd = "PRINT|" + String(currentJobId) + "|" + currentJobText;
        enviarLinea(cmd);
        lcdShowStatus("Tratando ticket", "en impresora.");
        delay(2000);
        lcdShowStatus("Tratando ticket", "en impresora..");
        delay(2000);
        lcdShowStatus("Tratando ticket", "en impresora...");

        estado = ESP_ESPERA_DONE;
        t0 = millis();
        break;
      }

    case ESP_ESPERA_DONE:
      if (millis() - t0 > TIMEOUT_DONE) {
        Serial.println("ESP32: timeout esperando DONE, no se sabe si termino la impresion.");
        lcdShowStatus("Error impresora", "timeout DONE");
        // Dejamos el sistema libre igualmente
        currentJobText = "";
        currentJobId = 0;
        estado = ESP_IDLE;
      }
      break;
  }
}

// ====================== Auth MAIN ======================
bool checkMainAuth() {
  if (!server.authenticate(MAIN_USER, MAIN_PASS)) {
    requestAuth();
    return false;
  }
  return true;
}

void requestAuth() {
  server.requestAuthentication(BASIC_AUTH, "HexaTour Main", "Acceso restringido");
}

// ====================== Utilidades ======================
String contentType(const String& path) {
  if (path.endsWith(".html")) return "text/html; charset=UTF-8";
  if (path.endsWith(".css")) return "text/css";
  if (path.endsWith(".js")) return "application/javascript";
  if (path.endsWith(".json")) return "application/json; charset=UTF-8";
  if (path.endsWith(".png")) return "image/png";
  if (path.endsWith(".jpg") || path.endsWith(".jpeg")) return "image/jpeg";
  if (path.endsWith(".svg")) return "image/svg+xml";
  if (path.endsWith(".ico")) return "image/x-icon";
  if (path.endsWith(".webmanifest")) return "application/manifest+json";
  if (path.endsWith(".woff2")) return "font/woff2";
  if (path.endsWith(".pdf")) return "application/pdf";
  if (path.endsWith(".txt")) return "text/plain; charset=UTF-8";
  return "application/octet-stream";
}

bool isSafePath(const String& p) {
  if (p.indexOf("..") >= 0) return false;
  if (p.indexOf('\\') >= 0) return false;
  return true;
}

bool streamFileWithCache(File& file, const String& ctype, bool cache) {
  if (cache) server.sendHeader("Cache-Control", "public, max-age=86400");
  size_t sent = server.streamFile(file, ctype);
  file.close();
  return sent > 0;
}

// Versión SIN .gz
bool tryServePath(String path, bool cache) {
  if (!sd_ok) {
    sd_ok = SD.begin(PIN_CS, SPI, 1000000);
    if (!sd_ok) return false;
  }
  if (!isSafePath(path)) return false;

  if (!SD.exists(path)) return false;
  File f = SD.open(path, "r");
  if (!f) return false;
  return streamFileWithCache(f, contentType(path), cache);
}

// Arreglo: construir ruta completa al recursar
void listDir(const char* dirname, uint8_t levels) {
  File root = SD.open(dirname);
  if (!root) {
    Serial.println("No se pudo abrir dir");
    return;
  }
  if (!root.isDirectory()) {
    Serial.println("No es un directorio");
    return;
  }

  File file = root.openNextFile();
  while (file) {
    if (file.isDirectory()) {
      Serial.print("DIR : ");
      Serial.println(file.name());
      if (levels) {
        String sub = String(dirname);
        if (!sub.endsWith("/")) sub += "/";
        sub += file.name();
        listDir(sub.c_str(), levels - 1);
      }
    } else {
      Serial.print("FILE: ");
      Serial.print(file.name());
      Serial.print("  SIZE: ");
      Serial.println(file.size());
    }
    file = root.openNextFile();
  }
}

bool readFileToString(const char* path, String& out, size_t maxLen) {
  File f = SD.open(path, FILE_READ);
  if (!f) return false;
  out = "";
  while (f.available()) {
    out += (char)f.read();
    if (out.length() > (int)maxLen) break;
  }
  f.close();
  return true;
}

String readWholeFile(const String& path) {
  File f = SD.open(path, "r");
  if (!f) return "";
  String out;
  out.reserve(f.size() + 16);
  while (f.available()) out += (char)f.read();
  f.close();
  return out;
}

int discountForCategory(const String& category) {
  if (category == "campings" || category == "hospedajes") {
    return random(1, 4);
  }
  if (category == "servicios" || category == "ferias" || category == "restaurantes") {
    return random(5, 8);
  }
  return 0;
}

String buildDiscountMessage(int discount) {
  if (discount <= 0) return "";
  return "Haz ganado un descuento de " + String(discount) + "%\\nMuestra el ticket en la tienda";
}

void sanitizeSegment(String& value) {
  value.replace("..", "");
  value.replace("\\", "");
  value.replace("/", "");
}

bool parsePoiRef(const String& fileParam, String& category, String& slug) {
  int slash = fileParam.indexOf('/');
  if (slash <= 0) return false;
  category = fileParam.substring(0, slash);
  slug = fileParam.substring(slash + 1);
  sanitizeSegment(category);
  sanitizeSegment(slug);
  return category.length() > 0 && slug.length() > 0;
}

bool loadPoiFromDb(const String& category, const String& slug, String& name, String& routeText, String& routeImg) {
  String path = "/www/db/poi/" + category + "/" + slug + ".json";
  String json;
  if (!SD.exists(path) || !readFileToString(path.c_str(), json, 20000)) {
    return false;
  }

  DynamicJsonDocument doc(12288);
  DeserializationError err = deserializeJson(doc, json);
  if (err) return false;

  name = doc["name"].as<String>();
  routeText = doc["route"]["text"].as<String>();
  routeImg = doc["images"]["route"].as<String>();
  return true;
}

// ====================== Navegación ======================
void handleMainRoot() {
  if (!checkMainAuth()) return;
  server.sendHeader("Location", "/main/");
  server.send(302, "text/plain", "");
}

// / => /visitor/index.html (home directa al portal visitante)
void handleFileRequest() {
  String uri = server.uri();

  if (uri == "/") {
    uri = "/visitor/index.html";
  } else if (uri == "/main") {
    if (!checkMainAuth()) return;
    uri = "/main/";
  } else if (uri.endsWith("/")) {
    uri += "index.html";
  }
  if (!uri.startsWith("/")) uri = "/" + uri;

  if (uri.startsWith("/main/")) {
    if (!checkMainAuth()) return;
  }

  String full = "/www" + uri;
  bool isHome = (uri == "/visitor/index.html" || uri == "/index.html" || uri == "/");

  if (tryServePath(full, !isHome)) return;
  if (tryServePath(START_FILE, false)) return;
  if (tryServePath("/www/index.html", false)) return;

  server.send(404, "text/plain; charset=UTF-8", "404 Not Found: " + uri + "\nEsperado en SD: /www" + uri);
}

// Abrir portal automáticamente en la ventana cautiva
void redirectToRoot() {
  server.sendHeader("Location", String("http://") + WiFi.softAPIP().toString() + "/visitor/");
  server.send(302, "text/plain", "");
}

// ====================== APIs ======================
// API de impresión: lee ruta desde SD y lanza trabajo hacia el UNO
void handlePrintRuta() {
  // Si ya hay un trabajo en curso, no aceptamos otro
  if (estado != ESP_IDLE) {
    server.send(409, "text/plain; charset=UTF-8", "printer busy");
    return;
  }

  if (!sd_ok) {
    sd_ok = SD.begin(PIN_CS, SPI, 4000000);
  }
  if (!sd_ok) {
    server.send(500, "text/plain; charset=UTF-8", "SD error");
    lcdShowStatus("Error SD", "no montada");
    return;
  }

  String name = server.hasArg("name") ? server.arg("name") : "";
  String category = server.hasArg("cat") ? server.arg("cat") : "";
  String slug = server.hasArg("slug") ? server.arg("slug") : "";
  String file = server.hasArg("file") ? server.arg("file") : "";

  if ((category == "" || slug == "") && file.length()) {
    parsePoiRef(file, category, slug);
  }
  sanitizeSegment(category);
  sanitizeSegment(slug);
  if (category == "" || slug == "") {
    server.send(400, "text/plain; charset=UTF-8", "cat y slug requeridos");
    return;
  }

  String dbName, routeText, routeImg;
  if (!loadPoiFromDb(category, slug, dbName, routeText, routeImg)) {
    server.send(404, "text/plain; charset=UTF-8", "poi no encontrado");
    lcdShowStatus("Ruta no", "encontrada");
    return;
  }
  if (name.length() == 0) name = dbName;
  if (routeText.length() == 0) {
    server.send(404, "text/plain; charset=UTF-8", "ruta no encontrada");
    lcdShowStatus("Ruta no", "encontrada");
    return;
  }

  // === Construir el texto a enviar al UNO ===
  //  - Se conservan los saltos de línea del TXT,
  //    pero codificados como la secuencia "\n" para no romper el protocolo.
  //  - Se evita el carácter '|' porque es separador de campos.

  // 1) Normalizar saltos de línea en el cuerpo
  String body = routeText;
  body.replace("\r\n", "\n");
  body.replace("\r", "\n");

  // 2) Evitar el separador de protocolo
  body.replace("|", "/");

  // 3) Codificar cada salto de línea real como la secuencia "\n"
  body.replace("\n", "\\n");

  body.trim();

  // 4) Preparar el texto completo, anteponiendo la línea de título "Ruta: <name>"
  String texto = body;
  if (name.length()) {
    String safeName = name;
    safeName.replace("|", "/");  // por seguridad, también aquí
    // Título en una línea propia
    texto = "Ruta: " + safeName + "\\n" + texto;
  }

  // 4.1) Descuento dinámico por categoría (se imprime despues del mensaje final)
  int discount = discountForCategory(category);
  String discountMsg = buildDiscountMessage(discount);
  if (discountMsg.length()) {
    texto += "\\n__DESCUENTO__=" + discountMsg;
  }

  // 5) Limitar longitud para no saturar el buffer del UNO
  const size_t MAX_JOB_LEN = 800;
  if (texto.length() > MAX_JOB_LEN) {
    texto = texto.substring(0, MAX_JOB_LEN);
  }

  currentJobText = texto;
  currentJobId = nextJobId++;
  if (nextJobId == 0) nextJobId = 1;  // evitar 0 por overflow

  Serial.println(F("=== HEXATOUR PRINT REQUEST ==="));
  if (name.length()) {
    Serial.print(F("Lugar: "));
    Serial.println(name);
  }
  Serial.print(F("Archivo: "));
  Serial.println(String("/www/db/poi/") + category + "/" + slug + ".json");
  Serial.print(F("JobId: "));
  Serial.println(currentJobId);
  Serial.println(F("Texto codificado (truncado si era largo):"));
  Serial.println(currentJobText);
  Serial.println(F("================================"));

  // Lanzamos la máquina de estados: preguntar STATUS al UNO
  estado = ESP_PREGUNTA_STATUS;
  t0 = millis();

  // Respuesta inmediata al cliente HTTP: el trabajo fue aceptado
  server.send(200, "text/plain; charset=UTF-8", "print job accepted");
}


bool deriveImageFromTxtFile(const String& fileParam, String& folder, String& slug, String& imgPath) {
  folder = "";
  slug = "";
  int slash = fileParam.indexOf('/');
  if (slash > 0) folder = fileParam.substring(0, slash);

  int i1 = fileParam.indexOf("indicaciones");
  int i2 = fileParam.lastIndexOf("ruta.txt");
  if (i1 < 0 || i2 <= i1) return false;

  slug = fileParam.substring(i1 + String("indicaciones").length(), i2);
  slug.toLowerCase();
  slug.replace("\\", "");
  slug.replace("/", "");

  imgPath = "/www/img/";
  if (folder.length()) imgPath += folder + "/";
  imgPath += "ruta" + slug + ".jpg";
  return true;
}

// --- JPEG dims
bool readJpegDims(const char* path, int& w, int& h, int& comps) {
  File f = SD.open(path, "r");
  if (!f) return false;
  auto rf = [&]() {
    int c = f.read();
    return c;
  };
  int b = rf();
  if (b != 0xFF) {
    f.close();
    return false;
  }
  b = rf();
  if (b != 0xD8) {
    f.close();
    return false;
  }

  while (f.available()) {
    int m1 = rf();
    if (m1 != 0xFF) continue;
    int mk = rf();
    if (mk < 0) break;
    while (mk == 0xFF) mk = rf();
    if (mk == 0xC0 || mk == 0xC1 || mk == 0xC2) {
      int lh = rf();
      int ll = rf();
      (void)lh;
      (void)ll;
      int prec = rf();
      (void)prec;
      int hh = rf();
      int hl = rf();
      int wh = rf();
      int wl = rf();
      int ncomp = rf();
      if (hh < 0 || hl < 0 || wh < 0 || wl < 0 || ncomp < 0) {
        f.close();
        return false;
      }
      h = (hh << 8) | hl;
      w = (wh << 8) | wl;
      comps = ncomp;
      f.close();
      return (w > 0 && h > 0);
    } else if (mk == 0xDA) {
      break;
    } else {
      int lh = rf();
      int ll = rf();
      if (lh < 0 || ll < 0) {
        f.close();
        return false;
      }
      int len = (lh << 8) | ll;
      if (len < 2) {
        f.close();
        return false;
      }
      size_t pos = f.position();
      f.seek(pos + (len - 2));
    }
  }
  f.close();
  return false;
}

bool findLogoJpeg(String& logoPath, int& w, int& h, int& comps, size_t& len) {
  const char* CANDIDATES[] = { "/www/img/map/logo.jpg", "/www/img/map/logo.jpeg" };
  for (auto c : CANDIDATES) {
    if (SD.exists(c)) {
      logoPath = String(c);
      if (!readJpegDims(logoPath.c_str(), w, h, comps)) return false;
      File f = SD.open(logoPath, "r");
      if (!f) return false;
      len = f.size();
      f.close();
      return true;
    }
  }
  return false;
}

String pdfEscape(String s) {
  s.replace("\\", "\\\\");
  s.replace("(", "\\(");
  s.replace(")", "\\)");
  return s;
}

// --- PDF inline (dl=0 inline / dl=1 attachment)
void handleApiRoutePdf() {
  String name = server.hasArg("name") ? server.arg("name") : "";
  String file = server.hasArg("file") ? server.arg("file") : "";
  String category = server.hasArg("cat") ? server.arg("cat") : "";
  String slug = server.hasArg("slug") ? server.arg("slug") : "";
  String extra = server.hasArg("extra") ? server.arg("extra") : "";
  if ((category == "" || slug == "") && file.length()) {
    parsePoiRef(file, category, slug);
  }
  sanitizeSegment(category);
  sanitizeSegment(slug);
  if (category == "" || slug == "") {
    server.send(400, "text/plain; charset=UTF-8", "cat y slug requeridos");
    return;
  }
  String dbName, routeText, routeImg;
  if (!loadPoiFromDb(category, slug, dbName, routeText, routeImg)) {
    server.send(404, "text/plain; charset=UTF-8", "poi no encontrado");
    return;
  }
  if (name.length() == 0) name = dbName;

  String body = routeText;
  if (body == "") {
    server.send(404, "text/plain; charset=UTF-8", "ruta no encontrada");
    return;
  }
  body.replace("\r", "\n");
  if (body.length() > 8000) body = body.substring(0, 8000);

  String routeImgPath;
  bool hasRouteImg = false;
  if (routeImg.length()) {
    routeImgPath = routeImg;
    if (!routeImgPath.startsWith("/")) routeImgPath = "/www/" + routeImgPath;
    hasRouteImg = SD.exists(routeImgPath);
  }
  int routeW = 0, routeH = 0, routeComps = 3;
  size_t routeLen = 0;
  if (hasRouteImg) {
    if (!readJpegDims(routeImgPath.c_str(), routeW, routeH, routeComps)) hasRouteImg = false;
    else {
      File fi = SD.open(routeImgPath, "r");
      if (fi) {
        routeLen = fi.size();
        fi.close();
      } else hasRouteImg = false;
    }
  }

  String logoPath;
  int logoW = 0, logoH = 0, logoComps = 3;
  size_t logoLen = 0;
  bool hasLogo = findLogoJpeg(logoPath, logoW, logoH, logoComps, logoLen);

  String header = "%PDF-1.4\n%\xE2\xE3\xCF\xD3\n";
  String o1 = "1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n";
  String o2 = "2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n";

  String res;
  if (hasRouteImg && hasLogo)
    res = "<< /Font << /F1 5 0 R >> /XObject << /Im1 6 0 R /Lg1 7 0 R >> >>";
  else if (hasRouteImg)
    res = "<< /Font << /F1 5 0 R >> /XObject << /Im1 6 0 R >> >>";
  else if (hasLogo)
    res = "<< /Font << /F1 5 0 R >> /XObject << /Lg1 6 0 R >> >>";
  else
    res = "<< /Font << /F1 5 0 R >> >>";

  String o3 = "3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources " + res + " >> endobj\n";

  float maxW = 495.0f, maxH = 350.0f;
  float drawW = 0, drawH = 0;

  int imgX = 50, imgY = 250;  // más abajo en la página

  if (hasRouteImg && routeW > 0 && routeH > 0) {
    float s = min(maxW / (float)routeW, maxH / (float)routeH);
    drawW = routeW * s;
    drawH = routeH * s;
  }

  float logoDW = 0, logoDH = 0;
  int logoX = 0, logoY = 0;
  if (hasLogo && logoW > 0 && logoH > 0) {
    float lw = 64.0f;
    float s = lw / (float)logoW;
    logoDW = lw;
    logoDH = logoH * s;
    logoX = (int)(595.0f - 50.0f - logoDW);
    logoY = (int)(842.0f - 50.0f - logoDH);
  }

  String content;
  content.reserve(22000);
  content += "BT\n";
  content += "/F1 18 Tf 50 800 Td (" + pdfEscape("Ruta: " + name) + ") Tj\n";
  content += "/F1 12 Tf 0 -28 Td (" + pdfEscape("Indicaciones:") + ") Tj\n";
  content += "0 -18 Td\n";

  int ycount = 0, maxLines = hasRouteImg ? 24 : 38;
  int lineStart = 0;
  while (lineStart < (int)body.length() && ycount < maxLines) {
    int nl = body.indexOf('\n', lineStart);
    String line = (nl < 0) ? body.substring(lineStart) : body.substring(lineStart, nl);
    if (line.length() == 0) line = " ";
    content += "(" + pdfEscape(line) + ") Tj\n";
    content += "0 -14 Td\n";
    ycount++;
    if (nl < 0) break;
    lineStart = nl + 1;
  }

  if (extra.length()) {
    content += "0 -10 Td\n";
    content += "/F1 12 Tf (" + pdfEscape("Consejo adicional:") + ") Tj\n";
    content += "0 -14 Td\n";
    content += "(" + pdfEscape(extra) + ") Tj\n";
  }
  content += "ET\n";

  if (hasRouteImg) {
    char buf[256];
    snprintf(buf, sizeof(buf), "q %.2f 0 0 %.2f %d %d cm /Im1 Do Q\n", drawW, drawH, imgX, imgY);
    content += buf;
  }
  if (hasLogo) {
    char buf[256];
    snprintf(buf, sizeof(buf), "q %.2f 0 0 %.2f %d %d cm /Lg1 Do Q\n", logoDW, logoDH, logoX, logoY);
    content += buf;
  }

  String o4 = "4 0 obj << /Length " + String(content.length()) + " >> stream\n" + content + "endstream\nendobj\n";
  String o5 = "5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n";

  String o6_head, o6_tail, o7_head, o7_tail;
  if (hasRouteImg) {
    String cs = (routeComps == 1) ? "/DeviceGray" : "/DeviceRGB";
    o6_head = "6 0 obj << /Type /XObject /Subtype /Image /Width " + String(routeW) + " /Height " + String(routeH) + " /ColorSpace " + cs + " /BitsPerComponent 8 /Filter /DCTDecode /Length " + String((unsigned long)routeLen) + " >> stream\n";
    o6_tail = "endstream\nendobj\n";
  }
  if (hasLogo) {
    String cs = (logoComps == 1) ? "/DeviceGray" : "/DeviceRGB";
    if (hasRouteImg) {
      o7_head = "7 0 obj << /Type /XObject /Subtype /Image /Width " + String(logoW) + " /Height " + String(logoH) + " /ColorSpace " + cs + " /BitsPerComponent 8 /Filter /DCTDecode /Length " + String((unsigned long)logoLen) + " >> stream\n";
      o7_tail = "endstream\nendobj\n";
    } else {
      o6_head = "6 0 obj << /Type /XObject /Subtype /Image /Width " + String(logoW) + " /Height " + String(logoH) + " /ColorSpace " + cs + " /BitsPerComponent 8 /Filter /DCTDecode /Length " + String((unsigned long)logoLen) + " >> stream\n";
      o6_tail = "endstream\nendobj\n";
    }
  }

  uint32_t cur = header.length();
  uint32_t off1 = cur;
  cur += o1.length();
  uint32_t off2 = cur;
  cur += o2.length();
  uint32_t off3 = cur;
  cur += o3.length();
  uint32_t off4 = cur;
  cur += o4.length();
  uint32_t off5 = cur;
  cur += o5.length();
  uint32_t off6 = 0, off7 = 0;

  if (o6_head.length()) {
    off6 = cur;
    cur += o6_head.length();
    size_t bin6 = (hasRouteImg ? routeLen : (hasLogo && !hasRouteImg ? logoLen : 0));
    cur += bin6;
    cur += o6_tail.length();
  }
  if (o7_head.length()) {
    off7 = cur;
    cur += o7_head.length();
    size_t bin7 = (hasLogo && hasRouteImg) ? logoLen : 0;
    cur += bin7;
    cur += o7_tail.length();
  }

  String xref = "xref\n0 " + String(6 + (off6 ? 1 : 0) + (off7 ? 1 : 0)) + "\n";
  auto addX = [&](uint32_t off) {
    char b[32];
    sprintf(b, "%010lu 00000 n \n", (unsigned long)off);
    xref += b;
  };
  xref += "0000000000 65535 f \n";
  addX(off1);
  addX(off2);
  addX(off3);
  addX(off4);
  addX(off5);
  if (off6) addX(off6);
  if (off7) addX(off7);
  uint32_t xrefOffset = cur;
  String trailer = "trailer << /Size " + String(6 + (off6 ? 1 : 0) + (off7 ? 1 : 0)) + " /Root 1 0 R >>\nstartxref\n" + String(xrefOffset) + "\n%%EOF\n";

  size_t totalLen = header.length() + o1.length() + o2.length() + o3.length() + o4.length() + o5.length()
                    + (off6 ? (o6_head.length() + (hasRouteImg ? routeLen : (hasLogo && !hasRouteImg ? logoLen : 0)) + o6_tail.length()) : 0)
                    + (off7 ? (o7_head.length() + (hasLogo && hasRouteImg ? logoLen : 0) + o7_tail.length()) : 0)
                    + xref.length() + trailer.length();

  String filename = "ruta";
  if (slug.length()) filename += "-" + slug;
  filename += ".pdf";

  bool attach = server.hasArg("dl") ? (server.arg("dl").toInt() != 0) : false;
  String disp = String(attach ? "attachment" : "inline");
  server.sendHeader("Content-Disposition", disp + "; filename=\"" + filename + "\"");
  server.sendHeader("Cache-Control", "no-store");
  server.setContentLength(totalLen);
  server.send(200, "application/pdf", "");

  // stream
  server.sendContent(header);
  server.sendContent(o1);
  server.sendContent(o2);
  server.sendContent(o3);
  server.sendContent(o4);
  server.sendContent(o5);

  if (off6) {
    server.sendContent(o6_head);
    const char* path6 = nullptr;
    if (hasRouteImg) path6 = routeImgPath.c_str();
    else if (hasLogo && !hasRouteImg) path6 = logoPath.c_str();
    if (path6) {
      File f6 = SD.open(path6, "r");
      if (f6) {
        uint8_t buf2[1024];
        while (f6.available()) {
          size_t n = f6.read(buf2, sizeof(buf2));
          if (n) server.client().write(buf2, n);
        }
        f6.close();
      }
    }
    server.sendContent(o6_tail);
  }
  if (off7) {
    server.sendContent(o7_head);
    File f7 = SD.open(logoPath, "r");
    if (f7) {
      uint8_t buf3[1024];
      while (f7.available()) {
        size_t n = f7.read(buf3, sizeof(buf3));
        if (n) server.client().write(buf3, n);
      }
      f7.close();
    }
    server.sendContent(o7_tail);
  }

  server.sendContent(xref);
  server.sendContent(trailer);
}
