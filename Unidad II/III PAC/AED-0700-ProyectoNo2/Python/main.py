# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
Main
---------------------------------------------------------------------------------------------------------------------

* Se establece un ciclo infinito donde se realizará cada operación del programa.
* Se captura, en una cadena, los comandos que el usuario introduce por medio de la consola.
* La cadena se limpia y se convierte en un arreglo para después procesarla y operar cada función del programa.
* Los comandos deben estar validados para su porterior ejecución.
* El usuario solo podrá salir de la ejecuión del programa si introduce el comando "exit".

---------------------------------------------------------------------------------------------------------------------
"""

from Core.MultiFunction import Function

multiFunction = Function()
multiFunction.printHeader()
centinel = True

while(centinel):
    #Captura del comando por medio de una cadena.
    command = input("\t$ ")
    
    if (command == None or command == ""):
        pass
    else:
        #Conversión de la cadena (comando) en un arrego.
        array = multiFunction.info(command)

        for command in array:
            if (command[0] == "help"):
                #Mensaje de ayuda con la lista de comandos válidos.
                if (command[1] == "help"):
                    #Muestra la información básica del programa, como la lista de los comandos soportados por el mismo.
                    multiFunction.printHeader() 
                    multiFunction.printHelp()
                else:
                    multiFunction.printError()

            elif (command[0] == "ls"):
                if (command[1] == "-1"):
                    #Captura de parametro.
                    #Muestra una lista vertical de los directorios y archivos ordenados.
                    multiFunction.ls(command[1])
                elif (command[1] == "ls"):
                    #Muestra una lista horizontal de los directorios y archivos ordenados.                    
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
                #Crea un enlace a un archivo.
                multiFunction.ln(command[1])

            elif (command[0] == "touch"):
                #Crea un Nodo de tipo archivo.
                #Captura de parametro.
                multiFunction.touch(command[1])

            elif (command[0] == "mkdir"):
                #Crea un Nodo de tipo directorio.
                #Captura de parametro.
                multiFunction.mkdir(command[1])

            elif (command[0] == "plot"):
                #Muestra el grafo en una ventana.
                if (command[1] == "plot"):
                    multiFunction.plot()
                else:
                    multiFunction.printError()

            elif (command[0] == "trash"):
                #Muestra una lista de los directorios o archivos eliminados, con su información básica.
                if (command[1] == "trash"):
                    multiFunction.trash()
                else:
                    multiFunction.printError()

            elif (command[0] == "cd"):
                #Navegación entre nodos.
                #Captura de parametro.                
                multiFunction.cd(command[1])

            elif (command[0] == "rm"):
                #Elimina un Nodo de tipo archivo del árbol.
                #Captura de parametro.
                multiFunction.rm(command[1])

            elif (command[0] == "rmdir"):
                #Elimina un Nodo de tipo directorio del árbol.
                #Captura de parametro.
                multiFunction.rm(command[1])

            elif (command[0] == "findfbe"):
                #Encuentra archivos por extensión en el árbol.
                pass

            elif (command[0] == "exit"):
                #Sale del programa rompiendo el ciclo infinito.
                if (command[1] == "exit"):
                    centinel = False
                    break
                else:
                    multiFunction.printError()

            else:
                #Error si el usuario ha ingresado un comando inválido.
                multiFunction.printError()
