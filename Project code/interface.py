import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

from PyQt5 import QtCore, QtGui, QtWidgets

from splashh import SplashScreen
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Virtual Try on")
        MainWindow.resize(1089, 782)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color:#000;\n"
"border:none;\n"
"}\n"
"#centralwidget{\n"
"background-color:#eff9fe;\n"
"}\n"
"#leftmenu{\n"
"background-color:#2596be;\n"
"}\n"
"#QLineEdit{\n"
"background:transperent;\n"
"}\n"
"#searchframe{\n"
"border-radius:10px;\n"
"border:2px solid #2596be;\n"
"}\n"
"#appheader{\n"
"color: #2596be;\n"
"}\n"
"#card1,#card2,#card3,#card4{\n"
"background-color:#fefeff\n"
";\n"
"border-radius:25px;\n"
"\n"
"}\n"
"#pushButton,#pushButton_2,#pushButton_3{\n"
"background-color:#2596be;\n"
"color:#fff;\n"
"border-radius:10px;\n"
"}\n"
"#widget_7,#widget_5,#widget_4,#label_8{\n"
"background-color:#fefeff;\n"
"border-radius:25px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mainbody = QtWidgets.QWidget(self.centralwidget)
        self.mainbody.setAutoFillBackground(False)
        self.mainbody.setObjectName("mainbody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainbody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainbody)
        self.headerFrame.setAutoFillBackground(False)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.widget)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/blueIcons/icons/blue/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_3.addWidget(self.menuBtn, 0, QtCore.Qt.AlignTop)
        self.appheader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.appheader.setFont(font)
        self.appheader.setObjectName("appheader")
        self.horizontalLayout_3.addWidget(self.appheader)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.widget_2 = QtWidgets.QWidget(self.headerFrame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.acoountbtn = QtWidgets.QPushButton(self.widget_2)
        self.acoountbtn.setMinimumSize(QtCore.QSize(24, 24))
        self.acoountbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.acoountbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/blueIcons/icons/blue/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acoountbtn.setIcon(icon1)
        self.acoountbtn.setIconSize(QtCore.QSize(32, 32))
        self.acoountbtn.setObjectName("acoountbtn")
        self.horizontalLayout_6.addWidget(self.acoountbtn, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.cardsFrame = QtWidgets.QWidget(self.mainbody)
        self.cardsFrame.setObjectName("cardsFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.card2 = QtWidgets.QFrame(self.cardsFrame)
        self.card2.setMinimumSize(QtCore.QSize(160, 0))
        self.card2.setMaximumSize(QtCore.QSize(16777215, 158))
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home = QtWidgets.QFrame(self.card2)
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home.setObjectName("home")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.home)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.home)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.home)
        self.label_3.setMinimumSize(QtCore.QSize(40, 40))
        self.label_3.setMaximumSize(QtCore.QSize(40, 40))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/blueIcons/icons/blue/home.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.home, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card2)
        self.card1 = QtWidgets.QFrame(self.cardsFrame)
        self.card1.setMinimumSize(QtCore.QSize(160, 0))
        self.card1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tryon = QtWidgets.QFrame(self.card1)
        self.tryon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tryon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tryon.setObjectName("tryon")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tryon)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.tryon)
        self.label_5.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.tryon)
        self.label_6.setMinimumSize(QtCore.QSize(40, 40))
        self.label_6.setMaximumSize(QtCore.QSize(40, 40))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/blueIcons/icons/blue/aperture.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.tryon, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card1)
        self.card4 = QtWidgets.QFrame(self.cardsFrame)
        self.card4.setMinimumSize(QtCore.QSize(160, 0))
        self.card4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contactus = QtWidgets.QFrame(self.card4)
        self.contactus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contactus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contactus.setObjectName("contactus")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.contactus)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.contactus)
        self.label_12.setMinimumSize(QtCore.QSize(40, 40))
        self.label_12.setMaximumSize(QtCore.QSize(46, 40))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/blueIcons/icons/blue/phone-call.svg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.contactus)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.verticalLayout_5.addWidget(self.contactus)
        self.horizontalLayout_7.addWidget(self.card4)
        self.verticalLayout.addWidget(self.cardsFrame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.mainbody, 0, QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setObjectName("widget_3")
        self.glasses = QtWidgets.QFrame(self.widget_3)
        self.glasses.setGeometry(QtCore.QRect(0, 0, 791, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses.sizePolicy().hasHeightForWidth())
        self.glasses.setSizePolicy(sizePolicy)
        self.glasses.setAutoFillBackground(False)
        self.glasses.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.glasses.setFrameShadow(QtWidgets.QFrame.Raised)
        self.glasses.setObjectName("glasses")
        self.widget_5 = QtWidgets.QWidget(self.glasses)
        self.widget_5.setGeometry(QtCore.QRect(30, 50, 141, 171))
        self.widget_5.setObjectName("widget_5")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 140, 141))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/blueIcons/glass1.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.widget_7 = QtWidgets.QWidget(self.glasses)
        self.widget_7.setGeometry(QtCore.QRect(190, 50, 141, 171))
        self.widget_7.setObjectName("widget_7")
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/blueIcons/glass.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.widget_4 = QtWidgets.QWidget(self.glasses)
        self.widget_4.setGeometry(QtCore.QRect(370, 50, 141, 171))
        self.widget_4.setObjectName("widget_4")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/blueIcons/glass2.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.glasses)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.glasses)
        self.pushButton.setGeometry(QtCore.QRect(50, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.glasses)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 240, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.glasses)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 240, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_8 = QtWidgets.QWidget(self.glasses)
        self.widget_8.setGeometry(QtCore.QRect(540, 50, 141, 171))
        self.widget_8.setStyleSheet("#widget_8{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;}")
        self.widget_8.setObjectName("widget_8")
        self.label_10 = QtWidgets.QLabel(self.widget_8)
        self.label_10.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/blueIcons/glass3.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.glasses)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 240, 93, 28))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"background-color: rgb(0, 150, 195);\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.accessories = QtWidgets.QFrame(self.widget_3)
        self.accessories.setGeometry(QtCore.QRect(0, 280, 791, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accessories.sizePolicy().hasHeightForWidth())
        self.accessories.setSizePolicy(sizePolicy)
        self.accessories.setMaximumSize(QtCore.QSize(791, 271))
        self.accessories.setAutoFillBackground(False)
        self.accessories.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accessories.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accessories.setObjectName("accessories")
        self.label_4 = QtWidgets.QLabel(self.accessories)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.widget_9 = QtWidgets.QWidget(self.accessories)
        self.widget_9.setGeometry(QtCore.QRect(30, 40, 140, 171))
        self.widget_9.setMinimumSize(QtCore.QSize(140, 171))
        self.widget_9.setAutoFillBackground(False)
        self.widget_9.setStyleSheet("#widget_9{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;}")
        self.widget_9.setObjectName("widget_9")
        self.label_13 = QtWidgets.QLabel(self.widget_9)
        self.label_13.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/blueIcons/necklac1.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.widget_10 = QtWidgets.QWidget(self.accessories)
        self.widget_10.setGeometry(QtCore.QRect(210, 40, 141, 171))
        self.widget_10.setStyleSheet("#widget_10{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;}")
        self.widget_10.setObjectName("widget_10")
        self.label_14 = QtWidgets.QLabel(self.widget_10)
        self.label_14.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/blueIcons/necklace 2.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.widget_11 = QtWidgets.QWidget(self.accessories)
        self.widget_11.setGeometry(QtCore.QRect(380, 40, 141, 171))
        self.widget_11.setStyleSheet("#widget_11{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;}")
        self.widget_11.setObjectName("widget_11")
        self.label_15 = QtWidgets.QLabel(self.widget_11)
        self.label_15.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/blueIcons/necklace 3.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.widget_12 = QtWidgets.QWidget(self.accessories)
        self.widget_12.setGeometry(QtCore.QRect(550, 40, 141, 171))
        self.widget_12.setStyleSheet("#widget_12{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;}")
        self.widget_12.setObjectName("widget_12")
        self.label_16 = QtWidgets.QLabel(self.widget_12)
        self.label_16.setGeometry(QtCore.QRect(0, 20, 140, 141))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/blueIcons/necklace 4.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.pushButton_5 = QtWidgets.QPushButton(self.accessories)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 230, 93, 28))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"background-color: rgb(0, 150, 195);\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.accessories)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 230, 93, 28))
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"background-color: rgb(0, 150, 195);\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.accessories)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 230, 93, 28))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"background-color: rgb(0, 150, 195);\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.accessories)
        self.pushButton_8.setGeometry(QtCore.QRect(580, 230, 93, 28))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"background-color: rgb(0, 150, 195);\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setGeometry(QtCore.QRect(800, 0, 251, 571))
        self.widget_6.setMinimumSize(QtCore.QSize(241, 571))
        self.widget_6.setAutoFillBackground(False)
        self.widget_6.setObjectName("widget_6")
        self.widget_13 = QtWidgets.QWidget(self.widget_6)
        self.widget_13.setGeometry(QtCore.QRect(0, 10, 251, 261))
        self.widget_13.setAutoFillBackground(False)
        self.widget_13.setObjectName("widget_13")
        self.label_17 = QtWidgets.QLabel(self.widget_13)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 251, 261))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/blueIcons/model3.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.widget_14 = QtWidgets.QWidget(self.widget_6)
        self.widget_14.setGeometry(QtCore.QRect(0, 290, 251, 261))
        self.widget_14.setAutoFillBackground(False)
        self.widget_14.setObjectName("widget_14")
        self.label_18 = QtWidgets.QLabel(self.widget_14)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 251, 261))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/blueIcons/model.jpg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appheader.setText(_translate("MainWindow", "Virtual Try on"))
        self.label.setText(_translate("MainWindow", "              HOME"))
        self.label_5.setText(_translate("MainWindow", "      TRY ON"))
        self.label_11.setText(_translate("MainWindow", "     CONTACT US"))
        self.label_2.setText(_translate("MainWindow", "GLASSES"))
        self.pushButton.setText(_translate("MainWindow", "Try on"))
        self.pushButton_2.setText(_translate("MainWindow", "Try on"))
        self.pushButton_3.setText(_translate("MainWindow", "Try on"))
        self.pushButton_4.setText(_translate("MainWindow", "Try on"))
        self.label_4.setText(_translate("MainWindow", "ACCESSORIES"))
        self.pushButton_5.setText(_translate("MainWindow", "Try on"))
        self.pushButton_6.setText(_translate("MainWindow", "Try on"))
        self.pushButton_7.setText(_translate("MainWindow", "Try on"))
        self.pushButton_8.setText(_translate("MainWindow", "Try on"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    splash = SplashScreen()
    splash.show()
    splash.setStyleSheet(''' #LabelTitle {
            font-size: 60px;
            color: #93deed;
        }

        #LabelDesc {
            font-size: 30px;
            color: #c2ced1;
        }

        #LabelLoading {
            font-size: 30px;
            color: #e8e8eb;
        }

        QFrame {
            background-color: #2F4454;
            color: rgb(220, 220, 220);
        }

        QProgressBar {
            background-color: #DA7B93;
            color: rgb(200, 200, 200);
            border-style: none;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
        }

        QProgressBar::chunk {
            border-radius: 10px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
        }
    '''
    )
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: MainWindow.show())
    timer.start(10000)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    sys.exit(app.exec_())
