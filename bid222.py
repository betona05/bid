import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import *
# from selenium import wedriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import requests

# url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
# params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'type' : 'json', 'bidNtceBgnDt' : '201712010000', 'bidNtceEndDt' : '201712312359' }

# response = requests.get(url, params=params)
# print(response.content)

form_class = uic.loadUiType("bid2.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()

        self.clock()
        self.btnSearch.clicked.connect(self.selfSearch)
        self.btnClear.clicked.connect(self.editClear)

    def clock(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.getDateTime)

    def getDateTime(self):
        self.time = QTime.currentTime()
        self.date = QDate.currentDate()        
        font1 = self.textDate.font()
        font1.setPointSize(14)
        font2 = self.textTime.font()
        font2.setPointSize(14)
        self.textDate.setText(self.date.toString(Qt.DefaultLocaleShortDate))
        self.textTime.setText(self.time.toString(Qt.DefaultLocaleLongDate))

    def editClear(self):
        self.bidNum.setText("")

    def selfSearch(self):
        self.txtResult5_2.setText(self.bidNum)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_()) 

    