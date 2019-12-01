# -*- coding:utf8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.Windows.graphWindow import Graph
from Core.TreeGraph.TDAGraph import *

graph = TreeGraph()
list1 = LinkedList()

class Function: 
    def __init__(self):
        #Arreglo de rutas en las que se navega
        self.rootes = [graph.root]

    def printHeader(self):
        header = "\n%s%s%s%s%s%s%s%s\n" % (
            "%s%s" % ("\t", "-" * 100),
            "\n%s%s%s" % (
                "\t%s" % (("*" * 11).center(100, " ")),
                "\n\t%s" % ("* Simulador de Gestor de Archivos  *".center(100, " ")),
                "\n\t%s\n" % (("*" * 11).center(100, " "))
            ),
            "\n\t%s\n" % ("Sistema gestor de archivos".center(100, " ")),
            "\n\t%s" % ("Creado por: ".center(100, " ")),
            "\n\t%s" % ("[Bryan Gonzales] [Edgar Benedetto] [Fabio Lagos]".center(100, " ")),
            "\n\t%s\n" % ("v 0.00.10".center(100, " ")),
            "\n\tSistema que gestiona archivos y carpetas en consola exclusivamente, almacenados en formato JSON.\n",
            "%s%s" % ("\t", "-" * 100)
        )
        print(header)
    
    def printCommandError(self):
        commandError = "\n%s%s%s\n" % (
            "%s%s" % ("\t", "*" * 100),
            "\n\tEl comando ingresado no existe.\n",
            "%s%s" % ("\t", "*" * 100)
        )
        print(commandError)

    #Comandos de la consola
    def printHelp(self):
        help = "\n%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n" % (
            #"%s%s" % ("\t", "-" * 100),
            "\tComandos:\n",
            "\n\t\thelp\n\n\t\t\t---> Ayuda.\n",
            "\n\t\tls\n\n\t\t\t---> Imprime una lista de forma horizontal, con lo existente en la ruta actual.\n",
            "\n\t\tls -1\n\n\t\t\t---> Imprime una lista de forma vertical, con lo existente en la ruta actual.\n",
            "\n\t\tpwd\n\n\t\t\t---> Impresión de la ruta actual en la que se encuentra.\n",
            "\n\t\ttouch [NOMBRE DEL ARCHIVO]\n\n\t\t\t---> Crea un Archivo.\n",
            "\n\t\tmkdir [NOMBRE DEL DIRECTORIO]\n\n\t\t\t---> Crea un Directorio.\n",
            "\n\t\tplot\n\n\t\t\t---> Crea un Directorio.\n",
            "\n\t\trm [NOMBRE DEL ARCHIVO]\n\n\t\t\t---> Elimina un archivo.\n",
            "\n\t\trmdir [NOMBRE DEL DIRECTORIO]\n\n\t\t\t---> Elimina un carpeta.\n",
            "\n\t\ttrash\n\n\t\t\t---> Lista de archivos y directorios borrados con su nombre y fecha.\n",
            "\n\t\tcd [RUTA]\n\n\t\t\t---> Para navergar en rutas.\n",
            "\n\t\tcd ..\n\n\t\t\t---> Para regresar a una ruta anterior a la actual.\n",
            "\n\t\tfindfbe [EXTENSIÓN]\n\n\t\t\t---> Encontrar archivos por extensión.\n\n",
            #"%s%s" % ("\t", "-" * 100),
        )
        print(help)
    

    def plot(self):
        app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.goWindow = Graph()
        self.goWindow.setupUi(self.window)
        self.window.show()
        app.exec()
    
    def mkdir(self, name):
        refer  = self.rootes[-1]
        graph.add(name,"D",refer.value.name)
        
    def touch(self,name):
        refer = self.rootes[-1]
        graph.add(name, "F",refer.value.name)
    
    def info(self, text):

        text = text.split(";")
        array = []

        for i in text:
            newArray = []
            i = i.strip()

            space = i.find(" ")
            if space == -1:
                command, param = i[:],i[:]
            else: 
                command, param = i[:space],i[space:]

            newArray.append(command)
            newArray.append(param.strip())
            array.append(newArray)

        return array

    def cd(self, nodeName):
        if nodeName is "..":
            #condicional si esta en el root
            if len(self.rootes) == 1:
                pass
            else:
                self.rootes.pop()
        else:
            nodeName = graph.navegation(nodeName)
            if nodeName :
                self.rootes.append(nodeName)
            else:
                print("Ruta no encontrada")

        return True
    
    def ls_1(self):
        pass

    def ls(self):
        pass

    def pwd(self):
        
        array = self.rootes
        rute = ""
        for node in array:

            nameRute = node.value.name
            rute = "%s/%s" % (rute,nameRute)
        rute = "%s/" % rute

        return rutes

    def ln(self, text):
        pos = text.find("/")
        text = [(pos+1):]
        text = text.split("/")

        copyfile = text[-1]
        direc = text[-2]

        file1 = self.rootes[-1].value.edge.search(copyfile)
        pos = (file1.value.name).find(".")
        name = "%s.lnk" % file1.value.name[:pos]

        dir1 = graph.search(direc)
        
        if file1 and dir1:
            graph.add(name,"F",dir1.value.name)
        else:
            print("La dirección o el archivo no existe en el árbol")
        

    def rm(self,name):
        refer = self.rootes[-1]
        graph.remove(name,refer.value.name)

    def rmdir(self,name):
        refer = self.rootes[-1]
        graph.remove(name,refer.value.name)
    
    def trash(self):
        
        list1 = graph.trash
        current = list1.first
        trail = ""
        while (current):
            trail = "%s%s, fecha de eliminación: %s\n" % (trail,current.value.name,current.date) 
            current = current.next
        
        print(trail)


    def findfbe(self, extension):
        pass
        #listOfNodes = 