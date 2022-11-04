from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QTextEdit, QComboBox, 
                                QSpinBox, QSlider, QProgressBar,
                                QCheckBox, QGroupBox,
                                )

from PySide2.QtGui import (
    QPixmap, QImage, QColorSpace, 
    QIntValidator, QDoubleValidator, QRegExpValidator
)

from PySide2.QtCore import Qt, QRegExp, QThread ,Signal , Slot

import sys
import serial
import time

class WorkerSumP1(QThread):

    def __init__(self, low, high, widget):
        super().__init__()

        self.low = low
        self.high = high
        self.widget:QTextEdit = widget

        # print("widget id2: ", id(self.widget))

    def run(self) -> None:

        print(f'스레드시작: {self.low}부터 {self.high}까지 더할거임')
        now = time.time()

        total = 0
        for i in range(self.low, self.high):
            total += i

        delta = time.time() - now

        resultMSG = f'스레드끝: 결과는 {total}, 걸린시간: {delta} sec'
        print(resultMSG)

        self.widget.append(resultMSG)

        pass

    pass

class CallbackHandler():
    def __init__(self):
        self.functions = []
        pass
    
    def connect(self, func):
        self.functions.append(func)
        pass
    
    def disconnect(self, func = None):
        if not func:
            self.functions.clear()
            return
        
        self.functions.remove(func)
        
        # for i in range(len(self.functions)):
        #     f = self.functions[i]
        #     if f is func:
        #         self.functions.pop(i)
        
        # for f in self.functions:
        #     #is 는 memory 비교
        #     if f is func:
        #         self.functions.remove(f)
            # pass
        pass
    
    def emit(self,*args):
        for func in self.functions:
            func(args)
            pass
        
        pass
    pass

class WorkerSumP2(QThread):
    
    # callbackSignal = pyqtSiganl(str) #qt5 
    callbackSignal = Signal(str) #pyside

    handler =  CallbackHandler()
    
    def __init__(self, low, high , callback):
        super().__init__()

        self.low = low
        self.high = high
        # self.callback = callback
        
        # callbackSignal = Signal(str)
        self.callbackSignal.connect(callback)

    def run(self) -> None:
        print(f'스레드 시작 : {self.low}부터 {self.high}까지 더할거임')
        now = time.time()
        
        total = 0 
        for i in range(self.low, self.high):
            total += i
        
        delta = time.time() - now
        resultMSG = f'스레드 끝: 결과는 {total},걸린시간: {delta} sec'
        print(resultMSG)
        
        self.callbackSignal.emit(resultMSG)
        
        self.handler.emit(resultMSG)
        pass

    pass

class WorkerSerialRead(QThread):
    def __init__(self):
        
        pass
    def run(self) -> None:
        
        pass
    pass

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.inputLineEdit = QLineEdit()
        self.printTextEdit = QTextEdit()
        self.printTextEdit.setReadOnly(True)

        self.inputLineEdit.returnPressed.connect(self.sendMessage)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.inputLineEdit)
        mainLayout.addWidget(self.printTextEdit)

        self.setLayout(mainLayout)
        self.setWindowTitle("시리얼통신")
        self.setMinimumSize(500,500)

        pass

    def sendMessage(self):
        # inputText = self.inputLineEdit.text()

        # 입력된 문구가 숫자인지 파악

        # 입력된 문구를 숫자형으로 변경

        # 입력된 숫자가 일정 범위 안에 있는지 파악

        # 숫자를 문자로 변경

        # 시리얼 통신을 통해 문자를 전달


        # 스레드 없이 메인스레드에서 더하기 함수 실행 테스트
        # self.sum(1, 100000000)

        # print("widget id1: ", id(self.printTextEdit))

        # 스레드생성 및 시작
        # self.workerSumP1 = WorkerSumP1(1, 100000000, self.printTextEdit)
        # self.workerSumP1.start()
        
        self.workerSumP2 = WorkerSumP2(1, 100000000 ,self.complete)
        self.workerSumP2.callbackSignal.connect(self.complete2)#외부 연결
        # self.workerSumP2.callbackSignal.disconnect(self.complete2)#연결 끊기
        self.workerSumP2.handler.connect(self.complete3)
        self.workerSumP2.handler.connect(self.complete4)
        self.workerSumP2.handler.connect(self.complete5)
        
        self.workerSumP2.handler.disconnect(self.complete3)
        self.workerSumP2.start()
        

        # 출력공간에 문구 추가 테스트
        # # self.printTextEdit.setText(self.printTextEdit.toPlainText() + inputText)
        # self.printTextEdit.append(inputText)


        # 입력된 문구를 초기화 (지우기)
        # print("find: ", inputText.find('\n'))
        self.inputLineEdit.setText('')

        pass
    
    def complete(self, text):
        print("complete :: text: ", text)
        self.printTextEdit.append(text)
        pass
    def complete2(self, text):
        print("complete2 :: text: ",text)
        pass
    def complete3(self, text):
        print("complete3 :: text: ", text)
        pass
    def complete4(self, text):
        print("complete4 :: text: ", text)
        pass
    def complete5(self, text):
        print("complete5 :: text: ", text)
        pass
    def sum(self, low, high):

        total = 0
        for i in range(low, high):
            total += i
        print('sum: ', total)

        # while True:
        #     total = 0
        #     for i in range(low, high):
        #         total += i
        #     print('sum: ', total)



# PORT = "COM3" #윈도우
PORT = "/dev/ttyUSB0" #리눅스, $ sudo chmod 666 /dev/ttyUSB0
BAUDRATE = 9600
# BAUDRATE = 115200

# 시리얼 포트와 통신 준비
# ser = serial.Serial(PORT, baudrate=BAUDRATE)

ser:serial.Serial = None

def prepare():
    global ser

    ser = serial.Serial(PORT, baudrate=BAUDRATE)

    pass

if __name__ == '__main__':
    # prepare()

    app = QApplication(sys.argv)
    # app.setStyleSheet("QCheckBox{font-size: 30pt;} QPushButton{font-size: 30pt;}")

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()

    pass