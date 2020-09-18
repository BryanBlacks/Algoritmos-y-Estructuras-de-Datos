#-*- coding: "utf-8" -*-
from PyQt5 import uic, QtWidgets
from Nucleo.Interface.mainwin import *
from Nucleo.Interface.mapwin import *
from Nucleo.Interface.tablewin import *
from Nucleo.Python.GraphTDA import *
from Nucleo.Python.MultiFunction import *
import copy

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #Pantalla Principal
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui=Ui_MainWindow()
        self.resize(505, 490)
        self.center()
        self.CreateMap.clicked.connect(self.openMap)
        self.CreateTable.clicked.connect(self.openTable)
        self.LoadFile.clicked.connect(self.listFiles)

        #Instancia para la carga de archivos .txt
        txt = TxtFile()
        files= txt.lines("/home/benedetto/Documentos/Proyecto #2/Python/Memory")
        #Agregar lista de archivos .txt en la ubicación anterior 
        self.comboBox.addItems(files)

    #Guardar lista de archivos .txt y lectura del actual
    def listFiles(self):
        filename = self.comboBox.currentText()
        array= open("%s%s" % ('/home/benedetto/Documentos/Proyecto #2/Python/Memory/',filename),"r")
        b = array.read()
        array.close()
        self.textEdit.setText(b)

    #Crear Mapa de Nodos creando el json de lo que se encuentra en el texto plano 
    def openMap(self):
        #Se obtiene lo que se encuentra en editText de la pantalla principal
        info = self.textEdit.toPlainText()
        
        #Se divide por saltos de línea
        info = info.split("\n")

        #Instancia de la clase arista para la conversión de lo obtenido en el edit text a un JSON
        prin = Arista()
        prin.process(info)
        

        #Momento donde el JSON hace uso de matplotlib para el guardado y embebido de la imagen en la pantalla Map
        prin.toMap()
        self.windowMap=QtWidgets.QWidget()
        self.ui=Ui_Grafo()      
        self.ui.setupUi(self.windowMap)
        MainWindow.center(self.windowMap)
        self.windowMap.show()  
        #self.hide()
        
    #Embeber un texto de multiples líneas no editable con una tabla generada por caracteres ASCII
    def openTable(self):
        #Obtener lo que hay en el texto de multiples lineas de la pantalla principal
        info1 = self.textEdit.toPlainText()

        #Dividirlo por saltos de línea
        info1 = info1.split("\n")

        #Instanciar la clase Arista en la cual se crean los grafos: Tipo Json y Tipo TDA
        principal = Arista()

        #Se manda lo obtenido del EditText de la pantalla principal para ser procesado a los grafos
        principal.process(info1)

        #Se obtiene el texto que contienen las dos casillas donde se inserta el nodo origen y destino
        origin = self.OriginNode.toPlainText()
        destiny = self.DestinyNode.toPlainText()

        #Se calculan sus rutas y pesos
        principal.findPaths(origin, destiny)
        principal.findWeight(origin, destiny)

        #Se ordenan las rutas
        principal.orderRutes()

        #Se genera la cadena con caracteres ASCII
        table = principal.toTable(origin,destiny)

        self.resize(505, 490)
        self.windowTable=QtWidgets.QMainWindow()
        self.ui=Ui_Tabla()
        self.center()
        self.ui.setupUi(self.windowTable) 

        #Se muestra la tabla de caracteres ASCII en el TableEditText que es no editable
        self.ui.TableTextEdit.setText(table)

        MainWindow.center(self.windowTable)
        self.windowTable.show()
        #self.hide()

    #Función para centrar las pantallas
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
