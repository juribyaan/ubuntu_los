import serial
# import os
import time
PORT = "/dev/ttyUSB0"
BAUDRATE = 9600

#serial 통신 준비
# ser = serial.Serial(PORT, baudrate = BAUDRATE)
ser:serial.Serial = None

#시리얼 준비
def prepare():
    global ser
    ser = serial.Serial(PORT, baudrate = BAUDRATE)
    #쓰레드 설정 
    t = threading.Thread(target = sum , args = (1 , 10000000))
    #쓰레드 시작
    t.start()
    pass

def readSerial():
    while True:
        line = ser.readline().decode(input, output).replace('\n','').replace('r','')
        print('line' , line)
        time.sleep(2)
        pass    
    pass

def wrtieSerial():
    while True:
        #window
        #os.system('cls') 
        msg = input('input degree [ 0 - 180 ] , exit = q')
        if msg == 'Q' :
            break
        elif not msg.istrip('-').isdigit():
            continue
        
        angle = int(msg)
        
        if 0 > angle > 180:
           print('over, again retry') 
           time.sleep(2)
           continue
        
            
        #입력값을 바이너리가 아닌 utf-8로 다듬음
        ser.write(str(angle).encode())
        print('send', angle)
        time.sleep(2)
        
        # line = ser.readline().decode(input, output).replace('\n','').replace('r','')
        # print('line' , line)
        # time.sleep(2)
        
        pass
    pass

#Thread 에서 쓰려고 나눠놓은거
def sum(low,high):
    total = 0 
    for i in int range(low,high):
        total += i
    print('sum = ' , total)

if __name__ == '__main__':
    prepare()
    #입력을 계속 받음
    wrtieSerial()
    
    pass
    
    