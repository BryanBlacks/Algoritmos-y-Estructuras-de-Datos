#-*- coding:utf8 -*-

from Core.MultiFunction import *

multiFunction = Function()
multiFunction.printHeader()
centinel = True

while(centinel):
    command = input("\t$ ")
    
    if (command == None or command == ""):
        pass
    else:
        array = multiFunction.info(command)

        for command in array:
            if (command[0] == "help"):
                #Mensaje de ayuda con la lista de comandos válidos.
                if (command[1] == "help"):
                    multiFunction.printHeader() 
                    multiFunction.printHelp()
                else:
                    multiFunction.printError()

            elif (command[0] == "ls"):
                #Lista en forma horizontal y vertical.
                #Captura de parametro.
                if (command[1] == "-1"):
                    multiFunction.ls(command[1])
                elif (command[1] == "ls"):
                    multiFunction.ls()
                else:
                    multiFunction.printError()

            elif (command[0] == "pwd"):
                #Imprime la ruta del nodo actual del árbol.
                if (command[1] == "pwd"):
                    multiFunction.pwd()
                else:
                    multiFunction.printError()

            elif (command[0] == "ln"):
                #Restricciones sino se agregan plecas, sino existe el directorio y/o el archivo.
                #Crear Link de archivo.
                multiFunction.ln(command[1])

            elif (command[0] == "touch"):
                #Crear Nodo de tipo archivo.
                #Captura de parametro.
                multiFunction.touch(command[1])

            elif (command[0] == "mkdir"):
                #Crear Nodo de tipo directorio.
                #Captura de parametro.
                multiFunction.mkdir(command[1])

            elif (command[0] == "plot"):
                #Muestra el grafo en una ventana.
                if (command[1] == "plot"):
                    multiFunction.plot()
                else:
                    multiFunction.printError()

            elif (command[0] == "trash"):
                #Muestra una lista de los directorios o archivos eliminados.
                if (command[1] == "trash"):
                    multiFunction.trash()
                else:
                    multiFunction.printError()

            elif (command[0] == "cd"):
                #Navegación entre nodos.
                #Captura de parametro.                
                multiFunction.cd(command[1])

            elif (command[0] == "rm"):
                #Elimina un archivo en el nodo actual del árbol.
                #Captura de parametro.
                multiFunction.rm(command[1])

            elif (command[0] == "rmdir"):
                #Elimina un directorio en el nodo actual del árbol.
                #Captura de parametro.
                multiFunction.rm(command[1])

            elif (command[0] == "findfbe"):
                #Encuentra archivos por extensión en el árbol.
                pass

            elif (command[0] == "exit"):
                #Sale del programa
                if (command[1] == "exit"):
                    centinel = False
                    break
                else:
                    multiFunction.printError()

            else:
                #Error si el usuario ha ingresado un comando inválido.
                multiFunction.printError()
