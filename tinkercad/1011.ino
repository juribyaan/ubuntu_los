
const int LED =13;
void setup()
{
  Serial.begin(10500);
  pinMode(LED, OUTPUT);
}

void loop()
{
  //for(int i=0; i<=10 ;i++){
  //	digitalWrite(LED,HIGH);
  //  delay(i*300);
  //  digitalWrite(LED, LOW);
  //  delay((10-i)*300);
  //};
  
  int i = 1;
  int m = 200;
  while(i<11){
    digitalWrite(LED, HIGH);
    
    delay(i*100);
    digitalWrite(LED,  LOW); 
    
    delay(i*100);
    i++;
    	}
}