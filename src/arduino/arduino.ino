#include <SafeString.h>

const int coil_count = 5;
const int coil_pins[] = {3, 5, 6, 9, 10 };
const int relay_pins[] = {2, 4, 7, 8, 12 };

const int data_splits = 2;

double axis_x_value = 0;
double axis_y_value = 0;
double axis_z_value = 0;

bool axis_x_neg = false;
bool axis_y_neg = false;
bool axis_z_neg = false;

void setup() {
  for (int i = 0; i < 5; i++) {
    pinMode(relay_pins[i], OUTPUT);
    digitalWrite(relay_pins[i], LOW);
  }
  Serial.begin(115200);
}

void loop() {

  serial_processing();
  handle_relays();
  handle_coils();
}

void serial_processing() {

  if (Serial.available() > 0) {
    char input[100];
    createSafeString (strInput, sizeof(input));
    strInput = Serial.readStringUntil('\n').c_str();

    if (strInput.startsWith("X;")) {
      strInput.remove(0,2); 
      createSafeString (str_x, 20);

      // Split the string and assign to variable
      strInput.stoken(str_x, 0, ";");
      axis_x_value = atof(str_x.c_str());
      Serial.print("X;");
      Serial.println(axis_x_value);

      if (axis_x_value < 0.0) {
        axis_x_neg = true;
      }
      else {
        axis_x_neg = false;
      }
    }

    if (strInput.indexOf("Y") > -1) {
      strInput.remove(0,2); 
      createSafeString (str_y, 20);

      // Split the string and assign to variables
      strInput.stoken(str_y, 0, ";");
      axis_y_value = atof(str_y.c_str());
      Serial.print("X;");
      Serial.println(axis_y_value);

      if (axis_y_value < 0.0) {
        axis_y_neg = true;
      }
      else {
        axis_y_neg = false;
      }
    }

    if (strInput.indexOf("Z") > -1) {
      strInput.remove(0,2); 
      createSafeString (str_z, 20);

      // Split the string and assign to variables
      strInput.stoken(str_z, 0, ";");
      axis_z_value = atof(str_z.c_str());
      Serial.print("Z;");
      Serial.println(axis_z_value);

      if (axis_z_value < 0.0) {
        axis_z_neg = true;
      }
      else {
        axis_z_neg = false;
      }
    }
  }
}

void handle_relays() {
  digitalWrite(relay_pins[0], axis_x_neg);
  digitalWrite(relay_pins[1], axis_x_neg);

  digitalWrite(relay_pins[2], axis_y_neg);
  digitalWrite(relay_pins[3], axis_y_neg);

  digitalWrite(relay_pins[4], axis_z_neg);
}

void handle_coils() {
  analogWrite(coil_pins[0], calc_pin_val(axis_x_value));
  analogWrite(coil_pins[1], calc_pin_val(axis_x_value));


  analogWrite(coil_pins[2], calc_pin_val(axis_y_value));
  analogWrite(coil_pins[3], calc_pin_val(axis_y_value));

  analogWrite(coil_pins[4], calc_pin_val(axis_z_value));
}

int calc_pin_val(float voltage) {
  return abs(int(voltage * 255 / 5));
}
