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
                "\n\t%s" % ("* SGestor *".center(100, " ")),
                "\n\t%s\n" % (("*" * 11).center(100, " "))
            ),
            "\n\t%s\n" % ("Sistema gestor de archivos".center(100, " ")),
            "\n\t%s" % ("Creado por: ".center(100, " ")),
            "\n\t%s" % ("[Bryan Gonzales] [Edgar Benedetto] [Fabio Lagos]".center(100, " ")),
            "\n\t%s\n" % ("v 0.00.10".center(100, " ")),
            "\n\tSistema que gestiona archivos almacenados en formato JSON.\n",
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
            "\n\t\tls\t---> Muestra algo en la consola.",
            "\n\t\texit\t---> Salir del programa.\n",
            #"%s%s" % ("\t", "-" * 100),
        )
        print(help)

    def clean(self, command):
        return []
    
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
            a = []
            i = i.strip()

            space = i.find(" ")
            command, param = i[:space],i[space:]

            a.append(command)
            a.append(param.strip())
            array.append(a)

        return array