// C++ code
//
const unsigned int LED[8] ={2,3,4,5,6,7,8,9};

void initLed(int initValue){
  for(int i = 0 ; i < 8 ; i++){
    pinMode(LED[i] , OUTPUT); 
  };
  
  for(int i = 0 ; i < 8 ; i++){
    digitalWrite(LED[i] , initValue); 
  };
};

void setup()
{
  Serial.begin(10500);
  
}

void loop()
{
  for(int i = 0 ; i < 8 ; i++)
  {
    for(int i= 0; i<8 ; i++)
    {
     // initLed(0);
      digitalWrite(LED[i] , 0);
   	
    }
    
     digitalWrite(LED[i] , 1);
     delay(500);
    
  }
  
}