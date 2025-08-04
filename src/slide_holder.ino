const int X_PIN   = 2;
const int Y_PIN = 3;
const int X_DIR_PIN = 5;   
const int Y_DIR_PIN = 6;
const int ENABLE_PIN = 8;   
const int L_PIN = 52;
const int R_PIN = 50;
const int U_PIN = 48;
const int D_PIN = 46;

const int PULSE_US = 100;


void setup() {
  Serial.begin(9600);
  pinMode(X_PIN,   OUTPUT);
  pinMode(X_DIR_PIN,    OUTPUT);
  pinMode(Y_PIN,     OUTPUT);
  pinMode(Y_DIR_PIN, OUTPUT);
  pinMode(ENABLE_PIN, OUTPUT);

  pinMode(L_PIN, INPUT_PULLUP);
  pinMode(R_PIN, INPUT_PULLUP);
  pinMode(U_PIN, INPUT_PULLUP);
  pinMode(D_PIN, INPUT_PULLUP);

  // enable the driver
  digitalWrite(ENABLE_PIN, LOW);

}

void loop() {


  if (digitalRead(L_PIN) == LOW) {
    digitalWrite(X_DIR_PIN, LOW);
    digitalWrite(X_PIN, HIGH);
    delayMicroseconds(PULSE_US);
    digitalWrite(X_PIN, LOW);
  }

  if (digitalRead(R_PIN) == LOW) {
    digitalWrite(X_DIR_PIN, HIGH);
    digitalWrite(X_PIN, HIGH);
    delayMicroseconds(PULSE_US);
    digitalWrite(X_PIN, LOW);
    
  }

    if (digitalRead(U_PIN) == LOW) {
    digitalWrite(Y_DIR_PIN, LOW);
    digitalWrite(Y_PIN, HIGH);
    delayMicroseconds(PULSE_US);
    digitalWrite(Y_PIN, LOW);
    delayMicroseconds(PULSE_US);
  }

  if (digitalRead(D_PIN) == LOW) {
    digitalWrite(Y_DIR_PIN, HIGH);
    digitalWrite(Y_PIN, HIGH);
    delayMicroseconds(PULSE_US);
    digitalWrite(Y_PIN, LOW);
    delayMicroseconds(PULSE_US);
    
  }


}