#include <Wire.h>
//Temp+Hum
#include <dht11.h>
#define DHT11PIN 4
//Alkoholsensor
#define PIN_ANALOG_OUT  A0
//Ultrasonic Sensor
const int trigPin = 9;
const int echoPin = 10;

dht11 DHT11;

void setup()
{
  Wire.begin();
  Serial.begin(9600);
  pinMode(PIN_ANALOG_OUT, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
 
}

void readTempHum()
{
  int chk = DHT11.read(DHT11PIN);
  float humi = DHT11.humidity;
  float temper = DHT11.temperature;

  Serial.print("Humidity (%): ");
  Serial.println(humi, 2);

  Serial.print("Temperature (C): ");
  Serial.println(temper, 2);
}

void readAlk()
{
    float sensorValue, sensorVolt;

    sensorValue = analogRead(PIN_ANALOG_OUT);
    sensorVolt = sensorValue / 1024 * 5.0;

    Serial.println("Sensor: " + String(sensorValue) + " (" + String(sensorVolt) + "V)");
}

void readUltrasonic()
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
  Serial.print("Distance in cm: ");
  Serial.println(distance);
}

void sendOverI2C()
{
  Wire.beginTransmission(0x55); 
  Wire.write(7);             
  Wire.endTransmission();    
}
void loop()
{

  readTempHum();
  readAlk();
  readUltrasonic();
  delay(2000);

  

}
