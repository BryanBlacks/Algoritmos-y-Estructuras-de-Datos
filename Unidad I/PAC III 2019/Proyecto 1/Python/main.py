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
        #self.lblCount.setText(str(Queue.length()))

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
        #self.addInPosition = EditWindow()
        nameProduct = self.txtName.toPlainText()
        priceProduct = self.txtPrice.toPlainText()
        currencyProduct = self.comboBox.currentText()
        descriptProduct = self.plntxtDesc.toPlainText()
        #if (isinstance (self.addInPosition.numPos , int)):
            #Queue.pushInPosition(Product(nameProduct, priceProduct, currencyProduct, descriptProduct) , pos)
        #else:
        Queue.push(Product(nameProduct, priceProduct, currencyProduct, descriptProduct))

        #self.con.lblCount.setText(str(Queue.length()))
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
        self.txtTable.setPlainText(text)
        
    def openAddFromEdit(self):
        self.addfromedit = AddWindow()
        self.numPos = self.txtNumber.toPlainText()
        pos = int(self.numPos)
        if(pos == 0 or pos):
            self.toEdit = Queue.search(pos)
            if self.toEdit is False:
                QMessageBox.warning(self,"PyQt5 Message","Introduzca un número de producto válido")
            else:
                self.addfromedit.show()
                
                nameEdit = Queue.getName(pos)
                priceEdit = Queue.getPrice(pos)
                descEdit = Queue.getDesc(pos)
                self.addfromedit.txtName.setText(nameEdit)
                self.addfromedit.txtPrice.setText(priceEdit)
                self.addfromedit.plntxtDesc.setPlainText(descEdit)
                self.addfromedit.btnAdd.clicked.connect(self.addInPosition)
                
        else:
            QMessageBox.warning(self,"PyQt5 Message","Introduzca un número válido")

    def addInPosition(self):
        nameProduct = self.addfromedit.txtName.toPlainText()
        priceProduct = self.addfromedit.txtPrice.toPlainText()
        currencyProduct = self.addfromedit.comboBox.currentText()
        descriptProduct = self.addfromedit.plntxtDesc.toPlainText()
        #if (isinstance (self.addInPosition.numPos , int)):
            #Queue.pushInPosition(Product(nameProduct, priceProduct, currencyProduct, descriptProduct) , pos)
        #else:
        Queue.pushInPosition(Product(nameProduct, priceProduct, currencyProduct, descriptProduct),int(self.numPos))

    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

class AboutWindow(QtWidgets.QMainWindow,Ui_WinAbout):
    #Pantalla de Información del grupo
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
