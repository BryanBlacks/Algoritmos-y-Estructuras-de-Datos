# -*- coding: utf8 -*-
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Nucleo.Interfaz.MainWindow import *
from Nucleo.Interfaz.AddWindow import *
from Nucleo.Interfaz.EditWindow import *
from Nucleo.Interfaz.AboutWindow import *
from Nucleo.Interfaz.BST_HNL import *
from Nucleo.Interfaz.BST_USD import *
from Nucleo.Lista.LinkedList import *
from Nucleo.Lista.Product import *
from Nucleo.Arbol.ABB1 import *
from Nucleo.Arbol.ABB2 import *

Queue = LinkedList()
Queue.csvToLinked("Memoria/CSV.csv")

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
        self.btnTree.clicked.connect(self.openTree)
        self.lblCount.setText(str(Queue.length()))

    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    def openAddWindow(self):
        self.addwindow = AddWindow(pos = None)
        self.addwindow.btnAdd.clicked.connect(self.numProducts)
        self.addwindow.show()

    def openEdit(self):
        self.editwindow = EditWindow()
        self.editwindow.btnDelete.clicked.connect(self.numProducts)
        self.editwindow.show()
    
    def openAbout(self):
        self.aboutwindow = AboutWindow()
        self.aboutwindow.show()

    def openTree(self):
        self.bstHNLWin = BST_HNL()
        self.bstUSDWin = BST_USD()
        
        
        #self.bstHNLWin.show()
        #self.bstUSDWin.show()

    

    def numProducts(self):
        self.lblCount.setText(str(Queue.length()))

class AddWindow(QtWidgets.QMainWindow,Ui_WinAdd):
    #Pantalla para agregar
    def __init__(self, pos):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_WinAdd()
        self.center()
        self.posToAdd = pos    
        self.btnAdd.clicked.connect(self.addToList)
        self.btnCanel.clicked.connect(self.cancelCreation)

    def addToList(self):
        nameProduct = self.txtName.toPlainText()
        priceProduct = self.txtPrice.toPlainText()
        currencyProduct = self.comboBox.currentText()
        descriptProduct = self.plntxtDesc.toPlainText()
        Queue.pushInPosition(Product(nameProduct, priceProduct, currencyProduct, descriptProduct) , self.posToAdd)
        
        #if currencyProduct == 'HNL':
            #return bstHNL.add(float(priceProduct),nameProduct)
        #else: 
            #return bstUSD.add(float(priceProduct),nameProduct)

        self.clearText()
        Queue.toCsv("Memoria/CSV.csv")

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
        self.numPos = None
        self.btnEdit.clicked.connect(self.openAddFromEdit)
        self.btnDelete.clicked.connect(self.deleteProduct)
        self.drawTable()

        
    def openAddFromEdit(self):
        position = self.txtNumber.toPlainText()
        if position == '':
            QMessageBox.warning(self,"PyQt5 Message","Introduzca un número de producto a editar")
        else:
            pos = int(position)
            self.numPos = pos
            self.addfromedit = AddWindow(self.numPos)
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
                    self.addfromedit.btnAdd.clicked.connect(self.drawTable)
                    self.addfromedit.btnAdd.clicked.connect(self.closeWin)
                    
            else:
                QMessageBox.warning(self,"PyQt5 Message","Introduzca un número válido")

        self.txtNumber.clear()
    
    def closeWin(self):
        self.addfromedit.hide()

    def deleteProduct(self):
        position = self.txtNumber.toPlainText()
        position = self.txtNumber.toPlainText()
        if position == '':
            QMessageBox.warning(self,"PyQt5 Message","Introduzca un número de producto a eliminar")
        else:
            pos = int(position)
            self.numPos = pos
            if(pos == 0 or pos):
                self.toEdit = Queue.search(pos)
                if self.toEdit is False:
                    QMessageBox.warning(self,"PyQt5 Message","Introduzca un número de producto válido")
                else:
                    deleteButton = QMessageBox.question(self,"PyQt5 message","¿Está seguro que desea eliminar el producto?",QMessageBox.Yes | QMessageBox.No)
                    if deleteButton == QMessageBox.Yes:
                        Queue.pop(pos)
                        self.drawTable()
                    else:
                        pass
        self.txtNumber.clear()
        Queue.toCsv("Memoria/CSV.csv")

    def drawTable(self):
        text = Queue.generateTable() 
        self.txtTable.setPlainText(text)

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

class BST_HNL(QtWidgets.QMainWindow,Ui_BST_1):
    #Pantalla Principal
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_BST_1()
        self.center()

        self.bstHNL = BST()
        self.arrayPrices()
        self.bstHNL.showMapHNL()
    
    def arrayPrices(self):
        price= ""
        name= ""
        for i in range(Queue.length()):
            currency = Queue.getCoin(i)
            price = float(Queue.getPrice(i))
            name = str(Queue.getName(i))
            if currency == 'HNL':
                self.bstHNL.add(price,name)
            else:
                pass
        
        return True
    
    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

class BST_USD(QtWidgets.QMainWindow,Ui_BST_2):
    #Pantalla Principal
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_BST_2()
        self.center()

        self.bstUSD = BST1()
        self.arrayPrices1()
        self.bstUSD.showMapUSD()

    def arrayPrices1(self):
        price= ""
        name= ""
        for i in range(Queue.length()):
            currency = Queue.getCoin(i)
            price = float(Queue.getPrice(i))
            name = str(Queue.getName(i))
            if currency == 'USD':
                self.bstUSD.add(price,name)
            else:
                pass
        
        return True

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
