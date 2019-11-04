# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecWin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_secondwindow(object):
        
    def setupUi(self, secondwindow):
        secondwindow.setObjectName("secondwindow")
        secondwindow.resize(400, 198)
        secondwindow.setStyleSheet("background-color: rgb(148, 255, 115);")
        self.centralwidget = QtWidgets.QWidget(secondwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(100, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(0, 0, 0);")
        self.name.setObjectName("name")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(150, 110, 99, 31))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(147, 120, 255);")
        self.createButton.setObjectName("createButton")
        self.textInsert = QtWidgets.QTextEdit(self.centralwidget)
        self.textInsert.setGeometry(QtCore.QRect(100, 50, 211, 41))
        self.textInsert.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textInsert.setObjectName("textInsert")
        secondwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(secondwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        secondwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(secondwindow)
        self.statusbar.setObjectName("statusbar")
        secondwindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondwindow)
        QtCore.QMetaObject.connectSlotsByName(secondwindow)

    def retranslateUi(self, secondwindow):
        _translate = QtCore.QCoreApplication.translate
        secondwindow.setWindowTitle(_translate("secondwindow", "SecondWindow"))
        self.name.setText(_translate("secondwindow", "Insert Name"))
        self.createButton.setText(_translate("secondwindow", "Create"))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondwindow = QtWidgets.QMainWindow()
    ui = Ui_secondwindow()
    ui.setupUi(secondwindow)
    secondwindow.show()
    sys.exit(app.exec_())"""

