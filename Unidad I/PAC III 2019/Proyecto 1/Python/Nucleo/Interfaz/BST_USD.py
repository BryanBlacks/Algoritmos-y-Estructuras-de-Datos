# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BST_USD.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class Ui_BST_2(object):
    def setupUi(self, BST_2):
        BST_2.setObjectName("BST_2")
        BST_2.resize(640, 480)
        BST_2.setStyleSheet("background-color: rgb(211, 205, 255);")

        self.label = QtWidgets.QLabel(BST_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label.setText("")
        self.label.setObjectName("label")
        pix = (QPixmap('Memoria/BST2.png'))
        self.label.setPixmap(pix.scaled(640, 480))
        self.label.setGeometry(0,0,640, 480)

        self.retranslateUi(BST_2)
        QtCore.QMetaObject.connectSlotsByName(BST_2)

    def retranslateUi(self, BST_2):
        _translate = QtCore.QCoreApplication.translate
        BST_2.setWindowTitle(_translate("BST_2", "Árbol Binario de Costos en Dolares Americanos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BST_2 = QtWidgets.QWidget()
    ui = Ui_BST_2()
    ui.setupUi(BST_2)
    BST_2.show()
    sys.exit(app.exec_())

