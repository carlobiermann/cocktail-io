#include <Wire.h>
#define SLAVE_ADDRESS 0x05
//Temp+Hum
#include <dht11.h>
#define DHT11PIN 4
//Alkoholsensor
#define PIN_ANALOG_OUT  A1
//Ultrasonic Sensor
const int trigPin = 8;
const int echoPin = 9;
int a=0; 
int i=10; 
int n=0; 
float temp;
float hum; 
float alkVolt;
float alkVoltMax=0; 
int distance; 
int tempMidBit;
int humMidBit;
int distanceMidBit;
int alkVoltMaxBit;
int startMessung=0; 
int data[4];

dht11 DHT11;


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
  pinMode(4, INPUT);
 
}

float readTemp()
{
  int chk = DHT11.read(DHT11PIN);
  float temper = DHT11.temperature;

  //Serial.print("Temperature (C): ");
  //Serial.println(temper, 2);
  return(temper);
}

float readHum()
{
  int chk = DHT11.read(DHT11PIN);
  float humi = DHT11.humidity;

  //Serial.print("Humidity (%): ");
  //Serial.println(humi, 2);
  return (humi); 
}

float readAlk()
{
    float sensorValue, sensorVolt;

    sensorValue = analogRead(PIN_ANALOG_OUT);
    sensorVolt = sensorValue / 1024 * 5.0;

    //Serial.println("Sensor: " + String(sensorValue) + " (" + String(sensorVolt) + "V)");
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
  // Calculating the distance
  distance= duration*0.034/2;
  // Prints the distance on the Serial Monitor
  ////Serial.print("Distance in cm: ");
  //Serial.println(distance);
  return(distance);
}


void loop()
{
  Serial.println(startMessung);
  delay(500); 
  if (startMessung == 1)
  {
    while (a<i)
    {
      temp = readTemp()+temp;
      hum = readHum()+hum;
      distance = readUltrasonic()+ distance;
      alkVolt = readAlk();

      //Ermittlung des maximalen Wertes über die Messung 
      if (alkVolt>alkVoltMax)
      {
         alkVoltMax=alkVolt;
      }

  
      Serial.print("Distance:");
      Serial.println(distance);
      Serial.print("Temp: ");
      Serial.println(temp);
      Serial.print("Hum: ");
      Serial.println(hum);
      Serial.print("Alk: ");
      Serial.println(alkVolt);
      delay(800);
      a++;
    }

  //Ermittlung der Durchschnitsswerte über die Messung 
  float distanceMid = distance/i; 
  float tempMid = temp/i; 
  float humMid = hum/i; 


  Serial.print("DistanceMid:");
  Serial.println(distanceMid);
  Serial.print("TempMid:");
  Serial.println(tempMid);
  Serial.print("HumMid:");
  Serial.println(humMid);
  Serial.print("alkVoltMax:");
  Serial.println(alkVoltMax);
  Serial.println("over ");

  //Umrechnung in 8Bit, Wertebereich von 0 bis 255
  //Temperatur: 0° entspricht 0, 40° entspricht 255, Hier wurde der realistische, NICHT der mögliche Wertebereich abgedeckt 
  //Luftfeuchtigkeit: 0% entspricht 0, 100% entspricht 255
  //Abstand: 0cm entspricht 0 und 50cm entspricht 255
  //Alkohol in Volt: 0V entspricht 0 und 5V entspricht 255

   tempMidBit= (tempMid/40)*255;  
   humMidBit= (humMid/100)*255; 
   alkVoltMaxBit= (alkVoltMax/5)*255; 
   distanceMidBit= (distanceMid/50)*255; 

   //Abstandsmessung wird nach einigen 50-100cm fehlerhaft(zu große Werte, über 20m) deswegen skalieren auf Max Wert
   if (distanceMidBit>255)
   {
    distanceMidBit=255; 
   }
          
  Serial.print("DistanceMidBit:");
  Serial.println(distanceMidBit);
  Serial.print("TempMidBit:");
  Serial.println(tempMidBit);
  Serial.print("HumMidBit:");
  Serial.println(humMidBit);
  Serial.print("alkVoltMaxBit:");
  Serial.println(alkVoltMaxBit);
  Serial.println("over ");
  delay(1000);
  }
  
  data[0] = tempMidBit; // sensor 1
  data[1] = humMidBit; // sensor 2
  data[2] = alkVoltMaxBit; // sensor 3
  data[3] = distanceMidBit; // sensor 4

  startMessung=0; 
}

void sendData() { 
    Wire.write(data[n]);
    n++;
    if (n > 3) {
         n = 0;
    }
}


void receiveEvent(int howMany) {
    int event = Wire.read();
    if (event == 11); 
    {
      startMessung = 1; 
    }    
}
