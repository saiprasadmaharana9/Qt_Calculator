# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLable = QtWidgets.QLabel(self.centralwidget)
        self.outputLable.setGeometry(QtCore.QRect(10, 10, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLable.setFont(font)
        self.outputLable.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLable.setLineWidth(2)
        self.outputLable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLable.setObjectName("outputLable")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(292, 440, 88, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget)
        self.decimalButton.setGeometry(QtCore.QRect(198, 440, 88, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(10, 440, 182, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.zeroButton.setObjectName("zeroButton")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 110, 372, 91))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.cButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.cButton.setObjectName("cButton")
        self.plusminusButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.plusminusButton.setObjectName("plusminusButton")
        self.percentButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.percentButton.setObjectName("percentButton")
        self.divideButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.divideButton.setObjectName("divideButton")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(10, 200, 372, 81))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.sevenButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.nineButton.setObjectName("nineButton")
        self.multiplyButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.multiplyButton.setObjectName("multiplyButton")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(10, 280, 372, 81))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.fourButton = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.sixButton.setObjectName("sixButton")
        self.minusButton = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"")
        self.minusButton.setObjectName("minusButton")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(10, 360, 372, 81))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.oneButton = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.threeButton.setObjectName("threeButton")
        self.addButton = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.addButton.setObjectName("addButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLable.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.divideButton.setText(_translate("MainWindow", "??"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "??"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.addButton.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

