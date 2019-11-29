#-*- coding: utf8 -*-
from Nucleo.Comandos.Multifunction import *

multfunction = Function()
multfunction.printHeader()

while(True):
    command = input("\t$ ")
    #Limpiado del comand
    array = multfunction.clean(command)
    
    if (command == None or command == ""):
        pass
    #[["help"];[ls];[ls-1]]
    #PRUEBA 2 COÑO
    for command in array:
        elif (command[0] is "help"):
            multifunction.header() 
            multifunction.help()

        elif (command[0] is "ls"):
            multfunction.ls()

        elif (command[0] is "ls-1"):
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
            multfunction.commandError()
            multfunction.printHelp