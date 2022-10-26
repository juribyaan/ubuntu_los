import PySide2
import PySide2.QtCore
from PySide2.QtCore import Qt

print(PySide2.__version__)
print(PySide2.QtCore.__version__)

import sys

from PySide2.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QVBoxLayout, QWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv); 
           
    window = QWidget();
    # window.resize(1280,760)
    # window.setWindowTitle("Qt app")    
    # label = QLabel("hello Qt" , window)
    # #qt 창 안에서의 위치로 이동시킴 - 절대좌표
    # label.move(110,80)    
    
    
    labelId = QLabel('&Id :')
    #라벨 정렬
    labelId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    labelPW = QLabel("&Password: ")
    
    lineEditId = QLineEdit()
    lineEditPW = QLineEdit()
    lineEditPW.setEchoMode(QLineEdit.Password)
    
    #라벨ㅇㅇ [lineEditㅇㅇ]
    labelId.setBuddy(lineEditId)
    labelPW.setBuddy(lineEditPW)    
    
    buttonOK = QPushButton()
    buttonOK.setText("OK")   

    #레이아웃은 위젯을 포함할수 있다.
    layout_1 = QGridLayout()
    layout_1.addWidget(labelId,0,0)
    layout_1.addWidget(lineEditId,0,1)
    layout_1.addWidget(labelPW,1,0)
    layout_1.addWidget(lineEditPW,1,1)
    #----------title---------
    #       Id : [lineEditId]
    # Password : [lineEditPW]
    #모양으로 세팅
    
    # | 1 | 2 | 3 |
    layout_2 = QHBoxLayout()
    layout_2.addStretch()
    layout_2.addWidget(buttonOK)
    
    # | 1 |
    # | 2 |
    # | 3 |
    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layout_1)
    mainLayout.addLayout(layout_2)

    #window에 main을 set 함.
    window.setLayout(mainLayout)
    #창 타이틀 메시지
    window.setWindowTitle('Log in')
    # window.setWindowIcon(QIcon(":/images/ok.png"))  # 

    #buttonOK 를 clicked 했을때 전달,연결할 (app.quit) 
    buttonOK.clicked.connect(app.quit)
    
    window.show()    
    app.exec_()
