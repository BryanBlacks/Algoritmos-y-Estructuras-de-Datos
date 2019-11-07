# -*- coding: utf8 -*-
from PyQt5 import uic, QtWidgets
from Nucleo.Interfaz.MainWindow import *
from Nucleo.Interfaz.AddWindow import *
from Nucleo.Interfaz.EditWindow import *
from Nucleo.Interfaz.AboutWindow import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #Pantalla Principal
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_MainWindow()
        self.center()
        self.btnAdd.clicked.connect(self.openAdd)
        self.btnEdit.clicked.connect(self.openEdit)
        self.btnAbout.clicked.connect(self.openAbout)

    def openAdd(self):
        self.AddWindow=QtWidgets.QWidget()
        self.ui=Ui_WinAdd()      
        self.ui.setupUi(self.AddWindow)
        MainWindow.center(self.AddWindow)
        self.AddWindow.show()

    def openEdit(self):
        self.EditWindow=QtWidgets.QWidget()
        self.ui=Ui_Tabla()      
        self.ui.setupUi(self.EditWindow)
        MainWindow.center(self.EditWindow)
        self.EditWindow.show()

    def openAbout(self):
        self.AboutWindow=QtWidgets.QWidget()
        self.ui=Ui_WinAbout()      
        self.ui.setupUi(self.AboutWindow)
        MainWindow.center(self.AboutWindow)
        self.AboutWindow.show()
    
    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

if __name__ == "__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec()
