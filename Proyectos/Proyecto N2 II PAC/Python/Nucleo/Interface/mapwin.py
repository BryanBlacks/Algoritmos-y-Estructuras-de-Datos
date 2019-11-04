# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class Ui_Grafo(object):
    def setupUi(self, Grafo):
        Grafo.setObjectName("Grafo")
        Grafo.resize(525, 495)
        Grafo.setStyleSheet("background-color: rgb(208, 208, 208);")
        
        self.label = QtWidgets.QLabel(Grafo)
        self.label.setGeometry(QtCore.QRect(0, 0, 525, 495))
        self.label.setText("")
        self.label.setObjectName("label")
        pix = (QPixmap('/home/benedetto/Documentos/Proyecto #2/Python/Map/map.png'))
        self.label.setPixmap(pix.scaled(525, 495))
        self.label.setGeometry(0,0,525, 495)
        self.retranslateUi(Grafo)
        QtCore.QMetaObject.connectSlotsByName(Grafo)

    def retranslateUi(self, Grafo):
        _translate = QtCore.QCoreApplication.translate
        Grafo.setWindowTitle(_translate("Grafo", "Map"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grafo = QtWidgets.QWidget()
    ui = Ui_Grafo()
    ui.setupUi(Grafo)
    Grafo.show()
    sys.exit(app.exec_())

