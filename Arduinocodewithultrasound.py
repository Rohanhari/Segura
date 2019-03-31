#include <SoftwareSerial.h>

const unsigned int TRIG_PIN=11;
const unsigned int ECHO_PIN=12;
const unsigned int BAUD_RATE=9600;

int led1=5;
int led2=6;


void setup() {
  
  Serial.begin(9600);
 
  pinMode(led1,OUTPUT);
  pinMode(led2,INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(BAUD_RATE);

}

void loop() {
  
  int val=0;
digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  digitalWrite(led1,HIGH);
  val=digitalRead(led2);
 const unsigned long duration= pulseIn(ECHO_PIN, HIGH);
 int distance= duration/29/2;
 if(duration==0){
   Serial.println("Warning: no pulse from sensor");
   } 
//  else{
//      Serial.print("distance to nearest object:");
//      Serial.println(distance);
//      Serial.println(" cm");
//  }

  
if(distance<=40){
  if(val==LOW){

  Serial.write("wear the helmet strap");
  Serial.println("wear the helmet strap");
  }
  
  
   if(val==HIGH)
  {Serial.println("good job");
    }
}
}
