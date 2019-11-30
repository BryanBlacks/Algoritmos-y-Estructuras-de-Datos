#-*- coding:utf8 -*-

from Core.MultiFunction import *

multiFunction = Function()
multiFunction.printHeader()
a = True
while(a):
    command = input("\t$ ")
    
    if (command == None or command == ""):
        pass
    else:
        array = multiFunction.info(command)

        for command in array:
            if (command[0] == "help"):
                multiFunction.printHeader() 
                multiFunction.printHelp()

            elif (command[0] == "ls"):
                multiFunction.ls()

            elif (command[0] == "ls-1"):
                print("\n\t\tLista en forma vertical\n")

            elif (command[0] == "pwd"):
                print("\n\t\tImprime el nodo actual\n")

            elif (command[0] == "ln"):
                #Restricciones sino se agregan plecas, sino existe el directorio y/o el archivo
                print("\n\t\tCrear Link de archivo\n")

            elif (command[0] == "touch"):
                #captura de parametro
                print("\n\t\tCrear Nodo de tipo archivo\n")

            elif (command[0] == "mkdir"):
                #captura de parametro
                print("\n\t\tCrear Nodo de tipo directorio\n")

            elif (command[0] == "plot"):
                multiFunction.plot()

            elif (command[0] == "rmdir"):
                #captura de parametro
                print("\n\t\tElimina nodo del árbol\n")

            elif (command[0] == "trash"):
                print("\n\t\tLista de todo lo borrado en el árbol\n")

            elif (command[0] == "cd"):
                print("\n\t\tNavegar al nodo padre\n")

            elif (command[0] == "findfbe"):
                print("\n\t\tEncontrar archivos por extensión\n")

            elif (command[0] == "exit"):
                a = False
                break
            else:
                multiFunction.printCommandError()
                multiFunction.printHelp()
    
    
