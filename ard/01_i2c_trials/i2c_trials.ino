#include <Wire.h>

#define addr 0x05
int num = 0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Wire.begin(addr);

  Wire.onReceive(rxData);
  Wire.onRequest(txData);

  Serial.println("Ready");
}

void loop() {
  delay(100);
}

void rxData(int byteCount) {
  while (Wire.available()) {
    num = Wire.read();
    Serial.print("Received data: ");
    Serial.println(num);

    if (num == 1) {
        digitalWrite(LED_BUILTIN, HIGH);
    } else {
        digitalWrite(LED_BUILTIN, LOW);
    }
  }
}

void txData() {
  Wire.write(num);
}
