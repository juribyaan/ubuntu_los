#include <Servo.h>

const int LED =     2;
const int button =  4;
const int trigPin = 11; //출력
const int echoPin = 12;
const int SERVO =9;
int A =        0;
int angle =   90;
Servo servo; 
int t=0;

void LED_b()
{
  Serial.print("LED");
  for(int i = 0 ; i<256 ; i++)
  {
    digitalWrite(LED ,  i);
  }
}

void wave()
{
  Serial.print("wave");
  digitalWrite(trigPin , 1);
  delay(10);
  digitalWrite(echoPin , 0);
  
  float x = pulseIn(echoPin , 1);
  float y = ((float)(340 * x ) /10000) /2;
  
    Serial.print("초음파 시간 :");
    Serial.print(x);
    Serial.print("거리 :");
    Serial.print(y);
    Serial.print("cm");
    delay(300);    
}

void stick()
{
  Serial.print("stick"); 
}

void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(button , INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  servo.attach(SERVO);
  servo.write(0);
  
  
}

void loop()
{
  int bt = digitalRead(button);
  
 while(bt==1)
 {
   servo.write(A*angle); 
   if(A==0)
   {
     LED_b();
   }
   else if(A==1)
   {
     wave();
   }
   else if(A==2)
   {
     stick();
   }
   
   A++; 
   if(A == 3)
   {
     A=0;
   }
   
   delay(1000);
}
}






