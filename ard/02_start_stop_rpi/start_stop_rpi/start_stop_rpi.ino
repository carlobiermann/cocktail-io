#include <Wire.h>

#define addr 0x05

const int buttonPin = 1;  

int ledState = HIGH;
int buttonState;             
int lastButtonState = LOW;   

unsigned long lastDebounceTime = 0;  
unsigned long debounceDelay = 50;  

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  Wire.begin(addr);

  Wire.onReceive(rxData);
  Wire.onRequest(txData);
}


void loop() {
  int reading = digitalRead(buttonPin);
  
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        ledState = !ledState;
      }
    }
  }
  lastButtonState = reading;
}

void rxData(int byteCount) {
  while (Wire.available()) {
  // do nothing
  }
}

void txData() {
  Wire.write(ledState);
}
