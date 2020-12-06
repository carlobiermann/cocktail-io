/////////////////////////////////////////////
// cocktail-maker IO main loop
// horizontal joghurtz
/////////////////////////////////////////////

//how much ml troughput per minute CHANGE HERE!
#define mlinm = 100;
#define mlins = (mlinm/60);
#define mlinms = (mlins/1000);

//define I/O pins
#define vodkaPin 3
#define ojuicePin 4
#define cranberryPin 5
#define ginPin 6
#define tonicPin 7
#define jaegerPin 8
#define energyPin 9
#define bluePin 10

//define variables
int amountOne = 0;
int amountTwo = 0;
char ingredientOne;
char ingredientTwo;
int choosenCocktail = 0;

//define often use code snippets as functions

void getin(char ingredientOne, int amountOne, char ingredientTwo, int amountTwo) {
  //function to set ml to the glass
  //if u need one ingredient, pls set the ingredientTwo and amountTwo to zero
  
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
    }

    digitalWrite(ingredientOne, HIGH);
    digitalWrite(ingredientTwo, HIGH);
    delay(delayone/mlinms);
    digitalWrite(ingredientOne, LOW);
    delay(delaytwo/mlinms);
    digitalWrite(ingredientTwo, LOW);
        
  else {
    //only one ingredient
    digitalWrite(ingredientOne, HIGH);
    delay(amountOne/mlinms);
    digitalWrite(ingredientOne, LOW);
  }
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //debugging

  //set PinOutputs
  pinMode(vodkaPin, OUTPUT);
  pinMode(ojuicePin, OUTPUT);
  pinMode(cranberryPin, OUTPUT);
  pinMode(ginPin, OUTPUT);
  pinMode(tonicPin, OUTPUT);
  pinMode(jaegerPin, OUTPUT);
  pinMode(energyPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  //debugging bootstrap
  Serial.println("booted..");
}

void loop() {
  // put your main code here, to run repeatedly:

  //TO-DO: routine for get i2c data to variable "choosenCocktail"

  //TO-DO: sensor-input

  switch (choosenCocktail) {
    //switch case for make the right cocktail
    case 0:
      getin(ginPin, 40, tonicPin, 160);
      //...
    case 1:

    case 2:

    case 3:

    case 4:

    case 5:

    case 6: 

    case 7:

    case 8:

    case 9:
    
  }

  
  
  }
