int potMeter=A0;
void setup() {
  pinMode(potMeter,INPUT);
  Serial.begin(9600);
}

void loop() {
  int value=analogRead(potMeter);
}
