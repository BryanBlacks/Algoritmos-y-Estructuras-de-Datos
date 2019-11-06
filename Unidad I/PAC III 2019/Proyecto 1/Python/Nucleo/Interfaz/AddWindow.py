# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WinAdd(object):
    def setupUi(self, WinAdd):
        WinAdd.setObjectName("WinAdd")
        WinAdd.resize(485, 400)
        WinAdd.setStyleSheet("background-color: rgb(211, 205, 255);")
        self.txtName = QtWidgets.QTextEdit(WinAdd)
        self.txtName.setGeometry(QtCore.QRect(40, 40, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtName.setObjectName("txtName")
        self.txtPrice = QtWidgets.QTextEdit(WinAdd)
        self.txtPrice.setGeometry(QtCore.QRect(80, 120, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtPrice.setFont(font)
        self.txtPrice.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPrice.setObjectName("txtPrice")
        self.comboBox = QtWidgets.QComboBox(WinAdd)
        self.comboBox.setGeometry(QtCore.QRect(260, 120, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Nucleo/Interfaz/Imagenes/bancerahn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Nucleo/Interfaz/Imagenes/banderausa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        self.plntxtDesc = QtWidgets.QPlainTextEdit(WinAdd)
        self.plntxtDesc.setGeometry(QtCore.QRect(40, 200, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plntxtDesc.setFont(font)
        self.plntxtDesc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plntxtDesc.setObjectName("plntxtDesc")
        self.btnCanel = QtWidgets.QPushButton(WinAdd)
        self.btnCanel.setGeometry(QtCore.QRect(80, 310, 140, 60))
        self.btnCanel.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 40, 40);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.btnCanel.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Nucleo/Interfaz/Imagenes/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCanel.setIcon(icon2)
        self.btnCanel.setIconSize(QtCore.QSize(55, 55))
        self.btnCanel.setCheckable(False)
        self.btnCanel.setObjectName("btnCanel")
        self.btnAdd = QtWidgets.QPushButton(WinAdd)
        self.btnAdd.setGeometry(QtCore.QRect(260, 310, 140, 60))
        self.btnAdd.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(122, 255, 65);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.btnAdd.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Nucleo/Interfaz/Imagenes/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon3)
        self.btnAdd.setIconSize(QtCore.QSize(48, 48))
        self.btnAdd.setObjectName("btnAdd")
        self.lblName = QtWidgets.QLabel(WinAdd)
        self.lblName.setGeometry(QtCore.QRect(40, 20, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblName.setFont(font)
        self.lblName.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblName.setObjectName("lblName")
        self.lblPrice = QtWidgets.QLabel(WinAdd)
        self.lblPrice.setGeometry(QtCore.QRect(80, 100, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblPrice.setFont(font)
        self.lblPrice.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblPrice.setObjectName("lblPrice")
        self.label_3 = QtWidgets.QLabel(WinAdd)
        self.label_3.setGeometry(QtCore.QRect(260, 100, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.lblName_2 = QtWidgets.QLabel(WinAdd)
        self.lblName_2.setGeometry(QtCore.QRect(40, 180, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblName_2.setFont(font)
        self.lblName_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblName_2.setObjectName("lblName_2")

        self.retranslateUi(WinAdd)
        QtCore.QMetaObject.connectSlotsByName(WinAdd)

    def retranslateUi(self, WinAdd):
        _translate = QtCore.QCoreApplication.translate
        WinAdd.setWindowTitle(_translate("WinAdd", "Agregar a Inventario"))
        self.comboBox.setItemText(0, _translate("WinAdd", "HNL"))
        self.comboBox.setItemText(1, _translate("WinAdd", "USD"))
        self.lblName.setText(_translate("WinAdd", "Nombre del Producto"))
        self.lblPrice.setText(_translate("WinAdd", "Precio de costo"))
        self.label_3.setText(_translate("WinAdd", "Moneda"))
        self.lblName_2.setText(_translate("WinAdd", "Descripción del Producto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinAdd = QtWidgets.QWidget()
    ui = Ui_WinAdd()
    ui.setupUi(WinAdd)
    WinAdd.show()
    sys.exit(app.exec_())

