from tokenize import group
import PySide2
import PySide2.QtCore
from PySide2.QtCore import Qt
print(PySide2.__version__)
print(PySide2.QtCore.__version__)

import sys
from PySide2.QtWidgets import *

class Myform(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self,parent);
        self.setWindowTitle("&Button Demo");
        
        self.button = QPushButton("OK", self);
        self.button.clicked.connect(self.okButtonClicked);
        
        self.checkBox = QCheckBox('체크박스 테스트', self);
        self.checkBox.toggled.connect(self.onCaseSensitivity);
        
        box = QGroupBox("Sex", self);
        self.nameLabel1 =QLabel()
        
        self.button1 = QRadioButton("Male", box)
        self.button2 = QRadioButton("Female", box)
        self.button3 = QRadioButton("Other", box)
        self.button1.setChecked(True)
        
        groupBoxLayout = QVBoxLayout(box)
        groupBoxLayout.addWidget(self.button1)
        groupBoxLayout.addWidget(self.button2)
        groupBoxLayout.addWidget(self.button3)
        self.button1.toggled.connect(self.onMale)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.checkBox)
        mainLayout.addWidget(box)
        
        self.setLayout(mainLayout)
        
    
    def okButtonClicked(self):
        self.nameLabel1.setText()
        print("okbuttonClicked")
    
    def onCaseSensitivity(self,toggle):
        print("onCaseSensitivity",toggle)
        print(self.checkBox.isCheckable())
    
    def onMale(self,toggle):
        print("onMale",toggle)   


if __name__ == '__main__':
    app = QApplication(sys.argv); 
    window = QWidget();
    
    form = Myform()
    
    #한번 출력해주고
    form.show()
    
    form.button.setText("ok바꿈")
    # window.show()   
    
    #흐름제어 
    app.exec_()
