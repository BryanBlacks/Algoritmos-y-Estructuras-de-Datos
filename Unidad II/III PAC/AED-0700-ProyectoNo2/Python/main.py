#-*- coding:utf8 -*-

from Core.Formats.MultiFunction import Function

multiFunction = Function()
multiFunction.printHeader()

while(True):
    command = input("\t$ ")
    #Limpiado del comand
    array = multiFunction.clean(command)
    
    if (command == None or command == ""):
        pass
    #[["help"];[ls];[ls-1]]
    #PRUEBA 2 COÑO
    #for command in array:
    if (command[0] == "help"):
        multiFunction.printHeader() 
        multiFunction.printHelp()

    elif (command[0] == "ls"):
        multiFunction.ls()

    elif (command[0] == "ls-1"):
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
        multiFunction.plot()

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
        multiFunction.printCommandError()
        multiFunction.printHelp()