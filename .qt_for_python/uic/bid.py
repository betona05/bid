# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bid.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BidBETONA(object):
    def setupUi(self, BidBETONA):
        if not BidBETONA.objectName():
            BidBETONA.setObjectName(u"BidBETONA")
        BidBETONA.resize(1506, 894)
        BidBETONA.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(BidBETONA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bidTitle = QLabel(self.centralwidget)
        self.bidTitle.setObjectName(u"bidTitle")
        self.bidTitle.setGeometry(QRect(10, 10, 451, 61))
        self.bidTitle.setPixmap(QPixmap(u"bidtitle.png"))
        self.txtDate = QLabel(self.centralwidget)
        self.txtDate.setObjectName(u"txtDate")
        self.txtDate.setGeometry(QRect(20, 79, 251, 41))
        font = QFont()
        font.setFamily(u"G\ub9c8\ucf13 \uc0b0\uc2a4 TTF Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.txtDate.setFont(font)
        self.txtTime = QLabel(self.centralwidget)
        self.txtTime.setObjectName(u"txtTime")
        self.txtTime.setGeometry(QRect(280, 80, 151, 41))
        self.txtTime.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1380, 0, 121, 41))
        self.label.setPixmap(QPixmap(u"betonalogo.png"))
        self.label.setScaledContents(True)
        self.btnReset = QPushButton(self.centralwidget)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(1000, 20, 75, 41))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(10)
        self.btnReset.setFont(font1)
        self.bidNum = QLineEdit(self.centralwidget)
        self.bidNum.setObjectName(u"bidNum")
        self.bidNum.setGeometry(QRect(630, 28, 251, 31))
        font2 = QFont()
        font2.setFamily(u"ELAND \ucd08\uc774\uc2a4 Light")
        font2.setPointSize(12)
        self.bidNum.setFont(font2)
        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(900, 20, 75, 41))
        self.btnSearch.setFont(font2)
        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(540, 30, 81, 21))
        self.txtResult1 = QLineEdit(self.centralwidget)
        self.txtResult1.setObjectName(u"txtResult1")
        self.txtResult1.setGeometry(QRect(100, 150, 191, 20))
        self.txtResult1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(30, 460, 61, 21))
        self.comboBox6 = QComboBox(self.centralwidget)
        self.comboBox6.addItem("")
        self.comboBox6.addItem("")
        self.comboBox6.setObjectName(u"comboBox6")
        self.comboBox6.setGeometry(QRect(100, 300, 191, 22))
        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 180, 61, 21))
        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 210, 61, 21))
        self.label_38 = QLabel(self.centralwidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 330, 61, 21))
        self.label_39 = QLabel(self.centralwidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 430, 61, 21))
        self.label_40 = QLabel(self.centralwidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 240, 61, 21))
        self.label_41 = QLabel(self.centralwidget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 150, 61, 21))
        self.txtResult4 = QLineEdit(self.centralwidget)
        self.txtResult4.setObjectName(u"txtResult4")
        self.txtResult4.setGeometry(QRect(100, 240, 191, 20))
        self.txtResult2 = QLineEdit(self.centralwidget)
        self.txtResult2.setObjectName(u"txtResult2")
        self.txtResult2.setGeometry(QRect(100, 180, 291, 20))
        self.label_42 = QLabel(self.centralwidget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 400, 61, 21))
        self.txtResult3 = QLineEdit(self.centralwidget)
        self.txtResult3.setObjectName(u"txtResult3")
        self.txtResult3.setGeometry(QRect(100, 210, 191, 20))
        self.label_43 = QLabel(self.centralwidget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 300, 61, 21))
        self.txtResult10 = QLineEdit(self.centralwidget)
        self.txtResult10.setObjectName(u"txtResult10")
        self.txtResult10.setGeometry(QRect(100, 460, 191, 20))
        self.txtResult8 = QLineEdit(self.centralwidget)
        self.txtResult8.setObjectName(u"txtResult8")
        self.txtResult8.setGeometry(QRect(100, 400, 191, 20))
        self.txtResult5 = QLineEdit(self.centralwidget)
        self.txtResult5.setObjectName(u"txtResult5")
        self.txtResult5.setGeometry(QRect(100, 270, 191, 20))
        self.txtResult5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtResult7 = QLineEdit(self.centralwidget)
        self.txtResult7.setObjectName(u"txtResult7")
        self.txtResult7.setGeometry(QRect(100, 330, 191, 20))
        self.txtResult7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_44 = QLabel(self.centralwidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(30, 270, 61, 21))
        self.txtResult9 = QLineEdit(self.centralwidget)
        self.txtResult9.setObjectName(u"txtResult9")
        self.txtResult9.setGeometry(QRect(100, 430, 191, 20))
        self.txtBsis1 = QLineEdit(self.centralwidget)
        self.txtBsis1.setObjectName(u"txtBsis1")
        self.txtBsis1.setGeometry(QRect(430, 270, 111, 20))
        self.txtBsis1.setStyleSheet(u"")
        self.txtBsis1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(560, 480, 16, 21))
        self.txtBsis2 = QLineEdit(self.centralwidget)
        self.txtBsis2.setObjectName(u"txtBsis2")
        self.txtBsis2.setGeometry(QRect(430, 300, 111, 20))
        self.txtBsis2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(560, 420, 16, 21))
        self.txtBsis3 = QLineEdit(self.centralwidget)
        self.txtBsis3.setObjectName(u"txtBsis3")
        self.txtBsis3.setGeometry(QRect(430, 330, 111, 20))
        self.txtBsis3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBsis4 = QLineEdit(self.centralwidget)
        self.txtBsis4.setObjectName(u"txtBsis4")
        self.txtBsis4.setGeometry(QRect(430, 360, 111, 20))
        self.txtBsis4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(410, 420, 16, 21))
        self.txtBsis11 = QLineEdit(self.centralwidget)
        self.txtBsis11.setObjectName(u"txtBsis11")
        self.txtBsis11.setGeometry(QRect(580, 360, 111, 20))
        self.txtBsis11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBsis13 = QLineEdit(self.centralwidget)
        self.txtBsis13.setObjectName(u"txtBsis13")
        self.txtBsis13.setGeometry(QRect(580, 420, 111, 20))
        self.txtBsis13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(560, 450, 16, 21))
        self.txtBsis14 = QLineEdit(self.centralwidget)
        self.txtBsis14.setObjectName(u"txtBsis14")
        self.txtBsis14.setGeometry(QRect(580, 450, 111, 20))
        self.txtBsis14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBsis12 = QLineEdit(self.centralwidget)
        self.txtBsis12.setObjectName(u"txtBsis12")
        self.txtBsis12.setGeometry(QRect(580, 390, 111, 20))
        self.txtBsis12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBsis15 = QLineEdit(self.centralwidget)
        self.txtBsis15.setObjectName(u"txtBsis15")
        self.txtBsis15.setGeometry(QRect(580, 480, 111, 20))
        self.txtBsis15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtResult2_1 = QLineEdit(self.centralwidget)
        self.txtResult2_1.setObjectName(u"txtResult2_1")
        self.txtResult2_1.setGeometry(QRect(490, 150, 191, 20))
        self.txtResult2_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtResult2_3 = QLineEdit(self.centralwidget)
        self.txtResult2_3.setObjectName(u"txtResult2_3")
        self.txtResult2_3.setGeometry(QRect(490, 210, 191, 20))
        self.txtResult2_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(410, 450, 16, 21))
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(410, 360, 16, 21))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(410, 300, 16, 21))
        self.txtBsis8 = QLineEdit(self.centralwidget)
        self.txtBsis8.setObjectName(u"txtBsis8")
        self.txtBsis8.setGeometry(QRect(580, 270, 111, 20))
        self.txtBsis8.setAutoFillBackground(False)
        self.txtBsis8.setStyleSheet(u"")
        self.txtBsis8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(560, 360, 16, 21))
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(420, 210, 61, 21))
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(410, 390, 16, 21))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(430, 240, 111, 20))
        self.txtBsis7 = QLineEdit(self.centralwidget)
        self.txtBsis7.setObjectName(u"txtBsis7")
        self.txtBsis7.setGeometry(QRect(430, 450, 111, 20))
        self.txtBsis7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(560, 390, 16, 21))
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(560, 330, 16, 21))
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(420, 180, 61, 21))
        self.txtBsis5 = QLineEdit(self.centralwidget)
        self.txtBsis5.setObjectName(u"txtBsis5")
        self.txtBsis5.setGeometry(QRect(430, 390, 111, 20))
        self.txtBsis5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(420, 150, 61, 21))
        self.txtBsis9 = QLineEdit(self.centralwidget)
        self.txtBsis9.setObjectName(u"txtBsis9")
        self.txtBsis9.setGeometry(QRect(580, 300, 111, 20))
        self.txtBsis9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(560, 270, 16, 21))
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(410, 330, 16, 21))
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(560, 300, 16, 21))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(410, 270, 16, 21))
        self.txtBsis10 = QLineEdit(self.centralwidget)
        self.txtBsis10.setObjectName(u"txtBsis10")
        self.txtBsis10.setGeometry(QRect(580, 330, 111, 20))
        self.txtBsis10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBsis6 = QLineEdit(self.centralwidget)
        self.txtBsis6.setObjectName(u"txtBsis6")
        self.txtBsis6.setGeometry(QRect(430, 420, 111, 20))
        self.txtBsis6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.comboBox2_2 = QComboBox(self.centralwidget)
        self.comboBox2_2.addItem("")
        self.comboBox2_2.addItem("")
        self.comboBox2_2.setObjectName(u"comboBox2_2")
        self.comboBox2_2.setGeometry(QRect(490, 180, 191, 22))
        self.txtResult11 = QLineEdit(self.centralwidget)
        self.txtResult11.setObjectName(u"txtResult11")
        self.txtResult11.setGeometry(QRect(100, 490, 191, 20))
        self.label_45 = QLabel(self.centralwidget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(30, 490, 61, 21))
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(330, 250, 31, 51))
        self.btnPrice1 = QPushButton(self.centralwidget)
        self.btnPrice1.setObjectName(u"btnPrice1")
        self.btnPrice1.setGeometry(QRect(490, 100, 91, 41))
        self.btnPrice1.setFont(font1)
        self.txtBsisRepNum = QLineEdit(self.centralwidget)
        self.txtBsisRepNum.setObjectName(u"txtBsisRepNum")
        self.txtBsisRepNum.setGeometry(QRect(530, 520, 71, 20))
        self.txtBsisRepNum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnPrice1S = QPushButton(self.centralwidget)
        self.btnPrice1S.setObjectName(u"btnPrice1S")
        self.btnPrice1S.setGeometry(QRect(610, 520, 81, 23))
        self.labDisplay = QLabel(self.centralwidget)
        self.labDisplay.setObjectName(u"labDisplay")
        self.labDisplay.setGeometry(QRect(310, 560, 381, 151))
        self.btnRunPrices = QPushButton(self.centralwidget)
        self.btnRunPrices.setObjectName(u"btnRunPrices")
        self.btnRunPrices.setGeometry(QRect(890, 650, 181, 31))
        self.btnRunPrices.setFont(font1)
        self.txtBsisRepNum_2 = QLineEdit(self.centralwidget)
        self.txtBsisRepNum_2.setObjectName(u"txtBsisRepNum_2")
        self.txtBsisRepNum_2.setGeometry(QRect(790, 650, 71, 20))
        self.txtBsisRepNum_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnRunPrice1 = QPushButton(self.centralwidget)
        self.btnRunPrice1.setObjectName(u"btnRunPrice1")
        self.btnRunPrice1.setGeometry(QRect(810, 80, 91, 41))
        self.btnRunPrice1.setFont(font1)
        self.txtComNum = QLineEdit(self.centralwidget)
        self.txtComNum.setObjectName(u"txtComNum")
        self.txtComNum.setGeometry(QRect(720, 100, 71, 20))
        self.txtComNum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(710, 80, 91, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(720, 650, 61, 16))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(700, 140, 371, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 369, 499))
        self.listViewBidRunTitle = QListView(self.scrollAreaWidgetContents)
        self.listViewBidRunTitle.setObjectName(u"listViewBidRunTitle")
        self.listViewBidRunTitle.setGeometry(QRect(0, 0, 371, 51))
        self.listViewBidRun = QListView(self.scrollAreaWidgetContents)
        self.listViewBidRun.setObjectName(u"listViewBidRun")
        self.listViewBidRun.setGeometry(QRect(0, 50, 371, 451))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.txtBidPrice = QLineEdit(self.centralwidget)
        self.txtBidPrice.setObjectName(u"txtBidPrice")
        self.txtBidPrice.setGeometry(QRect(380, 800, 261, 51))
        font3 = QFont()
        font3.setFamily(u"ELAND \ucd08\uc774\uc2a4 Bold")
        font3.setPointSize(16)
        self.txtBidPrice.setFont(font3)
        self.txtBidPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 800, 91, 41))
        font4 = QFont()
        font4.setFamily(u"ELAND Choice")
        font4.setPointSize(18)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1210, 80, 101, 21))
        self.bidNum_2 = QLineEdit(self.centralwidget)
        self.bidNum_2.setObjectName(u"bidNum_2")
        self.bidNum_2.setGeometry(QRect(1320, 80, 151, 21))
        self.label_46 = QLabel(self.centralwidget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(1210, 110, 61, 21))
        self.txtResult8_2 = QLineEdit(self.centralwidget)
        self.txtResult8_2.setObjectName(u"txtResult8_2")
        self.txtResult8_2.setGeometry(QRect(1280, 110, 191, 20))
        self.checkBoxArm = QCheckBox(self.centralwidget)
        self.checkBoxArm.setObjectName(u"checkBoxArm")
        self.checkBoxArm.setGeometry(QRect(1400, 50, 81, 20))
        self.checkBoxArm.setToolTipDuration(-1)
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(1080, 140, 411, 501))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 409, 499))
        self.listViewResultList = QListView(self.scrollAreaWidgetContents_2)
        self.listViewResultList.setObjectName(u"listViewResultList")
        self.listViewResultList.setGeometry(QRect(0, 0, 411, 291))
        self.listViewResultListTail = QListView(self.scrollAreaWidgetContents_2)
        self.listViewResultListTail.setObjectName(u"listViewResultListTail")
        self.listViewResultListTail.setGeometry(QRect(0, 290, 411, 211))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.txtBidFirst = QLineEdit(self.centralwidget)
        self.txtBidFirst.setObjectName(u"txtBidFirst")
        self.txtBidFirst.setGeometry(QRect(880, 700, 221, 31))
        font5 = QFont()
        font5.setFamily(u"ELAND \ucd08\uc774\uc2a4 Medium")
        font5.setPointSize(12)
        self.txtBidFirst.setFont(font5)
        self.txtBidFirst.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(790, 700, 81, 31))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBidCom = QLineEdit(self.centralwidget)
        self.txtBidCom.setObjectName(u"txtBidCom")
        self.txtBidCom.setGeometry(QRect(1140, 660, 251, 31))
        font6 = QFont()
        font6.setFamily(u"ELAND \ucd08\uc774\uc2a4 Medium")
        font6.setPointSize(16)
        self.txtBidCom.setFont(font6)
        self.txtBidCom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBoxSort = QCheckBox(self.centralwidget)
        self.checkBoxSort.setObjectName(u"checkBoxSort")
        self.checkBoxSort.setGeometry(QRect(600, 120, 71, 16))
        self.txtBidEprice = QLineEdit(self.centralwidget)
        self.txtBidEprice.setObjectName(u"txtBidEprice")
        self.txtBidEprice.setGeometry(QRect(380, 730, 261, 51))
        font7 = QFont()
        font7.setFamily(u"ELAND \ucd08\uc774\uc2a4 Light")
        font7.setPointSize(16)
        self.txtBidEprice.setFont(font7)
        self.txtBidEprice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 740, 81, 41))
        font8 = QFont()
        font8.setFamily(u"ELAND Choice")
        font8.setPointSize(16)
        self.label_8.setFont(font8)
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBidCom_2 = QLineEdit(self.centralwidget)
        self.txtBidCom_2.setObjectName(u"txtBidCom_2")
        self.txtBidCom_2.setGeometry(QRect(1270, 700, 201, 31))
        self.txtBidCom_2.setFont(font5)
        self.txtBidCom_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1170, 710, 91, 21))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnAdd2 = QPushButton(self.centralwidget)
        self.btnAdd2.setObjectName(u"btnAdd2")
        self.btnAdd2.setGeometry(QRect(1090, 70, 31, 51))
        self.btnReset_2 = QPushButton(self.centralwidget)
        self.btnReset_2.setObjectName(u"btnReset_2")
        self.btnReset_2.setGeometry(QRect(910, 80, 81, 41))
        self.btnReset_2.setFont(font1)
        self.btnBidResultList = QPushButton(self.centralwidget)
        self.btnBidResultList.setObjectName(u"btnBidResultList")
        self.btnBidResultList.setGeometry(QRect(1310, 50, 75, 23))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(790, 740, 81, 31))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBidFirst_2 = QLineEdit(self.centralwidget)
        self.txtBidFirst_2.setObjectName(u"txtBidFirst_2")
        self.txtBidFirst_2.setGeometry(QRect(880, 740, 221, 31))
        self.txtBidFirst_2.setFont(font5)
        self.txtBidFirst_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBidFirst_3 = QLineEdit(self.centralwidget)
        self.txtBidFirst_3.setObjectName(u"txtBidFirst_3")
        self.txtBidFirst_3.setGeometry(QRect(880, 780, 221, 31))
        self.txtBidFirst_3.setFont(font5)
        self.txtBidFirst_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(790, 780, 81, 31))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnSearchCom = QPushButton(self.centralwidget)
        self.btnSearchCom.setObjectName(u"btnSearchCom")
        self.btnSearchCom.setGeometry(QRect(1400, 650, 75, 41))
        self.txtBidCom_3 = QLineEdit(self.centralwidget)
        self.txtBidCom_3.setObjectName(u"txtBidCom_3")
        self.txtBidCom_3.setGeometry(QRect(1270, 740, 201, 31))
        self.txtBidCom_3.setFont(font5)
        self.txtBidCom_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1170, 740, 91, 31))
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBidCom_4 = QLineEdit(self.centralwidget)
        self.txtBidCom_4.setObjectName(u"txtBidCom_4")
        self.txtBidCom_4.setGeometry(QRect(1270, 780, 201, 31))
        self.txtBidCom_4.setFont(font5)
        self.txtBidCom_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1170, 780, 91, 31))
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtBidFirst_4 = QLineEdit(self.centralwidget)
        self.txtBidFirst_4.setObjectName(u"txtBidFirst_4")
        self.txtBidFirst_4.setGeometry(QRect(880, 820, 221, 31))
        font9 = QFont()
        font9.setFamily(u"ELAND \ucd08\uc774\uc2a4 Medium")
        font9.setPointSize(10)
        self.txtBidFirst_4.setFont(font9)
        self.txtBidFirst_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(710, 820, 161, 31))
        self.label_34.setFont(font2)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_47 = QLabel(self.centralwidget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(30, 560, 61, 21))
        self.txtResult12 = QLineEdit(self.centralwidget)
        self.txtResult12.setObjectName(u"txtResult12")
        self.txtResult12.setGeometry(QRect(100, 560, 191, 20))
        self.labAresult = QLabel(self.centralwidget)
        self.labAresult.setObjectName(u"labAresult")
        self.labAresult.setGeometry(QRect(70, 610, 201, 151))
        self.checkBoxSort_2 = QCheckBox(self.centralwidget)
        self.checkBoxSort_2.setObjectName(u"checkBoxSort_2")
        self.checkBoxSort_2.setGeometry(QRect(1000, 100, 71, 16))
        self.txtResult13 = QLineEdit(self.centralwidget)
        self.txtResult13.setObjectName(u"txtResult13")
        self.txtResult13.setGeometry(QRect(100, 530, 191, 20))
        self.label_48 = QLabel(self.centralwidget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(30, 530, 61, 21))
        self.label_49 = QLabel(self.centralwidget)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(30, 370, 61, 21))
        self.txtInputDt = QLineEdit(self.centralwidget)
        self.txtInputDt.setObjectName(u"txtInputDt")
        self.txtInputDt.setGeometry(QRect(100, 370, 191, 20))
        self.txtResult1_2 = QLineEdit(self.centralwidget)
        self.txtResult1_2.setObjectName(u"txtResult1_2")
        self.txtResult1_2.setGeometry(QRect(100, 120, 311, 20))
        self.txtResult1_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_50 = QLabel(self.centralwidget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(30, 120, 61, 21))
        self.comboBox11_2 = QComboBox(self.centralwidget)
        self.comboBox11_2.addItem("")
        self.comboBox11_2.addItem("")
        self.comboBox11_2.setObjectName(u"comboBox11_2")
        self.comboBox11_2.setGeometry(QRect(320, 480, 171, 22))
        self.comboBox11_3 = QComboBox(self.centralwidget)
        self.comboBox11_3.addItem("")
        self.comboBox11_3.addItem("")
        self.comboBox11_3.addItem("")
        self.comboBox11_3.setObjectName(u"comboBox11_3")
        self.comboBox11_3.setGeometry(QRect(320, 510, 171, 22))
        self.btnBestBid = QPushButton(self.centralwidget)
        self.btnBestBid.setObjectName(u"btnBestBid")
        self.btnBestBid.setGeometry(QRect(680, 740, 91, 41))
        self.txtBsisRepNum_3 = QLineEdit(self.centralwidget)
        self.txtBsisRepNum_3.setObjectName(u"txtBsisRepNum_3")
        self.txtBsisRepNum_3.setGeometry(QRect(790, 680, 71, 20))
        self.txtBsisRepNum_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(720, 680, 61, 16))
        BidBETONA.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BidBETONA)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1506, 21))
        BidBETONA.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BidBETONA)
        self.statusbar.setObjectName(u"statusbar")
        BidBETONA.setStatusBar(self.statusbar)

        self.retranslateUi(BidBETONA)

        QMetaObject.connectSlotsByName(BidBETONA)
    # setupUi

    def retranslateUi(self, BidBETONA):
        BidBETONA.setWindowTitle(QCoreApplication.translate("BidBETONA", u"Bid BETONA", None))
        self.bidTitle.setText("")
        self.txtDate.setText(QCoreApplication.translate("BidBETONA", u"2022\ub144 6\uc6d4 22\uc77c \uc218\uc694\uc77c", None))
        self.txtTime.setText(QCoreApplication.translate("BidBETONA", u"11:00:00", None))
        self.label.setText("")
        self.btnReset.setText(QCoreApplication.translate("BidBETONA", u"\uc804\uccb4\ucd08\uae30\ud654", None))
        self.btnSearch.setText(QCoreApplication.translate("BidBETONA", u"\uac80  \uc0c9 ", None))
        self.label_33.setText(QCoreApplication.translate("BidBETONA", u"\uc870\ub2ec\uacf5\uace0\ubc88\ud638", None))
        self.label_35.setText(QCoreApplication.translate("BidBETONA", u"\uc785\ucc30\ub9c8\uac10", None))
        self.comboBox6.setItemText(0, QCoreApplication.translate("BidBETONA", u"-3 ~ +3% (\uc548\uc804\ud589\uc815\ubd80)", None))
        self.comboBox6.setItemText(1, QCoreApplication.translate("BidBETONA", u"-2 ~ +2% (\uc870\ub2ec\uccad,\uacf5\uae30\uc5c5)", None))

        self.label_36.setText(QCoreApplication.translate("BidBETONA", u"\uacf5 \uace0  \uba85", None))
        self.label_37.setText(QCoreApplication.translate("BidBETONA", u"\uacf5\uace0\uae30\uad00", None))
        self.label_38.setText(QCoreApplication.translate("BidBETONA", u"\ub099  \ucc30  \uc728", None))
        self.label_39.setText(QCoreApplication.translate("BidBETONA", u"\uc785\ucc30\uc2dc\uc791", None))
        self.label_40.setText(QCoreApplication.translate("BidBETONA", u"\uacc4\uc57d\ubc29\ubc95", None))
        self.label_41.setText(QCoreApplication.translate("BidBETONA", u"\uacf5\uace0\ubc88\ud638", None))
        self.label_42.setText(QCoreApplication.translate("BidBETONA", u"\uac1c\ucc30\uc77c\uc2dc", None))
        self.label_43.setText(QCoreApplication.translate("BidBETONA", u"\uc608\uac00\ubc94\uc704", None))
        self.label_44.setText(QCoreApplication.translate("BidBETONA", u"\uae30\ucd08\uae08\uc561", None))
        self.label_32.setText(QCoreApplication.translate("BidBETONA", u"15", None))
        self.label_30.setText(QCoreApplication.translate("BidBETONA", u"13", None))
        self.label_23.setText(QCoreApplication.translate("BidBETONA", u"6", None))
        self.label_31.setText(QCoreApplication.translate("BidBETONA", u"14", None))
        self.label_24.setText(QCoreApplication.translate("BidBETONA", u"7", None))
        self.label_18.setText(QCoreApplication.translate("BidBETONA", u"4", None))
        self.label_16.setText(QCoreApplication.translate("BidBETONA", u"2", None))
        self.label_28.setText(QCoreApplication.translate("BidBETONA", u"11", None))
        self.label_21.setText(QCoreApplication.translate("BidBETONA", u"\ub099  \ucc30  \uc728", None))
        self.label_22.setText(QCoreApplication.translate("BidBETONA", u"5", None))
        self.label_10.setText(QCoreApplication.translate("BidBETONA", u"\uc608\ube44\uac00\uaca9 \uc0b0\ucd9c\uacb0\uacfc", None))
        self.label_29.setText(QCoreApplication.translate("BidBETONA", u"12", None))
        self.label_27.setText(QCoreApplication.translate("BidBETONA", u"10", None))
        self.label_20.setText(QCoreApplication.translate("BidBETONA", u"\uc608\uac00\ubc94\uc704", None))
        self.label_19.setText(QCoreApplication.translate("BidBETONA", u"\uae30\ucd08\uae08\uc561", None))
        self.label_25.setText(QCoreApplication.translate("BidBETONA", u"8", None))
        self.label_17.setText(QCoreApplication.translate("BidBETONA", u"3", None))
        self.label_26.setText(QCoreApplication.translate("BidBETONA", u"9", None))
        self.label_15.setText(QCoreApplication.translate("BidBETONA", u"1", None))
        self.comboBox2_2.setItemText(0, QCoreApplication.translate("BidBETONA", u"-3 ~ +3% (\uc548\uc804\ud589\uc815\ubd80)", None))
        self.comboBox2_2.setItemText(1, QCoreApplication.translate("BidBETONA", u"-2 ~ +2% (\uc870\ub2ec\uccad,\uacf5\uae30\uc5c5)", None))

        self.label_45.setText(QCoreApplication.translate("BidBETONA", u"\uc885\ubaa9\uad6c\ubd84", None))
        self.btnAdd.setText(QCoreApplication.translate("BidBETONA", u">>", None))
        self.btnPrice1.setText(QCoreApplication.translate("BidBETONA", u"\uc608\uac00\uc0b0\ucd9c", None))
        self.txtBsisRepNum.setText(QCoreApplication.translate("BidBETONA", u"10", None))
        self.btnPrice1S.setText(QCoreApplication.translate("BidBETONA", u"\ubc88 \ubc18\ubcf5\uc0b0\ucd9c", None))
        self.labDisplay.setText("")
        self.btnRunPrices.setText(QCoreApplication.translate("BidBETONA", u"\ubc18\ubcf5\uc0b0\ucd9c", None))
        self.txtBsisRepNum_2.setText(QCoreApplication.translate("BidBETONA", u"5", None))
        self.btnRunPrice1.setText(QCoreApplication.translate("BidBETONA", u"\uc0b0\ucd9c", None))
        self.txtComNum.setText(QCoreApplication.translate("BidBETONA", u"50", None))
        self.label_2.setText(QCoreApplication.translate("BidBETONA", u"\ucc38\uc5ec\uc608\uc0c1\uc5c5\uccb4\uc218", None))
        self.label_3.setText(QCoreApplication.translate("BidBETONA", u"\ubc18 \ubcf5 \ud69f \uc218", None))
        self.label_4.setText(QCoreApplication.translate("BidBETONA", u"\ud22c\ucc30\uac00\uaca9", None))
        self.label_5.setText(QCoreApplication.translate("BidBETONA", u"\uac1c\ucc30\uc54c\ub9bc\uacf5\uace0\ubc88\ud638", None))
        self.label_46.setText(QCoreApplication.translate("BidBETONA", u"\uac1c\ucc30\uc77c\uc2dc", None))
        self.checkBoxArm.setText(QCoreApplication.translate("BidBETONA", u"\uc54c\ub9bc\uc124\uc815", None))
        self.label_6.setText(QCoreApplication.translate("BidBETONA", u"\ub099\ucc30\uc5c5\uccb4\uba85", None))
        self.checkBoxSort.setText(QCoreApplication.translate("BidBETONA", u"\uc815\ub82c\ud558\uae30", None))
        self.label_8.setText(QCoreApplication.translate("BidBETONA", u"\uc608\uc815\uac00\uaca9", None))
        self.label_9.setText(QCoreApplication.translate("BidBETONA", u"\ud22c\ucc30\uc21c\uc704", None))
        self.btnAdd2.setText(QCoreApplication.translate("BidBETONA", u">>", None))
        self.btnReset_2.setText(QCoreApplication.translate("BidBETONA", u"\uc0b0\ucd9c\ucd08\uae30\ud654", None))
        self.btnBidResultList.setText(QCoreApplication.translate("BidBETONA", u"\uac1c\ucc30\ud655\uc778", None))
        self.label_11.setText(QCoreApplication.translate("BidBETONA", u"\ub300\ud45c\uc774\uc0ac", None))
        self.label_12.setText(QCoreApplication.translate("BidBETONA", u"\ub099\ucc30\uae08\uc561", None))
        self.btnSearchCom.setText(QCoreApplication.translate("BidBETONA", u"\uc5c5\uccb4\uac80\uc0c9", None))
        self.label_13.setText(QCoreApplication.translate("BidBETONA", u"\uac80\uc0c9\uc5c5\uccb4\uba85", None))
        self.label_14.setText(QCoreApplication.translate("BidBETONA", u"\ud22c\ucc30\uae08\uc561", None))
        self.label_34.setText(QCoreApplication.translate("BidBETONA", u"\uc608\uc815\uac00\uaca9(\ucd5c\uc801\ub099\ucc30\uac00)", None))
        self.label_47.setText(QCoreApplication.translate("BidBETONA", u"A \uac12", None))
        self.txtResult12.setText("")
        self.labAresult.setText("")
        self.checkBoxSort_2.setText(QCoreApplication.translate("BidBETONA", u"\uc815\ub82c\ud558\uae30", None))
        self.txtResult13.setText("")
        self.label_48.setText(QCoreApplication.translate("BidBETONA", u"\uc21c\uacf5\uc0ac\uc6d0\uac00", None))
        self.label_49.setText(QCoreApplication.translate("BidBETONA", u"\uacf5\uace0\uc77c\uc790", None))
        self.label_50.setText(QCoreApplication.translate("BidBETONA", u"\uacf5\uace0\uc6d0\ubb38", None))
        self.comboBox11_2.setItemText(0, QCoreApplication.translate("BidBETONA", u"\uc804\uae30.\ud1b5\uc2e0.\uc18c\ubc29.\ubb38\ud654\uc7ac\uacf5\uc0ac", None))
        self.comboBox11_2.setItemText(1, QCoreApplication.translate("BidBETONA", u"\uc885\ud569\uc804\ubb38\uacf5\uc0ac", None))

        self.comboBox11_3.setItemText(0, QCoreApplication.translate("BidBETONA", u"\uae30\uc220\uc6a9\uc5ed", None))
        self.comboBox11_3.setItemText(1, QCoreApplication.translate("BidBETONA", u"\uc2dc\uc124\uc774\uc678\uc6a9\uc5ed", None))
        self.comboBox11_3.setItemText(2, QCoreApplication.translate("BidBETONA", u"\uc2dc\uc124\uc6a9\uc5ed", None))

        self.btnBestBid.setText(QCoreApplication.translate("BidBETONA", u"\ucd5c\uc801\uc0b0\ucd9c \ucc3e\uae30", None))
        self.txtBsisRepNum_3.setText(QCoreApplication.translate("BidBETONA", u"0", None))
        self.label_7.setText(QCoreApplication.translate("BidBETONA", u"\uc608 \uac00 \ubc14 \uafc8", None))
    # retranslateUi

