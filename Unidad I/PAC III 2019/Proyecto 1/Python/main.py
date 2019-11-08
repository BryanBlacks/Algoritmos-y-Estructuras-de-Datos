# -*- coding: utf8 -*-
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Nucleo.Interfaz.MainWindow import *
from Nucleo.Interfaz.AddWindow import *
from Nucleo.Interfaz.EditWindow import *
from Nucleo.Interfaz.AboutWindow import *
from Nucleo.Lista.LinkedList import *
from Nucleo.Lista.Product import *

Queue = LinkedList()

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #Pantalla Principal
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_MainWindow()
        self.center()
        self.show()
        self.btnAddProduct.clicked.connect(self.openAddWindow)
        self.btnEdit.clicked.connect(self.openEdit)
        self.btnAbout.clicked.connect(self.openAbout)

    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    def openAddWindow(self):
        self.addwindow = AddWindow()
        self.addwindow.show()

    def openEdit(self):
        self.editwindow = EditWindow()
        self.editwindow.show()
    
    def openAbout(self):
        self.aboutwindow = AboutWindow()
        self.aboutwindow.show()

class AddWindow(QtWidgets.QMainWindow,Ui_WinAdd):
    #Pantalla para agregar
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_WinAdd()
        self.center()
        self.btnAdd.clicked.connect(self.addToList)
        self.btnCanel.clicked.connect(self.cancelCreation)

    def addToList(self):
        nameProduct = self.txtName.toPlainText()
        priceProduct = self.txtPrice.toPlainText()
        currencyProduct = self.comboBox.currentText()
        descriptProduct = self.plntxtDesc.toPlainText()
        Queue.push(Product(nameProduct, priceProduct, currencyProduct, descriptProduct))
        self.clearText()
        #print(nameProduct, priceProduct, currencyProduct, descriptProduct)
        
    def clearText(self):
        self.txtName.clear()
        self.txtPrice.clear()
        self.plntxtDesc.clear()
        #print(Queue.printQueue())
    
    def cancelCreation(self):
        cancelButton = QMessageBox.question(self,"PyQt5 message","¿Está seguro que desea cancelar la creación del producto?", QMessageBox.Yes | QMessageBox.No)
        if cancelButton == QMessageBox.Yes:
            self.clearText()
        else:
            pass

    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())
    
class EditWindow(QtWidgets.QMainWindow,Ui_Tabla):
    #Pantalla para editar
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_Tabla()
        self.center()
        self.btnEdit.clicked.connect(self.openAddFromEdit)
    
        text = Queue.generateTable() 
        self.txtTable.setText(text)
        
    def openAddFromEdit(self):
        self.addfromedit = AddWindow()


        numPos = self.txtNumber.toPlainText()
        if(int(numPos)):
            editProduct = Queue.search(int(numPos))
        else:
            QMessageBox.warning(self,"PyQt5 Message","Introduzca un número de producto válido")
        self.addfromedit.show()
 
    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

class AboutWindow(QtWidgets.QMainWindow,Ui_WinAbout):
    #Pantalla para editar
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_WinAbout()
        self.center()
    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

if __name__ == "__main__":
    apt = QtWidgets.QApplication([])
    mainwindow = MainWindow()
    mainwindow.show()
    apt.exec()
