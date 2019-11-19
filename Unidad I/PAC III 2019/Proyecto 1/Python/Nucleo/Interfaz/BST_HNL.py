# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BST_HNL.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class Ui_BST_1(object):
    def setupUi(self, BST_1):
        BST_1.setObjectName("BST_1")
        BST_1.resize(650, 400)
        BST_1.setStyleSheet("background-color: rgb(211, 205, 255);")

        self.label = QtWidgets.QLabel(BST_1)
        self.label.setGeometry(QtCore.QRect(0, 0, 650, 400))
        self.label.setText("")
        self.label.setObjectName("label")
        pix = (QPixmap('Memoria/BST1.png'))
        self.label.setPixmap(pix.scaled(650, 400))
        self.label.setGeometry(0,0,650, 400)

        self.retranslateUi(BST_1)
        QtCore.QMetaObject.connectSlotsByName(BST_1)

    def retranslateUi(self, BST_1):
        _translate = QtCore.QCoreApplication.translate
        BST_1.setWindowTitle(_translate("BST_1", "Árbol Binario de Costos en Lempiras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BST_1 = QtWidgets.QWidget()
    ui = Ui_BST_1()
    ui.setupUi(BST_1)
    BST_1.show()
    sys.exit(app.exec_())

