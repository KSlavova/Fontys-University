#include "Display.h" //libraries
#include "DHT11.h"

const int PIN_LDR = 16;//light sensor
const int button=8;
int counter=0;
int buttonState=0;

void setup() {
  pinMode(PIN_LDR, INPUT);
  pinMode(button, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  buttonState=digitalRead(button);
  if(buttonState==LOW){
    counter++;
    if(counter>4){
      counter=1;
    }
      if(counter==1){
        Display.show("NONE");
        Serial.println("NONE");
        
  }
  else if(counter==2){
     float temperature = DHT11.getTemperature();
        if (isnan(temperature)) { //isnan() converts the value to a number before testing
        Display.show("Err");
        Serial.println("Error");
    }
    else
    {
        Display.show(temperature);
        Serial.print("The temperature is: ");
        Serial.println(temperature);
    }
  }
  else if(counter==3){
       float humidity=DHT11.getHumidity();
         if (isnan(humidity)) { //isnan() converts the value to a number before testing
        Display.show("Err");
        Serial.println("Error");
    }
    else
    {
        Display.show(humidity);
        Serial.print("The humidity is: ");
         Serial.println(humidity);
    }
  }
  else if(counter==4){
    // read the analog value
    int sensorValue = analogRead(PIN_LDR);
    float resistance_sensor;
    // and convert to resistance in Kohms
    resistance_sensor=(float)(1023-sensorValue)*10/sensorValue;

    Serial.print("The resistance of the light sensor is: ");
    Serial.print(resistance_sensor, 1);
    Serial.println(" KOhm");

    // convert the resitance to Lux
    float lux;
    lux = 325 * pow(resistance_sensor, -1.4);

    Display.show(lux/1000);

    Serial.print("Illuminance is almost ");
    Serial.print(lux/1000, 1);
    Serial.println(" Kilo lux");
  }
    delay(350);
  }
}
