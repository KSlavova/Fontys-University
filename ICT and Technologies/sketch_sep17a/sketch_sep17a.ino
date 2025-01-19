int potMeter=A0;
void setup(void) {
  // put your setup code here, to run once:
  pinMode(potMeter,INPUT);
  Serial.begin(9600);

}

void loop(void) {
  // put your main code here, to run repeatedly:
  int value=analogRead(potMeter);
  int mapValue=map(value,0,1023,0,100);
  Serial.print(value);
  Serial.print("=");
  Serial.println(mapValue);
  Serial.println("%");
}
