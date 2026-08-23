#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

const int BTN_1 = 12;
const int BTN_2 = 13;

const int LED_ROJO = 26;

const int BUZZER = 27;

const int SS_PIN = 5;
const int RST_PIN = 4;

LiquidCrystal_I2C lcd(0x27, 16, 2);

MFRC522 rfid(SS_PIN, RST_PIN);

enum Estado{
  INICIO, ERROR_TARJETA, USUARIO, MAQUINA,
  CONFIG_SERIE, CONFIG_DESCANSO, CONFIG_SERIES,
  RESUMEN, CONTADOR, FIN
};

Estado estado        = INICIO;
Estado estadoAnterior = FIN;

struct Usuario {
  String nombre;
  String uid;
};

Usuario usuarios[] = {
  {"Gerardo Gonzalez", "01020304"},
  {"Juan Alonso", "11223344"}
};

Usuario usuarioActual;

int maquina      = 10;
int tiempoSerie  = 60;
int descanso     = 30;
int series       = 3;

unsigned long tiempoTotal    = 0;
unsigned long tiempoRestante = 0;
unsigned long ultimoTick     = 0;
unsigned long tiempoArranque = 0;

const unsigned long ARRANQUE_MS = 300;
bool arrancado = false;
bool cambio    = false;       // <── ahora global

bool lastBtn[2] = {0,0};

// ─────────────────────────────────────────────────────────────────
// UTILIDADES
// ─────────────────────────────────────────────────────────────────

enum TipoPulsacion {
  NINGUNA,
  CORTA,
  LARGA
};

TipoPulsacion leerPulsacion(int pin, int idx) {

  const unsigned long TIEMPO_LARGO = 1000;

  static bool ultimoEstado[2] = {false};
  static unsigned long inicio[2] = {0};
  static bool largaDetectada[2] = {false};

  bool pulsado = (digitalRead(pin) == LOW);

  // Inicio de pulsación
  if (pulsado && !ultimoEstado[idx]) {
    inicio[idx] = millis();
    largaDetectada[idx] = false;
  }

  // Pulsación larga
  if (pulsado &&
      !largaDetectada[idx] &&
      millis() - inicio[idx] >= TIEMPO_LARGO) {

    largaDetectada[idx] = true;
    ultimoEstado[idx] = pulsado;
    return LARGA;
  }

  // Soltar botón
  if (!pulsado && ultimoEstado[idx]) {

    unsigned long duracion = millis() - inicio[idx];

    ultimoEstado[idx] = false;

    if (!largaDetectada[idx] &&
        duracion < TIEMPO_LARGO) {

      return CORTA;
    }
  }

  ultimoEstado[idx] = pulsado;

  return NINGUNA;
}

void ledOn() {
  digitalWrite(LED_ROJO, HIGH);
}

void ledOff() {
  digitalWrite(LED_ROJO, LOW);
}

void escribirFila(int fila, const char* texto){
  char buf[17];
  snprintf(buf,sizeof(buf),"%-16s",texto);
  lcd.setCursor(0,fila);
  lcd.print(buf);
}

void mostrarMMSS(unsigned long seg){
  char buf[17];
  int m = seg/60;
  int s = seg%60;
  snprintf(buf,sizeof(buf),"Tiempo: %02d:%02d  ",m,s);
  lcd.setCursor(0,1);
  lcd.print(buf);
}

void reiniciar(){
  tiempoSerie    = 60;
  descanso       = 30;
  series         = 3;
  tiempoTotal    = 0;
  tiempoRestante = 0;
  noTone(BUZZER);
  ledOff();
  lcd.clear();
  estadoAnterior = FIN;
  estado         = INICIO;
  arrancado      = false;
  tiempoArranque = millis();
}
// Leer UID de tarjeta RFID
String leerUID() {

  if (!rfid.PICC_IsNewCardPresent())
    return "";

  if (!rfid.PICC_ReadCardSerial())
    return "";

  String uid = "";

  for (byte i = 0; i < rfid.uid.size; i++) {

    if (rfid.uid.uidByte[i] < 0x10)
      uid += "0";

    uid += String(rfid.uid.uidByte[i], HEX);
  }

  uid.toUpperCase();

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();

  return uid;
}

// Buscar usuario por UID
bool buscarUsuario(String uidLeido) {

  int cantidad = sizeof(usuarios) / sizeof(usuarios[0]);

  for (int i = 0; i < cantidad; i++) {

    if (usuarios[i].uid == uidLeido) {

      usuarioActual = usuarios[i];
      return true;
    }
  }

  return false;
}
// ─────────────────────────────────────────────────────────────────
// FUNCIONES DE ESTADO
// ─────────────────────────────────────────────────────────────────

void estadoInicio(){
  if(cambio){
    escribirFila(0,"GymTime RFID");
    escribirFila(1,"Acerque tarjeta");
  }

  String uid = leerUID();
  if(uid != ""){
    if(buscarUsuario(uid)){
        estado = USUARIO;
    }else{
      estado = ERROR_TARJETA;
        
    }
}
}

void estadoErrorTarjeta(){
  if(cambio){
    lcd.clear();
    escribirFila(0,"Tarjeta");
    escribirFila(1,"No registrada");
    delay(1500);
    cambio = true;
    estado = INICIO;

}

}

void estadoUsuario(){
  if(cambio){
    ledOn();
    escribirFila(0,"Usuario:");
    escribirFila(1,usuarioActual.nombre.c_str());
  }
  TipoPulsacion btn1 = leerPulsacion(BTN_1, 0);
  if(btn1 == CORTA) estado = MAQUINA;
}






