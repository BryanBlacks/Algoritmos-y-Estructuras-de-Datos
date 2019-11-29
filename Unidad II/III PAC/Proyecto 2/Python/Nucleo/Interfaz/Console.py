# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Console.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Console(object):
    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.resize(626, 319)
        Console.setStyleSheet("background-color: rgb(211, 205, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.txtMain = QtWidgets.QTextEdit(Console)
        self.txtMain.setGeometry(QtCore.QRect(10, 10, 611, 291))
        font = QtGui.QFont()
        font.setItalic(True)
        self.txtMain.setFont(font)
        self.txtMain.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-style:none")
        self.txtMain.setObjectName("txtMain")

        self.retranslateUi(Console)
        QtCore.QMetaObject.connectSlotsByName(Console)

    def retranslateUi(self, Console):
        _translate = QtCore.QCoreApplication.translate
        Console.setWindowTitle(_translate("Console", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Console = QtWidgets.QWidget()
    ui = Ui_Console()
    ui.setupUi(Console)
    Console.show()
    sys.exit(app.exec_())

