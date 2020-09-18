#-*- coding: "utf-8" -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi

from mainwin import Ui_MainWindow
from secondsrc import Ui_secondwindow
from tree import *
treeOne = Tree()
treeTwo = Tree()
tree1 = DoubleLinked(k = treeOne.thisRoot())
tree2 = DoubleLinked(treeTwo.thisRoot())

 


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        loadUi('MainWin.ui', self)
        
        self.resize(640, 493)
        self.centerWindow()
        self.refer = None
        self.refer1 = None
        

        self.cd_tree1.clicked.connect(self.OpenSecondWindowCDTree1)
        self.cf_tree1.clicked.connect(self.OpenSecondWindowCFTree1)
        self.cd_tree2.clicked.connect(self.OpenSecondWindowCDTree2)
        self.cf_tree2.clicked.connect(self.OpenSecondWindowCFTree2)

        
        self.lwTree1.itemDoubleClicked.connect(self.innerItem1)
        self.lwTree2.itemDoubleClicked.connect(self.showItem2)

        self.lwTree1.itemSelectionChanged.connect(self.selectedOption)
        self.lwTree2.itemSelectionChanged.connect(self.selectedOption1)

    def centerWindow(self):

        # Geometría de la pantalla principal
        qr = self.frameGeometry()

        # Punto central de la pantalla
        cp = QDesktopWidget().availableGeometry().center()

        # Mover la pantalla al centro
        qr.moveCenter(cp)

        # Esquina Izquierda maxima se establece como la esquina izquierda maxima de la pantalla 
        self.move(qr.topLeft())

        #Eventos de los botones crear, un solo clic

    
    def selectedOption(self,parent= None):

        if(not parent):
            parent = self.thisReference()

        current = self.lwTree1.selectedItems()

        list1 = []
        for item in current:
            list1.append(item.text())
        
        #eliminar
        if(self.delete_tree1.clicked):
            if(not parent):
                for i in list1:
                    treeOne.delete(i)
            else:
                for i in list1:
                    treeOne.delete(i,parent)
            
        #copiar
        if(self.copy_t1tot2.clicked):
            listcopy=[]

            for node in current:
                listcopy.append(treeOne.search(node.text()))
            
            

    
    def selectedOption1(self):
        current = self.lwTree2.currentItem()
        finded = treeOne.search(current.text())

        if(self.delete_tree1.clicked):
            treeOne.delete(finded)
            
        #if(self.copiar):


    def innerItem1(self):
        current = self.lwTree1.currentItem()
        finded = treeOne.search(current.text())
        self.refer = finded
        

        if(current.text() == '..'):
            temp = tree1.search1(self.father.value.name)
            nodePrevious = tree1.nodePrev(temp)
            self.father = nodePrevious

            self.lwTree1.clear()
            a = treeOne.array(nodePrevious)
            main.lwTree1.addItems(a)
            tree1.dele()

        if(finded.value.type == 'D'):
            tree1.linked(finded)
            self.father= finded

            self.lwTree1.clear()
            z = treeOne.array(finded)
            self.lwTree1.addItems(z)

            if(self.cd_tree1.clicked):
                    
                self.OpenSecondWindowCDTree1()
                
            if(self.cf_tree1.clicked):
                self.OPenSecondWindowCFTree1()
                
            if(self.lwTree1.itemClicked):
                self.selectedOption()

                
    def showItem2(self):
        
        current = self.lwTree2.currentItem()
        finded = treeTwo.search(current.text())
        self.refer = finded
        

        if(current.text() == '..'):
            temp = tree2.search1(self.father.value.name)
            nodePrevious = tree2.nodePrev(temp)
            self.father = nodePrevious

            self.lwTree2.clear()
            a = treeTwo.array(nodePrevious)
            main.lwTree2.addItems(a)
            tree2.dele()

        if(finded.value.type == 'D'):
            tree2.linked(finded)
            self.father= finded

            self.lwTree2.clear()
            z = treeTwo.array(finded)
            self.lwTree2.addItems(z)

            if(self.cd_tree2.clicked):
                    
                self.OpenSecondWindowCDTree2()
                
            if(self.cf_tree2.clicked):
                self.OpenSecondWindowCFTree2()
                
            if(self.lwTree2.itemClicked):
                self.selectedOption()
            
    
    def thisReference(self):
        return self.refer
    
    #def thisReference1(self):
        #return self.refer

    def OpenSecondWindowCDTree1(self):
        anotherWin = SecondWindowCDTree1(self)
        anotherWin.show()

    def OpenSecondWindowCFTree1(self):
        anotherWin = SecondWindowCFTree1(self)
        anotherWin.show()

    def OpenSecondWindowCDTree2(self):
        anotherWin = SecondWindowCDTree2(self)
        anotherWin.show()
    
    def OpenSecondWindowCFTree2(self):
        anotherWin = SecondWindowCFTree2(self)
        anotherWin.show()

