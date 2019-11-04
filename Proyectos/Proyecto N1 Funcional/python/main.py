from core.gui import *
from core.Tree import *
from PyQt5.QtGui import QIcon
import copy



class MainWindow(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.center() 
        self.tree1 = TSVToTree("memory/Tree-A.mem")
        self.tree2 = TSVToTree("memory/Tree-B.mem")
        self.parent1 = self.tree1.root 
        self.parent2 = self.tree2.root
        self.showInExplorer(self.tree1,self.parent1,self.explorer1)
        self.showInExplorer(self.tree2,self.parent2,self.explorer2)
        self.explorer1.itemDoubleClicked.connect(self.changeDir1)
        self.explorer2.itemDoubleClicked.connect(self.changeDir2)
        self.NDir1.clicked.connect(self.newDir1)
        self.NDir2.clicked.connect(self.newDir2)
        self.NFile1.clicked.connect(self.newFile1)
        self.NFile2.clicked.connect(self.newFile2)
        self.delete1.clicked.connect(self.del1)
        self.delete2.clicked.connect(self.del2)
        self.LeftToRight.clicked.connect(self.lTR)
        self.RightToLeft.clicked.connect(self.rTL)

    #Este metodo copia

    def lTR(self):
        aa = self.explorer1.selectedItems()
        na = []

        for i in aa:
            na.append(i.text())
        for j in na:
            if self.parent2.children.searchValue(j):
                if not self.question("File already exists","Replace %s" %j):
                    continue
            current = self.parent1.children.getNode(j)
            self.parent2.children.add(current)
            self.explorer2.clear()
            self.showInExplorer(self.tree2, self.parent2, self.explorer2)
            self.tree2.treeToFile("memory/Tree-B.mem")
    
    def rTL(self):
        aa = self.explorer2.selectedItems()
        na = []

        for i in aa:
            na.append(i.text())
        for j in na:
            if self.parent1.children.searchValue(j):
                if not self.question("File already exists","Replace %s" %j):
                    continue
            current = self.parent2.children.getNode(j)
            self.parent1.children.add(current)
            self.explorer1.clear()
            self.showInExplorer(self.tree1, self.parent1, self.explorer1)
            self.tree1.treeToFile("Archivo1.tsv")

    
        
        
    # Este método se ejecuta cuando el usuario dobleclikea un item de el explorador 1

    def changeDir1(self):
        name = self.explorer1.currentItem().text()
        if name[-1] == "/":
            self.parent1 = self.parent1.children.getNode(name)
            self.explorer1.clear()
            self.showInExplorer(self.tree1,self.parent1,self.explorer1)
        elif name == "..":
            self.parent1 = self.tree1.getParent(self.parent1)
            self.explorer1.clear()
            self.showInExplorer(self.tree1, self.parent1, self.explorer1)
        elif name == ".":
            pass
        else:
            self.showMsgBox("Files Explorer","Archivo: %s" % name)

    def changeDir2(self):
        name = self.explorer2.currentItem().text()
        if name[-1] == "/":
            self.parent2 = self.parent2.children.getNode(name)
            self.explorer2.clear()
            self.showInExplorer(self.tree2,self.parent2,self.explorer2)
        elif name == "..":
            self.parent2 = self.tree2.getParent(self.parent2)
            self.explorer2.clear()
            self.showInExplorer(self.tree2, self.parent2, self.explorer2)
        elif name == ".":
            pass
        else:
            self.showMsgBox("Files Explorer","Archivo: %s" % name)


    # Este método muestra una ventana de mensaje con titulo title y mensaje msg

    def showMsgBox(self, title, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(msg)
        msgbox.exec_()


    # Este metodo se encarga de añadir los hijos del nodo parent, del arbol tree, en el explorer

    def showInExplorer(self,tree, parent, explorer):
        if not parent == tree.root:
            explorer.addItem(".")
            explorer.addItem("..")
        array = tree.showChilds(parent)
        for i in array:
            if i[-1] == "/":
                item = QtWidgets.QListWidgetItem(QIcon("core/images/folder.ico"), i)
                explorer.addItem(item)
        for i in array:
            if not i[-1]=="/":
                item = QtWidgets.QListWidgetItem(QIcon("core/images/file.ico"), i)
                explorer.addItem(item)

    # Este metodo centra la ventana
    
    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    # Este metodo añade un directorio

    def newDir1(self):
        name,condition = QtWidgets.QInputDialog.getText(self,"New Folder","Write the name")
        if not condition:
            return False
        elif condition and name == "":
            self.showMsgBox("Message","You have to write the name")
            return False
        else:
            name += "/"
            if(self.parent1.children.searchValue(name)):
                if not self.question("Duplicated File","Do you want to replace it?"):
                    return False
                self.parent1.children.delete(name)
            self.parent1.children.add(name)
            self.explorer1.clear()
            self.showInExplorer(self.tree1,self.parent1,self.explorer1)
            self.tree1.treeToFile("memory/Tree-A.mem")
            return True

    def newDir2(self):
        name,condition = QtWidgets.QInputDialog.getText(self,"New Folder","Write the name")
        if not condition:
            return False
        elif condition and name == "":
            self.showMsgBox("Message","You have to write the name")
            return False
        else:
            name += "/"
            if(self.parent2.children.searchValue(name)):
                if not self.question("Duplicated File","Do you want to replace it?"):
                    return False
                self.parent2.children.delete(name)
            self.parent2.children.add(name)
            self.explorer2.clear()
            self.showInExplorer(self.tree2,self.parent2,self.explorer2)
            self.tree2.treeToFile("memory/Tree-B.mem")
            return True

    #Este metodo añade un archivo
    def newFile1(self):
        name,condition = QtWidgets.QInputDialog.getText(self,"New Folder","Write the name")
        if not condition:
            return False
        elif condition and name == "":
            self.showMsgBox("Message","You have to write the name")
            return False
        else:
            if(self.parent1.children.searchValue(name)):
                if not self.question("Duplicated File","Do you want to replace it?"):
                    return False
                self.parent1.children.delete(name)
            self.parent1.children.add(name)
            self.explorer1.clear()
            self.showInExplorer(self.tree1,self.parent1,self.explorer1)
            self.tree1.treeToFile("memory/Tree-A.mem")
            return True

    def newFile2(self):
        name,condition = QtWidgets.QInputDialog.getText(self,"New Folder","Write the name")
        if not condition:
            return False
        elif condition and name == "":
            self.showMsgBox("Message","You have to write the name")
            return False
        else:
            if(self.parent2.children.searchValue(name)):
                if not self.question("Duplicated File","Do you want to replace it?"):
                    return False
                self.parent2.children.delete(name)
            self.parent2.children.add(name)
            self.explorer2.clear()
            self.showInExplorer(self.tree2,self.parent2,self.explorer2)
            self.tree2.treeToFile("memory/Tree-B.mem")
            return True

    #Este metodo elimina archivos
    def del1(self):
        rr = self.explorer1.selectedItems()
        nr = []
        if not self.question("Removing","Are you sure?"):
            return False
        for i in rr:
            nr.append(i.text())
        for j in nr:
            self.parent1.children.delete(j)

        self.explorer1.clear()
        self.showInExplorer(self.tree1, self.parent1, self.explorer1)
        self.tree1.treeToFile("memory/Tree-A.mem")

    def del2(self):
        rr = self.explorer2.selectedItems()

        nr = []
        if not self.question("Removing","Are you sure?"):
            return False
        for i in rr:
            nr.append(i.text())
        for j in nr:
            self.parent2.children.delete(j)

        self.explorer2.clear()
        self.showInExplorer(self.tree2, self.parent2, self.explorer2)
        self.tree2.treeToFile("memory/Tree-B.mem")


    # otras funciones

    def question(self,title,msg):
        dialog = QtWidgets.QMessageBox.question(self,title,msg)
        return dialog==QtWidgets.QMessageBox.StandardButtons(QtWidgets.QMessageBox.Yes)




if __name__ == "__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec()