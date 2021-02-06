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

DHT dht(DHT_PIN, DHTTYPE);

//Ultrasonic Sensor
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

//define variables

int amountOne = 0;
int amountTwo = 0;
char ingredientOne;
char ingredientTwo;

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
  if (startMessung == true)
  {
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
    for (int i = 0; i <= 9; i++)
    {
    
      alkVolt = readAlk();

      // nur der maximale Alkohol-Wert wird übergeben
      if (alkVolt>alkVoltMax)
      {
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
   if (distanceMidBit > 255)
   {
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
  
  if (startValves == true) 
  {
    Serial.print("Ausgewählter Drink:");
    Serial.println(drinkChoice);

    //switch case for make the right cocktail
    switch (drinkChoice) {
      
      case 0:
        Serial.println("Sex on the Beach ;)");
        getin(vodkaPin, 50, ojuicePin, 100);
        getin(cranberryPin, 100, 0, 0);
     
      case 1:
        Serial.println("Gin Tonic");
        getin(ginPin, 50, tonicPin, 150);

      case 2:
        Serial.println("Blue Lagoon");
        getin(vodkaPin, 50, bluePin, 50);
        getin(ojuicePin, 150, 0, 0);
        
      case 3:
        Serial.println("Flying Hirsch");
        getin(jaegerPin, 60, energyPin, 190);

      case 4:
        Serial.println("Vodka E");
        getin(vodkaPin, 60, energyPin, 190);
        
      case 5:
        Serial.println("HemingWay");
        getin(ginPin, 50, ojuicePin, 100);
        getin(cranberryPin, 100, 0, 0);

      case 6: 
        Serial.println("Blue Gin Tonic");
        getin(ginPin, 50, tonicPin, 150);
        getin(bluePin, 30, 0, 0);

      case 7:
        Serial.println("Strong Red");
        getin(vodkaPin, 30, ginPin, 30);
        getin(cranberryPin, 140, 0, 0);

      case 8:
        Serial.println("No Sex on the Beach");
        getin(ojuicePin, 150, cranberryPin, 100);

      case 9:
        Serial.println("Blue Lagoon alkfree");
        getin(bluePin, 50, ojuicePin, 150);
    
    }        
    startValves = false;
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

void getin(char ingredientOne, int amountOne, char ingredientTwo, int amountTwo) {
  //function to set ml to the glass
  //if u need one ingredient, pls set the ingredientTwo and amountTwo to zero

  int delayone = 0; 
  int delaytwo = 0;
  
  //how much ml troughput per minute CHANGE HERE!
  int measurement_time = 100; //time ml in seconds
  int measurment_ml = 10; //ml in time
  int mlins = (measurment_ml/measurement_time);
  int mlinms = (mlins/1000);
  
  if (ingredientTwo != 0 && amountTwo != 0) {
    //two ingredients at the same time
    if (amountOne < amountTwo) {
      delayone = amountOne;
      delaytwo = amountTwo-amountOne;
    }
    else if (amountOne > amountTwo) {
      delayone = amountTwo;
      delaytwo = amountOne-amountTwo;
    }
    else if (amountOne == amountTwo) {
      delayone = amountOne;
      delaytwo = 0;
    } else {
    //only one ingredient
    digitalWrite(ingredientOne, HIGH);
    delay(amountOne/mlinms);
    digitalWrite(ingredientOne, LOW);
     }
     
    digitalWrite(ingredientOne, HIGH);
    digitalWrite(ingredientTwo, HIGH);
    delay(delayone/mlinms);
    digitalWrite(ingredientOne, LOW);
    delay(delaytwo/mlinms);
    digitalWrite(ingredientTwo, LOW);
        
  }
}
