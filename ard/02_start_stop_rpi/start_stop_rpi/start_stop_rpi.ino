/*

This code aims to save the state of an LED in order to turn it on and off with the press of a button.
It is based on the example code "Debounce":   http://www.arduino.cc/en/Tutorial/Debounce

The code needs a debouncing routine in order to counteract the issue of integrating a physical push button, which 
by nature bounces very quickly between HIGH and LOW states when pressed.

millis() --> Returns the number of milliseconds passed since the Arduino board began running the current program.

This code will be used to start and stop a program/loop/function on a Raspberry Pi 4 (RPI) with the press of a button from
an Arduino. Arduino and RPI will be connected via I2C.

*/


// INIT
const int buttonPin = 1;   
const int ledPin = LED_BUILTIN;      

int ledState = HIGH;         
int buttonState;             
int lastButtonState = LOW;   

unsigned long lastDebounceTime = 0;  
unsigned long debounceDelay = 50;    

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
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
        // INSERT FUNCTION TO SEND ledState TO VIA I2C RPI HERE  
        Serial.print(ledState); 
        // END INSERT
      }
    }
  }
  digitalWrite(ledPin, ledState);
  lastButtonState = reading;
}
