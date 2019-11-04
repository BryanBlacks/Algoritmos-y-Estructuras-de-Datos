# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proyectoAED.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(624, 780)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ver_rutaOrigen = QtGui.QLineEdit(self.centralwidget)
        self.ver_rutaOrigen.setGeometry(QtCore.QRect(0, 10, 411, 31))
        self.ver_rutaOrigen.setObjectName(_fromUtf8("ver_rutaOrigen"))
        self.sel_rutaOrigen = QtGui.QToolButton(self.centralwidget)
        self.sel_rutaOrigen.setGeometry(QtCore.QRect(420, 10, 71, 31))
        self.sel_rutaOrigen.setObjectName(_fromUtf8("sel_rutaOrigen"))
        self.encriptar = QtGui.QPushButton(self.centralwidget)
        self.encriptar.setGeometry(QtCore.QRect(430, 120, 171, 27))
        self.encriptar.setObjectName(_fromUtf8("encriptar"))
        self.desencriptar = QtGui.QPushButton(self.centralwidget)
        self.desencriptar.setGeometry(QtCore.QRect(430, 420, 171, 27))
        self.desencriptar.setObjectName(_fromUtf8("desencriptar"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 50, 411, 411))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.ver_rutaDestino = QtGui.QLineEdit(self.centralwidget)
        self.ver_rutaDestino.setGeometry(QtCore.QRect(0, 480, 411, 31))
        self.ver_rutaDestino.setObjectName(_fromUtf8("ver_rutaDestino"))
        self.sel_rutaDestino = QtGui.QToolButton(self.centralwidget)
        self.sel_rutaDestino.setGeometry(QtCore.QRect(420, 480, 71, 31))
        self.sel_rutaDestino.setObjectName(_fromUtf8("sel_rutaDestino"))
        self.sel_algoritmo = QtGui.QComboBox(self.centralwidget)
        self.sel_algoritmo.setGeometry(QtCore.QRect(430, 70, 181, 27))
        self.sel_algoritmo.setObjectName(_fromUtf8("sel_algoritmo"))
        self.sel_algoritmo.addItem(_fromUtf8(""))
        self.sel_algoritmo.addItem(_fromUtf8(""))
        self.aceptar_contrasenia_enc = QtGui.QPushButton(self.centralwidget)
        self.aceptar_contrasenia_enc.setGeometry(QtCore.QRect(480, 210, 91, 27))
        self.aceptar_contrasenia_enc.setObjectName(_fromUtf8("aceptar_contrasenia_enc"))
        self.contrasenia_enc = QtGui.QLineEdit(self.centralwidget)
        self.contrasenia_enc.setGeometry(QtCore.QRect(430, 180, 181, 27))
        self.contrasenia_enc.setObjectName(_fromUtf8("contrasenia_enc"))
        self.label_contrasenia_enc = QtGui.QLabel(self.centralwidget)
        self.label_contrasenia_enc.setGeometry(QtCore.QRect(450, 160, 131, 20))
        self.label_contrasenia_enc.setObjectName(_fromUtf8("label_contrasenia_enc"))
        self.label_contrasenia_des = QtGui.QLabel(self.centralwidget)
        self.label_contrasenia_des.setGeometry(QtCore.QRect(460, 280, 131, 41))
        self.label_contrasenia_des.setObjectName(_fromUtf8("label_contrasenia_des"))
        self.contrasenia_des = QtGui.QLineEdit(self.centralwidget)
        self.contrasenia_des.setGeometry(QtCore.QRect(440, 320, 171, 27))
        self.contrasenia_des.setObjectName(_fromUtf8("contrasenia_des"))
        self.pass_true_false = QtGui.QLabel(self.centralwidget)
        self.pass_true_false.setGeometry(QtCore.QRect(470, 380, 121, 20))
        self.pass_true_false.setText(_fromUtf8(""))
        self.pass_true_false.setObjectName(_fromUtf8("pass_true_false"))
        self.aceptar_contrasenia_des = QtGui.QPushButton(self.centralwidget)
        self.aceptar_contrasenia_des.setGeometry(QtCore.QRect(480, 350, 81, 27))
        self.aceptar_contrasenia_des.setObjectName(_fromUtf8("aceptar_contrasenia_des"))
        self.label_error = QtGui.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(500, 450, 41, 20))
        self.label_error.setText(_fromUtf8(""))
        self.label_error.setObjectName(_fromUtf8("label_error"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.sel_rutaOrigen.setText(_translate("MainWindow", "Origen", None))
        self.encriptar.setText(_translate("MainWindow", "Encriptar", None))
        self.desencriptar.setText(_translate("MainWindow", "Desencriptar", None))
        self.sel_rutaDestino.setText(_translate("MainWindow", "Destino", None))
        self.sel_algoritmo.setItemText(0, _translate("MainWindow", "AES-256", None))
        self.sel_algoritmo.setItemText(1, _translate("MainWindow", "Algoritmo 2", None))
        self.aceptar_contrasenia_enc.setText(_translate("MainWindow", "Aceptar", None))
        self.label_contrasenia_enc.setText(_translate("MainWindow", "Ingrese contraseña ", None))
        self.label_contrasenia_des.setText(_translate("MainWindow", "Ingrese contraseña\n"
"  para desencriptar", None))
        self.aceptar_contrasenia_des.setText(_translate("MainWindow", "Aceptar", None))

