#include <Wire.h>
#include <DHT.h> //Adarfruit library Unified_Sensors muss auch installiert werden

#define SLAVE_ADDRESS 0x05   // I2C-SLAVE-ADR.
#define PIN_ANALOG_OUT  A1   // Alk. 
#define DHT_PIN 13  // Temp. & Hum.
#define DHTTYPE DHT11  

//define I/O pins
#define vodkaPin 9
#define ojuicePin 8
#define cranberryPin 7
#define ginPin 6
#define tonicPin 5
#define jaegerPin 4
#define energyPin 3
#define bluePin 2
#define idlePin 10

DHT dht(DHT_PIN, DHTTYPE);

//Ultrasound Sensor
const int trigPin = 12;
const int echoPin = 11;

bool startMessung = false; 
bool startValves = false;
 
float temp;
float hum; 
float alkVolt;
float alkVoltMax=0; 
int distance; 

// Mittelwerte
float distanceMid; 
float tempMid;
float humMid;

// skalierte Werte
int tempMidBit;
int humMidBit;
int distanceMidBit;
int alkVoltMaxBit;

// Byte-Array zum verschicken an RPi
byte data[5];

int drinkChoice = 0;

int amountOne = 0;
int amountTwo = 0;
int ingredientOne;
int ingredientTwo;

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
  pinMode(DHT_PIN, INPUT);
  dht.begin();

  pinMode(vodkaPin, OUTPUT);
  pinMode(ojuicePin, OUTPUT);
  pinMode(cranberryPin, OUTPUT);  
  pinMode(ginPin, OUTPUT);
  pinMode(tonicPin, OUTPUT);
  pinMode(jaegerPin, OUTPUT);
  pinMode(energyPin, OUTPUT);  
  pinMode(bluePin, OUTPUT);
  
}


