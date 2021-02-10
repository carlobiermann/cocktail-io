#define vodkaPin 9
#define ojuicePin 8
#define cranberryPin 7
#define ginPin 6
#define tonicPin 5
#define jaegerPin 4
#define energyPin 3
#define bluePin 2


void setup() {
  // put your setup code here, to run once:
 
  pinMode(bluePin, OUTPUT);
  pinMode(energyPin, OUTPUT);
  pinMode(jaegerPin, OUTPUT);
  pinMode(tonicPin, OUTPUT);
  pinMode(ginPin, OUTPUT);
  pinMode(cranberryPin, OUTPUT);
  pinMode(ojuicePin, OUTPUT);
  pinMode(vodkaPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

/*
  // VENTIL 8
  delay(5000);
  digitalWrite(bluePin, HIGH);
  delay(5000);
  digitalWrite(bluePin, LOW);

  // VENTIL 7
  delay(5000);
  digitalWrite(energyPin, HIGH);
  delay(5000);
  digitalWrite(energyPin, LOW);

  // VENTIL 6
  delay(5000);
  digitalWrite(jaegerPin, HIGH);
  delay(5000);
  digitalWrite(jaegerPin, LOW);

  // VENTIL 5
  delay(5000);
  digitalWrite(tonicPin, HIGH);
  delay(5000);
  digitalWrite(tonicPin, LOW);  

  // VENTIL 4
  delay(5000);
  digitalWrite(ginPin, HIGH);
  delay(5000);
  digitalWrite(ginPin, LOW);  

  // VENTIL 3
  delay(5000);
  digitalWrite(cranberryPin, HIGH);
  delay(5000);
  digitalWrite(cranberryPin, LOW);  

  // VENTIL 2
  delay(5000);
  digitalWrite(ojuicePin, HIGH);
  delay(5000);
  digitalWrite(ojuicePin, LOW);  

  // VENTIL 1
  delay(5000);
  digitalWrite(vodkaPin, HIGH);
  delay(5000);
  digitalWrite(vodkaPin, LOW);
  */

 /*
  * 
        Serial.println("Sex on the Beach ;)");
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(25000);
        digitalWrite(vodkaPin, LOW);
        delay(25000);
        digitalWrite(ojuicePin, LOW);
        digitalWrite(cranberryPin, LOW);

     
        Serial.println("Gin Tonic");
        digitalWrite(ginPin, HIGH);
        digitalWrite(tonicPin, HIGH);
        delay(25000);
        digitalWrite(ginPin, LOW);
        delay(50000);
        digitalWrite(tonicPin, LOW);

*/

        Serial.println("Blue Lagoon");
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(bluePin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        delay(25000);
        digitalWrite(vodkaPin, LOW);
        digitalWrite(bluePin, LOW);
        delay(50000);
        digitalWrite(ojuicePin, LOW);

        /*

        Serial.println("Flying Hirsch");
        digitalWrite(jaegerPin, HIGH);
        digitalWrite(energyPin, HIGH);
        delay(30000);
        digitalWrite(jaegerPin, LOW);
        delay(65000);
        digitalWrite(energyPin, LOW);

        Serial.println("Vodka E");                
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(energyPin, HIGH);
        delay(30000);
        digitalWrite(vodkaPin, LOW);
        delay(65000);
        digitalWrite(energyPin, LOW);
        
        Serial.println("HemingWay");
        digitalWrite(ginPin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(25000);
        digitalWrite(ginPin, LOW);
        delay(50000);
        digitalWrite(ojuicePin, LOW);
        digitalWrite(cranberryPin, LOW);

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
        
        Serial.println("Strong Red");
        digitalWrite(vodkaPin, HIGH);
        digitalWrite(ginPin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(15000);
        digitalWrite(vodkaPin, LOW);
        digitalWrite(ginPin, LOW);
        delay(55000);
        digitalWrite(cranberryPin, LOW);

        Serial.println("No Sex on the Beach");
        digitalWrite(ojuicePin, HIGH);
        digitalWrite(cranberryPin, HIGH);
        delay(50000);
        digitalWrite(cranberryPin, LOW);
        delay(25000);
        digitalWrite(ojuicePin, LOW);
        
        Serial.println("Blue Lagoon alkfree");
        digitalWrite(bluePin, HIGH);
        digitalWrite(ojuicePin, HIGH);
        delay(25000);
        digitalWrite(bluePin, LOW);
        delay(50000);
        digitalWrite(ojuicePin, LOW);  
  */
    
  
}
