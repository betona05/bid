import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time

form_class = uic.loadUiType("bid.ui")[0]

g2bkey = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO%2Fycyce5D%2BiMJT8IbuB5IJy4ymCtZVEeqHN7KQ%3D%3D"

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnReset.clicked.connect(self.runClear)
        self.btnSearch.clicked.connect(self.runSearch)
        self.clock()

    def runClear(self):
        self.bidNum.setText("")

    def runSearch(self):
        self.txtResult1.setText(self.bidNum.text())
 
    def clock(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.getDateTime)

    def getDateTime(self):
        self.time = QTime.currentTime()
        self.date = QDate.currentDate()        
        font1 = self.txtDate.font()
        font1.setPointSize(14)
        font2 = self.txtTime.font()
        font2.setPointSize(14)
        self.txtDate.setText(self.date.toString(Qt.DefaultLocaleShortDate))
        self.txtTime.setText(self.time.toString(Qt.DefaultLocaleLongDate))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_()) 