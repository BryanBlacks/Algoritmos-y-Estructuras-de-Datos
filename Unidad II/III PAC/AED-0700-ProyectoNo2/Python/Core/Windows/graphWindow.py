# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Graph(object):
    def __init__(self):
        self.windowSizeX = 1000
        self.windowSizeY = 512

    def setupUi(self, graph):
        graph.setObjectName("graph")
        graph.resize(self.windowSizeX, self.windowSizeY)
        graph.setMinimumSize(QtCore.QSize(self.windowSizeX, self.windowSizeY))
        graph.setMaximumSize(QtCore.QSize(self.windowSizeX, self.windowSizeY))
        graph.setStyleSheet("background-color: rgb(252, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(graph)
        self.centralwidget.setObjectName("centralwidget")
        graph.setCentralWidget(self.centralwidget)

        self.retranslateUi(graph)
        QtCore.QMetaObject.connectSlotsByName(graph)

    def retranslateUi(self, graph):
        _translate = QtCore.QCoreApplication.translate
        graph.setWindowTitle(_translate("graph", "Sistema gestor de archivos"))
