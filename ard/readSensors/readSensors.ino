#include <Wire.h>
// #include <dht11.h>

#define SLAVE_ADDRESS 0x05   // I2C-SLAVE-ADR.
#define PIN_ANALOG_OUT  A1   // Alk. 
// #define DHT11PIN 4           // Temp. & Hum.

//Ultrasonic Sensor
const int trigPin = 8;
const int echoPin = 9;


// int a=0; 
// int i=10; 
// int n=0; 

bool startMessung = false; 

// dht11 DHT11;

// float temp;
// float hum; 
float alkVolt;
float alkVoltMax=0; 
int distance; 
float distanceMid; // Mittelwert

// skalierte Werte
//int tempMidBit;
//int humMidBit;
int distanceMidBit;
int alkVoltMaxBit;

byte data[3];


void setup() 
{
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  Wire.onRequest(sendData);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  pinMode(PIN_ANALOG_OUT, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);  
}


void loop()
{
  // SENSOR MESSROUTINE
  if (startMessung == true)
  {
    alkVolt = 0;
    alkVoltMax = 0;
    distance = 0;
    distanceMid = 0;
    data[0] = 0;
    data[1] = 0;
    // temp = 0;
    // hum = 0;

    // MESSUNG FÜR 10 SEKUNDEN
    for (int i = 0; i <= 9; i++)
    {
    
      alkVolt = readAlk();

      // nur der maximale Alkohol-Wert wird übergeben
      if (alkVolt>alkVoltMax)
      {
        alkVoltMax=alkVolt;
      }

      // Aufaddieren der Abstandswerte
      distance = distance + readUltrasonic();
      // temp = readTemp()+temp;
      // hum = readHum()+hum;

      Serial.print("Distance:");
      Serial.println(distance);
      
      Serial.print("Alk: ");
      Serial.println(alkVolt);
      
      Serial.print("max. Alk: ");
      Serial.println(alkVoltMax);
      
      // Serial.print("Temp: ");
      // Serial.println(temp);
      // Serial.print("Hum: ");
      // Serial.println(hum);

      delay(950); 
    }

    // AUSGABE DER MESSERGEBNISSE
    Serial.print("nach 10 Sekunden Messung --> max. Alkohol-Wert: ");
    Serial.println(alkVoltMax); 
    
    distanceMid = distance/10;
    Serial.print("nach 10 Sekunden Messung --> Mittelwert des Abstandssensor:");
    Serial.println(distanceMid);


    // SKALIEREN DER WERTE AUF WERTEBEREICH 0 - 255  
    alkVoltMaxBit = (alkVoltMax/5) * 255; 
    distanceMidBit = (distanceMid/50) * 255; 
    // tempMidBit = (tempMid/40) * 255;  
    // humMidBit = (humMid/100) * 255; 
    
   //Abstandsmessung wird nach einigen 50-100cm fehlerhaft(zu große Werte, über 20m) deswegen skalieren auf Max Wert
   if (distanceMidBit > 255)
   {
    distanceMidBit = 255; 
   }
   
    // AUSGABE DER SKALIERTEN MESSERGEBNISSE
    Serial.print("Skalierter Alkoholwertt:");
    Serial.println(alkVoltMaxBit);
    
    Serial.print("Skalierter Abstandswert:");
    Serial.println(distanceMidBit);
  
    // Serial.print("Skalierter Temperaturwert:");
    // Serial.println(tempMidBit);
  
    // Serial.print("Skalierter Feuchtigkeitswert: ");
    // Serial.println(humMidBit);

    data[0] = 99; // REGISTER ADRESSE?
    data[1] = distanceMidBit;
    data[2] = alkVoltMaxBit;
    
    startMessung = false;   
  }    
}


float readAlk()
{
    float sensorValue, sensorVolt;

    sensorValue = analogRead(PIN_ANALOG_OUT);
    sensorVolt = sensorValue / 1024 * 5.0;

    return sensorVolt; 
}

int readUltrasonic()
{
  long duration;
  int distance;
  
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;

  return(distance);
}

// float readTemp()
// {
//  int chk = DHT11.read(DHT11PIN);
//  float temper = DHT11.temperature;

//  return(temper);
// }

// float readHum()
// {
//  int chk = DHT11.read(DHT11PIN);
//  float humi = DHT11.humidity;

//  return (humi); 
// }


// I2C FUNCTIONS

void receiveEvent(int howMany) {
    int rxData = Wire.read();
    
    if (rxData == 11) 
    {
      startMessung = true; 
    } 
  
}

void sendData() { 
    Wire.write(data, 3);    
    Serial.println("Daten versendet");
    Serial.println(data[0]);
    Serial.println(data[1]);
    Serial.println(data[2]);
}
