# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BST_USD.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BST_2(object):
    def setupUi(self, BST_2):
        BST_2.setObjectName("BST_2")
        BST_2.resize(633, 319)
        BST_2.setStyleSheet("background-color: rgb(211, 205, 255);")

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

