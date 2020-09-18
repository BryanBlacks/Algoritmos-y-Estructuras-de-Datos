# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 319)
        MainWindow.setStyleSheet("background-color: rgb(211, 205, 255);")
        self.btnAddProduct = QtWidgets.QPushButton(MainWindow)
        self.btnAddProduct.setGeometry(QtCore.QRect(50, 50, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddProduct.setFont(font)
        self.btnAddProduct.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(122, 255, 65);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.btnAddProduct.setObjectName("btnAddProduct")
        self.btnTree = QtWidgets.QPushButton(MainWindow)
        self.btnTree.setGeometry(QtCore.QRect(50, 210, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnTree.setFont(font)
        self.btnTree.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(250, 255, 139);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.btnTree.setObjectName("btnTree")
        self.btnEdit = QtWidgets.QPushButton(MainWindow)
        self.btnEdit.setGeometry(QtCore.QRect(50, 130, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnEdit.setFont(font)
        self.btnEdit.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(147, 125, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.btnEdit.setObjectName("btnEdit")
        self.btnAbout = QtWidgets.QPushButton(MainWindow)
        self.btnAbout.setGeometry(QtCore.QRect(490, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(True)
        font.setWeight(75)
        self.btnAbout.setFont(font)
        self.btnAbout.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(122, 255, 65);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:12px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.btnAbout.setObjectName("btnAbout")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(320, 60, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.lblCount = QtWidgets.QLabel(MainWindow)
        self.lblCount.setGeometry(QtCore.QRect(400, 110,200, 91))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblCount.setFont(font)
        self.lblCount.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblCount.setObjectName("lblCount")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Principal"))
        self.btnAddProduct.setText(_translate("MainWindow", "Agregar a Inventario"))
        self.btnTree.setText(_translate("MainWindow", "Arbol Binario de Costos"))
        self.btnEdit.setText(_translate("MainWindow", "Ver y Editar Inventario"))
        self.btnAbout.setText(_translate("MainWindow", "Acerca de"))
        self.label.setText(_translate("MainWindow", "Productos en Inventario"))
        self.lblCount.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

