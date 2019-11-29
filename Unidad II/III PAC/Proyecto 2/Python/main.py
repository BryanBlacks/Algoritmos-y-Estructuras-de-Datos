#-*- coding: utf8 -*-
import sys
import datetime

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
    "\n\t%s\n" % ("v 0.00.04".center(100, " ")),
    "\n\tSistema que gestiona archivos almacenados en formato JSON.\n",
    "%s%s" % ("\t", "-" * 100)
) 

help = "\n%s%s%s%s\n" % (
    #"%s%s" % ("\t", "-" * 100),
    "\tComandos:\n",
    "\n\t\thelp\t---> Ayuda.",
    "\n\t\tls\t---> Muestra algo en la consola.",
    "\n\t\texit\t---> Salir del programa.\n",
    #"%s%s" % ("\t", "-" * 100),
)

commandError = "\n%s%s%s\n" % (
    "%s%s" % ("\t", "*" * 100),
    "\n\tEl comando ingresado no existe.\n",
    "%s%s" % ("\t", "*" * 100),
) 

print(header)

while(True):
    command = input("\t$ ")
    #Limpiado del comand
    
    if (command == None or command == ""):
        pass
    elif (command == "help"):
        print("%s%s" % (header, help))
    elif (command == "ls"):
        print("\n\t\tLista en forma Horizontal")
    elif (command == "ls-1"):
        print("\n\t\tLista en forma vertical\n")
    elif (command == "pwd"):
        print("\n\t\tImprime el nodo actual\n")

    elif (command == "ln"):
        #Restricciones sino se agregan plecas, sino existe el directorio y/o el archivo
        print("\n\t\tCrear Link de archivo\n")

    elif (command == "touch"):
        #captura de parametro
        print("\n\t\tCrear Nodo de tipo archivo\n")

    elif (command == "mkdir"):
        #captura de parametro
        print("\n\t\tCrear Nodo de tipo directorio\n")

    elif (command == "plot"):
        print("\n\t\tMapa de todos los nodos del grafo\n")

    elif (command == "rmdir"):
        #captura de parametro
        print("\n\t\tElimina nodo del árbol\n")

    elif (command == "trash"):
        print("\n\t\tLista de todo lo borrado en el árbol\n")

    elif (command == "cd"):
        print("\n\t\tNavegar al nodo padre\n")

    elif (command == "findfbe"):
        print("\n\t\tEncontrar archivos por extensión\n")

    elif (command == "exit"):
        break
    else:
        print("%s%s" % (commandError ,help))