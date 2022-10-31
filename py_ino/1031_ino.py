import serial

PORT = "/dev/ttyUSB0"
BAUDRATE = 9600

#serial 통신 준비
ser = serial.Serial(PORT, baudrate = BAUDRATE)

msg = 'Q'

while True:
    msg = input()
    
    if (msg == '0'):
        break
    ser.write(msg.encode())
    
    for c in msg:
        ser.write(c.encode(encoding='utf-8'))
    
ser.close()

# ino

# const int LED =     13;
# void setup(){
#   Serial.begin(9600);   
#   pinMode(LED , OUTPUT);                                                                                                    
# }
# void loop(){
#     while(Serial.available()){
#         char c =Serial.read();        
#         if ( c == 'Q'){
#             digitalWrite(LED , HIGH);
#             delay(500);
#             digitalWrite(LED , LOW);
#             delay(500);
#             digitalWrite(LED , HIGH);
#             delay(500);
#             digitalWrite(LED , LOW);
#             delay(500);            
#         }
#     }
# }


