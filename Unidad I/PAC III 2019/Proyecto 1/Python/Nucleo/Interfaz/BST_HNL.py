# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BST_HNL.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BST_1(object):
    def setupUi(self, BST_1):
        BST_1.setObjectName("BST_1")
        BST_1.resize(633, 319)
        BST_1.setStyleSheet("background-color: rgb(211, 205, 255);")

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

