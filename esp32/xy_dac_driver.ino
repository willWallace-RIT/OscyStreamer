#include <Arduino.h>

#define X_DAC 25
#define Y_DAC 26

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    int x = Serial.parseInt();
    int y = Serial.parseInt();

    x = constrain(x, -100, 100);
    y = constrain(y, -100, 100);

    int vx = map(x, -100, 100, 0, 255);
    int vy = map(y, -100, 100, 0, 255);

    dacWrite(X_DAC, vx);
    dacWrite(Y_DAC, vy);
  }
}