void loop()
{
  // SENSOR MESSROUTINE
  if (startMessung == true) {
    alkVolt = 0;
    alkVoltMax = 0;
  
    distance = 0;
    distanceMid = 0;
  
    temp = 0;
    tempMid = 0;
   
    hum = 0;
    humMid = 0;

    data[0] = 99; // SPEICHER-REGISTER ADRESSE?
    data[1] = 0;
    data[2] = 0;
    data[3] = 0;
    data[4] = 0;

    // MESSUNG FÜR 10 SEKUNDEN
    for (int i = 0; i <= 9; i++) {
      alkVolt = readAlk();
      // nur der maximale Alkohol-Wert wird übergeben
      if (alkVolt>alkVoltMax) {
        alkVoltMax=alkVolt;
      }

      // Aufaddieren der Abstands-, Temperatur und Feuchtigkeitswerte
      distance = distance + readUltrasonic();
      temp = temp + dht.readTemperature();
      hum = hum + dht.readHumidity();

      Serial.print("Distance:");
      Serial.println(distance);
      
      Serial.print("Alk: ");
      Serial.println(alkVolt);
      
      Serial.print("max. Alk: ");
      Serial.println(alkVoltMax);
      
      Serial.print("Temp: ");
      Serial.println(temp);
      
      Serial.print("Hum: ");
      Serial.println(hum);

      delay(800); 
    }

    // AUSGABE DER MESSERGEBNISSE
    Serial.print("nach 10 Sekunden Messung --> max. Alkohol-Wert: ");
    Serial.println(alkVoltMax); 
    
    distanceMid = distance/10;
    Serial.print("nach 10 Sekunden Messung --> Mittelwert des Abstandssensor:");
    Serial.println(distanceMid);

    tempMid = temp/10;
    Serial.print("nach 10 Sekunden Messung --> Mittelwert des Temperatursensor:");
    Serial.println(tempMid);

    humMid = hum/10;
    Serial.print("nach 10 Sekunden Messung --> Mittelwert des Feuchtigkeitssensor:");
    Serial.println(humMid);


    // SKALIEREN DER WERTE AUF WERTEBEREICH 0 - 255  
    alkVoltMaxBit = (alkVoltMax/5) * 255; 
    distanceMidBit = (distanceMid/50) * 255; 
    tempMidBit = (tempMid/40) * 255;  
    humMidBit = (humMid/100) * 255; 
    
   //Abstandsmessung wird nach einigen 50-100cm fehlerhaft(zu große Werte, über 20m) deswegen skalieren auf Max Wert
   if (distanceMidBit > 255) {
    distanceMidBit = 255; 
   }
   
    // AUSGABE DER SKALIERTEN MESSERGEBNISSE
    Serial.print("Skalierter Alkoholwertt:");
    Serial.println(alkVoltMaxBit);
    
    Serial.print("Skalierter Abstandswert:");
    Serial.println(distanceMidBit);
  
    Serial.print("Skalierter Temperaturwert:");
    Serial.println(tempMidBit);
  
    Serial.print("Skalierter Feuchtigkeitswert: ");
    Serial.println(humMidBit);

    data[1] = alkVoltMaxBit;
    data[2] = distanceMidBit;
    data[3] = tempMidBit;
    data[4] = humMidBit;
    
    startMessung = false;   
  }
  
  if (startValves == true) {    
    Serial.print("Ausgewählter Drink:");
    Serial.println(drinkChoice);

    //switch case for make the right cocktail
    switch (drinkChoice) {
      
      case 0:
        Serial.println("Sex on the Beach ;)");
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(25000);
        digitalWrite(vodkaPin, LOW);
        delay(25000);
        digitalWrite(ojuicePin, LOW);
        digitalWrite(cranberryPin, LOW);
        break;
     
      case 1:
        Serial.println("Gin Tonic");
        digitalWrite(ginPin, HIGH);
        digitalWrite(tonicPin, HIGH);
        delay(25000);
        digitalWrite(ginPin, LOW);
        delay(50000);
        digitalWrite(tonicPin, LOW);
        break;

      case 2:
        Serial.println("Blue Lagoon");
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(bluePin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        delay(25000);
        digitalWrite(vodkaPin, LOW);
        digitalWrite(bluePin, LOW);
        delay(50000);
        digitalWrite(ojuicePin, LOW);
        break;

      case 3:
        Serial.println("Flying Hirsch");
        digitalWrite(jaegerPin, HIGH);
        digitalWrite(energyPin, HIGH);
        delay(30000);
        digitalWrite(jaegerPin, LOW);
        delay(65000);
        digitalWrite(energyPin, LOW);
        break;

      case 4:
        Serial.println("Vodka E");                
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(energyPin, HIGH);
        delay(30000);
        digitalWrite(vodkaPin, LOW);
        delay(65000);
        digitalWrite(energyPin, LOW);
        break;
        
      case 5:
        Serial.println("HemingWay");
        digitalWrite(ginPin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(25000);
        digitalWrite(ginPin, LOW);
        delay(50000);
        digitalWrite(ojuicePin, LOW);
        digitalWrite(cranberryPin, LOW);
        break;

      case 6: 
        Serial.println("Blue Gin Tonic");
        digitalWrite(ginPin, HIGH);
        digitalWrite(tonicPin, HIGH);
        digitalWrite(bluePin, HIGH);
        delay(15000);
        digitalWrite(bluePin, LOW);
        delay(10000);
        digitalWrite(ginPin, LOW);
        delay(50000);
        digitalWrite(tonicPin, LOW);
        break;

      case 7:
        Serial.println("Strong Red");
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(ginPin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(15000);
        digitalWrite(vodkaPin, LOW);
        digitalWrite(ginPin, LOW);
        delay(55000);
        digitalWrite(cranberryPin, LOW);
        break;

      case 8:
        Serial.println("No Sex on the Beach");
        digitalWrite(ojuicePin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(50000);
        digitalWrite(cranberryPin, LOW);
        delay(25000);
        digitalWrite(ojuicePin, LOW);
        break;
        
      case 9:
        Serial.println("Blue Lagoon alkfree");
        digitalWrite(bluePin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        delay(25000);
        digitalWrite(bluePin, LOW);
        delay(50000);
        digitalWrite(ojuicePin, LOW);  
        break;
    }        
    startValves = false;
  }
}


float readAlk() {
  
    float sensorValue, sensorVolt;

    sensorValue = analogRead(PIN_ANALOG_OUT);
    sensorVolt = sensorValue / 1024 * 5.0;

    return sensorVolt; 
}

int readUltrasonic() {
  
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

// I2C FUNCTIONS
void receiveEvent(int howMany) {
    int rxData = Wire.read();
    
    if (rxData == 11) {
      startMessung = true; 

    } else if (rxData < 11) {
      startValves = true;
      drinkChoice = rxData; 
    }
}

void sendData() { 
    Wire.write(data, 5);    
    Serial.println("Daten versendet");
    Serial.println(data[0]);
    Serial.println(data[1]);
    Serial.println(data[2]);
    Serial.println(data[3]);
    Serial.println(data[4]);
}

/*
// DRINK MIXING ROUTING
void mixingDrink(int ingredientOne, int amountOne, int ingredientTwo, int amountTwo) {
  //function to set ml to the glass
  //if u need one ingredient, pls set the ingredientTwo and amountTwo to zero
  int delayone = 0; 
  int delaytwo = 0;
  
  //how much ml troughput per minute CHANGE HERE!
  int measurement_time = 90; //time ml in seconds
  int measurement_ml = 200; //ml in time
  
  int mlins = (measurement_ml/measurement_time);
  int mlinms = (mlins/1000);
  
  if (amountOne < amountTwo) {
    delayone = amountOne;
    delaytwo = amountTwo-amountOne;

    digitalWrite(ingredientOne, HIGH);
    digitalWrite(ingredientTwo, HIGH);
    // delay(delayone/mlinms);
    delay(25000);
    digitalWrite(ingredientOne, LOW);
    // delay(delaytwo/mlinms);
    digitalWrite(ingredientTwo, LOW);
      
    } else if (amountOne > amountTwo) {
      delayone = amountTwo;
      delaytwo = amountOne-amountTwo;
      
      digitalWrite(ingredientOne, HIGH);
      digitalWrite(ingredientTwo, HIGH);
      //delay(delayone/mlinms);
      delay(25000);
      digitalWrite(ingredientTwo, LOW);
      // delay(delaytwo/mlinms);
      digitalWrite(ingredientOne, LOW);
            
    } else if (amountOne == amountTwo) {
      delayone = amountOne;
      delaytwo = 0;
      digitalWrite(ingredientOne, HIGH);
      digitalWrite(ingredientTwo, HIGH);
      //delay(delayone/mlinms);
      delay(25000);
      digitalWrite(ingredientTwo, LOW);
      // delay(delaytwo/mlinms);
      digitalWrite(ingredientOne, LOW);
    }  
} */
