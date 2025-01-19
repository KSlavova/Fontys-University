int red=4;
int delayTime=1000;
void setup() {
  pinMode(red,OUTPUT);
}

void loop() {
  digitalWrite(red,HIGH);
  delay(delayTime);
  digitalWrite(red,LOW);
  delay(delayTime);
}