class SecondWindowCDTree1(QMainWindow):

    def __init__(self, parent = None):
        super(SecondWindowCDTree1, self).__init__(parent)
        loadUi('SecWin.ui', self)
        self.resize(400, 198)
        self.center()
        self.reference = None

        self.reference = main.thisReference()
        #Regresa a la pantalla principal
        self.createButton.clicked.connect(self.addToTree)
        self.createButton.clicked.connect(self.openMainWindow)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

    def addToTree(self, referen = None):
        if(not referen):
            referen = self.reference

        n = (self.textInsert.toPlainText())
        
        if(not referen):
            treeOne.add(n,"D")

        else:
            treeOne.add(n,"D",referen.value.name)
        
        #item = QListWidgetItem(n)
        #item.setIcon(QIcon("/home/benedetto/Documentos/ProyectoN1/Core/Imagenes/Directory.jpg"))
        main.lwTree1.clear()
        p = treeOne.array(referen)
        main.lwTree1.addItems(p)
        
        
    def openMainWindow(self):
        self.parent().show()
        self.close()

class SecondWindowCFTree1(QMainWindow):

    def __init__(self, parent = None):
        super(SecondWindowCFTree1, self).__init__(parent)
        loadUi('SecWin.ui', self)
        self.resize(400, 198)
        self.center()

        self.reference = None
        self.reference = main.thisReference()

        #Regresa a la pantalla principal
        self.createButton.clicked.connect(self.addToTree)
        self.createButton.clicked.connect(self.openMainWindow)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def addToTree(self, referen = None):

        if(not referen):
            referen = self.reference

        n = (self.textInsert.toPlainText())
        if(not referen):
            
            treeOne.add(n,"F")

        else:
            treeOne.add(n,"F",referen.value.name)

        main.lwTree1.clear()
        p = treeOne.array(referen)
        main.lwTree1.addItems(p)
        

    def openMainWindow(self):
        self.parent().show()
        self.close()

class SecondWindowCDTree2(QMainWindow):

    def __init__(self, parent = None):
        super(SecondWindowCDTree2, self).__init__(parent)
        loadUi('SecWin.ui', self)
        self.resize(400, 198)
        self.center()

        self.reference = None

        self.reference = main.thisReference1()
        #Regresa a la pantalla principal
        self.createButton.clicked.connect(self.addToTree)
        self.createButton.clicked.connect(self.openMainWindow)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

    def addToTree(self, referen = None):
        if(not referen):
            referen = self.reference

        n = (self.textInsert.toPlainText())
        #item = QListWidgetItem(QIcon("/home/benedetto/Documentos/Proyecto N1/Interfaz/Directory.jpg"), value)
        if(not referen):
            treeTwo.add(n,"D")

        else:
            treeTwo.add(n,"D",referen.value.name)
        
        main.lwTree2.clear()
        p = treeTwo.array(referen)
        main.lwTree2.addItems(p)
        
    def openMainWindow(self):
        self.parent().show()
        self.close()

class SecondWindowCFTree2(QMainWindow):

    def __init__(self, parent = None):
        super(SecondWindowCFTree2, self).__init__(parent)
        loadUi('SecWin.ui', self)
        self.resize(400, 198)
        self.center()

        self.reference = None
        self.reference = main.thisReference1()

        #Regresa a la pantalla principal
        self.createButton.clicked.connect(self.addToTree)
        self.createButton.clicked.connect(self.openMainWindow)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def addToTree(self, referen = None):

        if(not referen):
            referen = self.reference

        n = (self.textInsert.toPlainText())
        if(not referen):
            
            treeTwo.add(n,"F")

        else:
            treeTwo.add(n,"F",referen.value.name)

        main.lwTree2.clear()
        p = treeTwo.array(referen)
        main.lwTree2.addItems(p)
        

    def openMainWindow(self):
        self.parent().show()
        self.close()



app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())