# -*- coding:utf8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.Windows.graphWindow import Graph
from Core.TDAGraph.TDAGraph import *

graph = TreeGraph()

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
    
    def ls(self):
        pass

    def plot(self):
        app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.goWindow = Graph()
        self.goWindow.setupUi(self.window)
        self.window.show()
        app.exec()
    
    def mkdir(self, command):
        #command[4:]
        #self.clean quitar espacios quitar tabulados y por ultimo separar cada cadena por un espacio
        #para progresivamente hacer el split "[[comando,parametro];[comando1,parametro1]]"
        #parametro1
        pass
    
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
            self.rootes.pop()
        else:
            nodeName = graph.search(nodeName)
            if nodeName :
                self.rootes.append(nodeName)
            else:
                pass

        return self.rootes[-1]