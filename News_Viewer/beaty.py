# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'truthorfalse.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import news
from selenium import webdriver
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        """Sets up the GUI for the programm"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 160, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QPushButton(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 20, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QPushButton(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 120, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QPushButton(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 220, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QPushButton(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 320, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QPushButton(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 420, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QPushButton(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 520, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QPushButton(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 620, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QPushButton(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 720, 1500, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 15, 1500, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 300, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionNew_file = QtWidgets.QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """Assings functions to different buttons"""
        self.pushButton.clicked.connect(self.pressed)
        self.label.clicked.connect(lambda: self.linkconnect(0))
        self.label_2.clicked.connect(lambda: self.linkconnect(0))
        self.label_3.clicked.connect(lambda: self.linkconnect(1))
        self.label_4.clicked.connect(lambda: self.linkconnect(2))
        self.label_5.clicked.connect(lambda: self.linkconnect(3))
        self.label_6.clicked.connect(lambda: self.linkconnect(4))
        self.label_7.clicked.connect(lambda: self.linkconnect(5))
        self.label_8.clicked.connect(lambda: self.linkconnect(6))
        self.label_8.clicked.connect(lambda: self.linkconnect(8))


    def retranslateUi(self, MainWindow):

        """"Setting up the rest of GUI"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "CNN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New York Times"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vox"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Fox News"))
        self.label.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_2.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_3.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_4.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_5.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_6.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_7.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_8.setText(_translate("MainWindow", "Please wait 30 seconds for the results to load"))
        self.label_9.setText(_translate("MainWindow", "View the latest new from:"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionNew_file.setText(_translate("MainWindow", "New file"))
        self.actionNew_file.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew_file.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def pressed(self):
        """Displaying the lastest news on the screen"""
        media = self.comboBox.currentText()

        # News from the CNN
        if media == "CNN":
            information = news.Infogetter()
            answer = information.cnn()
            self.process(answer)

        # News from the New York Times
        if media == "New York Times":
            information = news.Infogetter()
            answer = information.nytimes()
            self.process(answer)

        # News from the Vox
        if media == "Vox":
            information = news.Infogetter()
            answer = information.vox()
            self.process(answer)

        # News from the Fox News
        if media == "Fox News":
            information = news.Infogetter()
            answer = information.foxnews()
            self.process(answer)

    def linkconnect(self, number):
        """Opens a webpage with the requested news page"""

        # Sets up the Chrome browser
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        options.add_argument('--allow-running-insecure-content')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--ignore-certificate-errors')

        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        options.add_argument("--proxy-server='direct://")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument("acceptInsecureCerts")

        webdriver_path = 'C://Users//azimc//chromedriver.exe' # Enter the file directory of the Chromedriver

        # Opens up the webpage
        browser = webdriver.Chrome(webdriver_path, options=options)
        browser.get(str(self.reference[number][1]))

    def process(self, answer):

        """Displays the found information""""
        self.label.setText("Please Wait")
        self.label_2.setText(answer[0][0])
        self.label_3.setText(answer[1][0])
        self.label_4.setText(answer[2][0])
        self.label_5.setText(answer[3][0])
        self.label_6.setText(answer[4][0])
        self.label_7.setText(answer[5][0])
        self.label_8.setText(answer[6][0])
        self.reference = answer









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
