# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WinAbout(object):
    def setupUi(self, WinAbout):
        WinAbout.setObjectName("WinAbout")
        WinAbout.resize(395, 230)
        WinAbout.setStyleSheet("background-color: rgb(211, 205, 255);")
        self.LblGerson = QtWidgets.QLabel(WinAbout)
        self.LblGerson.setGeometry(QtCore.QRect(20, 110, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.LblGerson.setFont(font)
        self.LblGerson.setObjectName("LblGerson")
        self.LblNames = QtWidgets.QLabel(WinAbout)
        self.LblNames.setEnabled(True)
        self.LblNames.setGeometry(QtCore.QRect(50, 20, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LblNames.setFont(font)
        self.LblNames.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.LblNames.setObjectName("LblNames")
        self.LblInfoClass = QtWidgets.QLabel(WinAbout)
        self.LblInfoClass.setGeometry(QtCore.QRect(20, 180, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.LblInfoClass.setFont(font)
        self.LblInfoClass.setStyleSheet("color: rgb(0, 0, 0);")
        self.LblInfoClass.setObjectName("LblInfoClass")
        self.LblBryan = QtWidgets.QLabel(WinAbout)
        self.LblBryan.setGeometry(QtCore.QRect(20, 60, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LblBryan.setFont(font)
        self.LblBryan.setObjectName("LblBryan")
        self.LblEdgar = QtWidgets.QLabel(WinAbout)
        self.LblEdgar.setGeometry(QtCore.QRect(20, 90, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.LblEdgar.setFont(font)
        self.LblEdgar.setObjectName("LblEdgar")
        self.LblEdgarAccount = QtWidgets.QLabel(WinAbout)
        self.LblEdgarAccount.setGeometry(QtCore.QRect(270, 90, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.LblEdgarAccount.setFont(font)
        self.LblEdgarAccount.setObjectName("LblEdgarAccount")
        self.lblBryanAccount = QtWidgets.QLabel(WinAbout)
        self.lblBryanAccount.setGeometry(QtCore.QRect(270, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.lblBryanAccount.setFont(font)
        self.lblBryanAccount.setObjectName("lblBryanAccount")
        self.LblGersonAccount = QtWidgets.QLabel(WinAbout)
        self.LblGersonAccount.setGeometry(QtCore.QRect(270, 120, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.LblGersonAccount.setFont(font)
        self.LblGersonAccount.setObjectName("LblGersonAccount")

        self.retranslateUi(WinAbout)
        QtCore.QMetaObject.connectSlotsByName(WinAbout)

    def retranslateUi(self, WinAbout):
        _translate = QtCore.QCoreApplication.translate
        WinAbout.setWindowTitle(_translate("WinAbout", "About"))
        self.LblGerson.setText(_translate("WinAbout", "<html><head/><body><p>Gerson Adalid Murillo</p></body></html>"))
        self.LblNames.setText(_translate("WinAbout", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Integrantes del equipo</span></p><p align=\"center\"><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.LblInfoClass.setText(_translate("WinAbout", "<html><head/><body><p>AED proyecto N°1 III-PAC 2019</p></body></html>"))
        self.LblBryan.setText(_translate("WinAbout", "<html><head/><body><p>Bryan Josue Gonzales </p></body></html>"))
        self.LblEdgar.setText(_translate("WinAbout", "<html><head/><body><p>Edgar Josue Benedetto</p></body></html>"))
        self.LblEdgarAccount.setText(_translate("WinAbout", "<html><head/><body><p><span style=\" font-style:italic;\">20171033802</span></p></body></html>"))
        self.lblBryanAccount.setText(_translate("WinAbout", "<html><head/><body><p><span style=\" font-style:italic;\">20141001209</span></p><p><span style=\" font-style:italic;\"><br/></span></p></body></html>"))
        self.LblGersonAccount.setText(_translate("WinAbout", "<html><head/><body><p><span style=\" font-style:italic;\">20181001777</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinAbout = QtWidgets.QWidget()
    ui = Ui_WinAbout()
    ui.setupUi(WinAbout)
    WinAbout.show()
    sys.exit(app.exec_())