void estadoMaquina(){
  if(cambio){
    char buf[17];
    snprintf(buf,sizeof(buf),"#%d",maquina);
    escribirFila(0,"Maquina");
    escribirFila(1,buf);
  }
  TipoPulsacion btn1 = leerPulsacion(BTN_1, 0);
  if(btn1 == CORTA) estado = CONFIG_SERIE;
}

void estadoConfigSerie(){
  if(cambio) escribirFila(0,"Tiempo Serie:");
  
  TipoPulsacion btn1 = leerPulsacion(BTN_1, 0);
  TipoPulsacion btn2 = leerPulsacion(BTN_2, 1);
  if(btn1 == CORTA && tiempoSerie < 300){ tiempoSerie += 15; cambio = true; }
  if(btn2 == CORTA && tiempoSerie > 15){ tiempoSerie -= 15; cambio = true; }

  if(cambio){
    char buf[17];
    snprintf(buf,sizeof(buf),"%d seg",tiempoSerie);
    escribirFila(1,buf);
  }
  if(btn1 == LARGA) estado = CONFIG_DESCANSO;
}

void estadoConfigDescanso(){
  if(cambio) escribirFila(0,"Descanso:");
  
  TipoPulsacion btn1 = leerPulsacion(BTN_1, 0);
  TipoPulsacion btn2 = leerPulsacion(BTN_2, 1);
  if(btn1 == CORTA && descanso < 300){ descanso += 15; cambio = true; }
  if(btn2 == CORTA && descanso > 0){ descanso -= 15; cambio = true; }
  
  if(cambio){
    char buf[17];
    snprintf(buf,sizeof(buf),"%d seg",descanso);
    escribirFila(1,buf);
  }
  if(btn1 == LARGA) estado = CONFIG_SERIES;
}

void estadoConfigSeries(){
  if(cambio) escribirFila(0,"N Series:");
  TipoPulsacion btn1 = leerPulsacion(BTN_1, 0);
  TipoPulsacion btn2 = leerPulsacion(BTN_2, 1);
  if(btn1 == CORTA && series < 5){ series++; cambio=true; }
  if(btn2 == CORTA && series > 1){ series--; cambio=true; }
  if(cambio){
    char buf[17];
    snprintf(buf,sizeof(buf),"%d series",series);
    escribirFila(1,buf);
  }
  if(btn1 == LARGA){
    tiempoTotal    = ((unsigned long)series * tiempoSerie)
                   + ((unsigned long)(series-1) * descanso);
    tiempoRestante = tiempoTotal;
    estado = RESUMEN;
  }
}

void estadoResumen(){
  if(cambio){
    escribirFila(0,"Total OK?");
    mostrarMMSS(tiempoTotal);
  }
  TipoPulsacion btn1 = leerPulsacion(BTN_1, 0);
  if(btn1 == LARGA){
    ultimoTick = millis();
    estado = CONTADOR;
  }
}

void estadoContador(){
  if(cambio){
    char nombre[17];
    snprintf(nombre,sizeof(nombre),"%-16s",usuarioActual.nombre.c_str());
    lcd.setCursor(0,0);
    lcd.print(nombre);
    mostrarMMSS(tiempoRestante);
    ultimoTick = millis();
  }

  unsigned long transcurrido = millis() - ultimoTick;

  if(transcurrido >= 1000){
    unsigned long seg = transcurrido / 1000;
    ultimoTick += seg * 1000;
    tiempoRestante = (tiempoRestante > seg) ? tiempoRestante - seg : 0;
    mostrarMMSS(tiempoRestante);
    if(tiempoRestante == 0){
      ledOff();
      tone(BUZZER,2500,200);
      estado = FIN;
    }
  }
}

void estadoFin(){
  if(cambio){
    tone(BUZZER,2500,200);
    escribirFila(0,"Sesion finalizada");
    escribirFila(1,"Mantenga Boton 2");
  }
}

// ─────────────────────────────────────────────────────────────────
// SETUP Y LOOP
// ─────────────────────────────────────────────────────────────────

void setup(){
  pinMode(BTN_1,  INPUT_PULLUP);
  pinMode(BTN_2,      INPUT_PULLUP);

  pinMode(BUZZER, OUTPUT);
  pinMode(LED_ROJO,  OUTPUT);

  SPI.begin(18, 19, 23, 5);
  rfid.PCD_Init();

  Wire.begin(21, 22);
  lcd.init();
  lcd.backlight();
  tiempoArranque = millis();
  reiniciar();
}

void loop(){

  // Habilitar botones tras arranque
  if(!arrancado && (millis() - tiempoArranque >= ARRANQUE_MS)){
    arrancado = true;
    lastBtn[0]=(digitalRead(BTN_1) ==LOW);
    lastBtn[1]=(digitalRead(BTN_2) ==LOW);
  }

  TipoPulsacion btn2 = leerPulsacion(BTN_2, 1);
  if(btn2 == LARGA){ reiniciar(); return; }

  cambio = (estado != estadoAnterior);
  if(cambio){ estadoAnterior = estado; lcd.clear(); }

  switch(estado){
    case INICIO:          estadoInicio();          break;
    case ERROR_TARJETA:   estadoErrorTarjeta();    break;
    case USUARIO:         estadoUsuario();         break;
    case MAQUINA:         estadoMaquina();         break;
    case CONFIG_SERIE:    estadoConfigSerie();     break;
    case CONFIG_DESCANSO: estadoConfigDescanso();  break;
    case CONFIG_SERIES:   estadoConfigSeries();    break;
    case RESUMEN:         estadoResumen();         break;
    case CONTADOR:        estadoContador();        break;
    case FIN:             estadoFin();             break;
  }
}

