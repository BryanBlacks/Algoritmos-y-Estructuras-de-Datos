# -*- coding: utf8 -*-
from PyQt5 import uic, QtWidgets
from Nucleo.Interfaz.MainWindow import *
from Nucleo.Interfaz.AddWindow import *
from Nucleo.Interfaz.EditWindow import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #Pantalla Principal
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_MainWindow()
        self.center()
        self.btnAdd.clicked.connect(self.openAdd)
        self.btnEdit.clicked.connect(self.openEdit)

    def openAdd(self):
        self.AddWindow=QtWidgets.QWidget()
        self.ui=Ui_WinAdd()      
        self.ui.setupUi(self.AddWindow)
        MainWindow.center(self.AddWindow)
        self.AddWindow.show()

    def openEdit(self):
        self.EditWin=QtWidgets.QWidget()
        self.ui=Ui_Tabla()      
        self.ui.setupUi(self.EditWin)
        MainWindow.center(self.EditWin)
        self.EditWin.show()
    
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
