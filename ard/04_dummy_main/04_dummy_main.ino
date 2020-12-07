// Dummy main loop to serve as a guide for the I2C connection 
// between Arduino and Raspberry Pi (RPI). 
// The Arduino will send its sensor data to the RPI.

// Afterwards the Arduino will receive an integer value (drinkChoice) from the RPI,
// which should trigger the valves.

#include <Wire.h>
#define SLAVE_ADDRESS 0x05

int data[4];

void setup() {
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);
    Wire.onRequest(sendData);
    Wire.onReceive(receiveEvent);
    Serial.begin(9600);
}

void loop() {
// dummy data from sensors  
    data[0] = 100; // sensor 1
    data[1] = 101; // sensor 2
    data[2] = 102; // sensor 3
    data[3] = 104; // sensor 4
}

// callback for sending data
int i = 0; // FIX THIS --> i isn't set back to 0 during next sendData()-call
void sendData() { 
    Wire.write(data[i]);
    i++;
    if (i > 3) {
         i = 0;
    }
}

void receiveEvent(int howMany) {
    int drinkChoice = Wire.read();
    Serial.println(drinkChoice);
}
 
