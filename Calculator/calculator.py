# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Setting up the GUI"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 727)
        self.calculation = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelresult = QtWidgets.QLabel(self.centralwidget)
        self.labelresult.setGeometry(QtCore.QRect(40, 10, 691, 81))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.labelresult.setFont(font)
        self.labelresult.setObjectName("labelresult")
        self.label7 = QtWidgets.QPushButton(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(30, 210, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.label8 = QtWidgets.QPushButton(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(160, 210, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.labelminus = QtWidgets.QPushButton(self.centralwidget)
        self.labelminus.setGeometry(QtCore.QRect(420, 210, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelminus.setFont(font)
        self.labelminus.setObjectName("labelminus")
        self.label9 = QtWidgets.QPushButton(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(290, 210, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.labelplus = QtWidgets.QPushButton(self.centralwidget)
        self.labelplus.setGeometry(QtCore.QRect(420, 330, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelplus.setFont(font)
        self.labelplus.setObjectName("labelplus")
        self.label6 = QtWidgets.QPushButton(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(290, 330, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.label4 = QtWidgets.QPushButton(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(30, 330, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QPushButton(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(160, 330, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.labeldot = QtWidgets.QPushButton(self.centralwidget)
        self.labeldot.setGeometry(QtCore.QRect(160, 570, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labeldot.setFont(font)
        self.labeldot.setObjectName("labeldot")
        self.labelplus_2 = QtWidgets.QPushButton(self.centralwidget)
        self.labelplus_2.setGeometry(QtCore.QRect(420, 450, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelplus_2.setFont(font)
        self.labelplus_2.setObjectName("labelplus_2")
        self.labelequal = QtWidgets.QPushButton(self.centralwidget)
        self.labelequal.setGeometry(QtCore.QRect(420, 570, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelequal.setFont(font)
        self.labelequal.setObjectName("labelequal")
        self.labeldivide = QtWidgets.QPushButton(self.centralwidget)
        self.labeldivide.setGeometry(QtCore.QRect(290, 570, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labeldivide.setFont(font)
        self.labeldivide.setObjectName("labeldivide")
        self.label1 = QtWidgets.QPushButton(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 450, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QPushButton(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(160, 450, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QPushButton(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(290, 450, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label0 = QtWidgets.QPushButton(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(30, 570, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label0.setFont(font)
        self.label0.setObjectName("label0")
        self.labelCE = QtWidgets.QPushButton(self.centralwidget)
        self.labelCE.setGeometry(QtCore.QRect(290, 100, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelCE.setFont(font)
        self.labelCE.setObjectName("labelCE")
        self.labelC = QtWidgets.QPushButton(self.centralwidget)
        self.labelC.setGeometry(QtCore.QRect(30, 100, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelC.setFont(font)
        self.labelC.setStyleSheet("C\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.labelC.setObjectName("labelC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        """Assings functions to different buttons"""
        self.label9.clicked.connect(lambda: self.pressed('9'))
        self.label8.clicked.connect(lambda: self.pressed('8'))
        self.label7.clicked.connect(lambda: self.pressed('7'))
        self.label6.clicked.connect(lambda: self.pressed('6'))
        self.label5.clicked.connect(lambda: self.pressed('5'))
        self.label4.clicked.connect(lambda: self.pressed('4'))
        self.label3.clicked.connect(lambda: self.pressed('3'))
        self.label2.clicked.connect(lambda: self.pressed('2'))
        self.label1.clicked.connect(lambda: self.pressed('1'))
        self.label0.clicked.connect(lambda: self.pressed('0'))
        self.label9.clicked.connect(lambda: self.pressed('9'))
        self.label9.clicked.connect(lambda: self.pressed('9'))
        self.labelminus.clicked.connect(lambda: self.pressed('-'))
        self.labelplus.clicked.connect(lambda: self.pressed('+'))
        self.labeldivide.clicked.connect(lambda: self.pressed('/'))
        self.labelplus_2.clicked.connect(lambda: self.pressed('*'))
        self.labeldot.clicked.connect(lambda: self.pressed('.'))
        self.labelequal.clicked.connect(self.equal)
        self.labelC.clicked.connect(self.clear)
        self.labelCE.clicked.connect(self.clear)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelresult.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">0</span></p></body></html>"))
        self.label7.setText(_translate("MainWindow", "7"))
        self.label8.setText(_translate("MainWindow", "8"))
        self.labelminus.setText(_translate("MainWindow", "-"))
        self.label9.setText(_translate("MainWindow", "9"))
        self.labelplus.setText(_translate("MainWindow", "+"))
        self.label6.setText(_translate("MainWindow", "6"))
        self.label4.setText(_translate("MainWindow", "4"))
        self.label5.setText(_translate("MainWindow", "5"))
        self.labeldot.setText(_translate("MainWindow", "."))
        self.labelplus_2.setText(_translate("MainWindow", "*"))
        self.labelequal.setText(_translate("MainWindow", "="))
        self.labeldivide.setText(_translate("MainWindow", "/"))
        self.label1.setText(_translate("MainWindow", "1"))
        self.label2.setText(_translate("MainWindow", "2"))
        self.label3.setText(_translate("MainWindow", "3"))
        self.label0.setText(_translate("MainWindow", "0"))
        self.labelCE.setText(_translate("MainWindow", "CE"))
        self.labelC.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">C</span></p></body></html>"))
        self.labelC.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">C</span></p></body></html>"))
        self.labelC.setText(_translate("MainWindow", "C"))

    def pressed(self, symbol):
        """Display the pressed buttons on the result label"""
        self.calculation += str(symbol)
        self.labelresult.setText(self.calculation)

    def equal(self):
        """Evaluate the numbers on the result screen and show the result of the calculations on the result label"""
        calc = eval(self.calculation)
        self.labelresult.setText(str(calc))
        self.calculation = ""

    def clear(self):
        """Clear everything from the result screen"""
        self.calculation = ""
        self.labelresult.setText(self.calculation)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
