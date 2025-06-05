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


  if (Serial.available()) {
    serial_processing();
  }
  
  handle_relays();
  handle_coils();
}

void serial_processing() {

  String data = Serial.readString();
  String split_data[data_splits] = {};
  int first_split = data.indexOf(";");
  split_data[0] = data.substring(0, first_split);
  split_data[1] = data.substring(first_split+1, data.length());

  String operation = split_data[0];


  if (operation == "X") {
    axis_x_value = split_data[1].toDouble();
    if (axis_x_value < 0.0) {
      axis_x_neg = true;
    }
    else {
      axis_x_neg = false;
    }
  } else if (operation == "Y") {
    axis_y_value = split_data[1].toDouble();
    if (axis_y_value < 0.0) {
      axis_y_neg = true;
    }
    else {
      axis_y_neg = false;
    }
  } else if (operation == "Z") {
    axis_z_value = split_data[1].toDouble();
    if (axis_z_value < 0.0) {
      axis_z_neg = true;
    }
    else {
      axis_z_neg = false;
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