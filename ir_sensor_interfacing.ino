int Led=13;
int SensorPin=7;
int BuzzerPin=8;
void setup() {
  // put your setup code here, to run once:
pinMode(Led,OUTPUT);
pinMode(SensorPin,INPUT);
pinMode(BuzzerPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value= digitalRead(SensorPin);
  if(value==1){
    digitalWrite(Led,HIGH);
    digitalWrite(BuzzerPin,LOW);
  }
  else{
    digitalWrite(Led,LOW);
    digitalWrite(BuzzerPin,HIGH);
  }

}
