# -*- coding:utf8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.Windows.graphWindow import Graph

class Function: 
    def __init__(self):
        pass

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
            "%s%s" % ("\t", "*" * 100),
        )
        print(commandError)

    #Comandos de la consola
    def printHelp(self):
        help = "\n%s%s%s%s\n" % (
            #"%s%s" % ("\t", "-" * 100),
            "\tComandos:\n",
            "\n\t\thelp\t---> Ayuda.",
            "\n\t\tls\t---> Imprime una lista de forma horizontal, con lo existente en la ruta actual.",
            "\n\t\tls-1\t---> Imprime una lista de forma vertical, con lo existente en la ruta actual.\n",
            "\n\t\tls-1\t---> Imprime una lista de forma vertical, con lo existente en la ruta actual.\n",
            "\n\t\tpwd\t---> Impresión de la ruta actual en la que se encuentra.\n",
            "\n\t\ttouch\t---> Crea un Archivo.\n",
            "\n\t\tmkdir\t---> Crea un Directorio.\n",
            "\n\t\tplot\t---> Crea un Directorio.\n",
            "\n\t\trm\t---> Elimina un archivo.\n",
            "\n\t\trmdir\t---> Elimina un carpeta.\n",
            "\n\t\ttrash\t---> Lista de archivos y directorios borrados con su nombre y fecha.\n",
            "\n\t\tcd\t---> Para navergar en rutas.\n",
            "\n\t\tfindfbe\t---> Encontrar archivos por extención.\n",
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
        command = self.clean(command)
        #self.clean quitar espacios quitar tabulados y por ultimo separar cada cadena por un espacio
        #para progresivamente hacer el split "[[comando,parametro];[comando1,parametro1]]"
        #parametro1
    
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