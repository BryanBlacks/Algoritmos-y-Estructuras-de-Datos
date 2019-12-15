# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
MultiFunction (Almacen de comandos)
---------------------------------------------------------------------------------------------------------------------

* Método printHeader
    Este método imprime en consola una cadena con la información básica del programa, como ser el nombre del mismo,
    los creadores, la versión, una descripción breve del funcionamiento del mismo.

* Método "printHelp"
    Este método retorna una cadena con formato de la lista de cada uo de los comandos que el programa utiliza.

* Comando "help"
    Este comando imprime la información básica del programa anexada con la lista de comandos soportados por el
    programa, esta última cadena se obtiene al llamar a la función printHelp.

* Comando "ls o ls -1"
    Este comando llama a la funcion "print" de la lista enlazada para obtener una cadena con formato con los nombres
    de cada archivo y carpetas. Si existe un parametro, la cadena sera retornada en forma de lista vertical, 
    de lo contrario, retornará una lista horizontal.

* Comando "pwd"
    Este comando retorna en una cadena la ruta donde el usario está actualmente.

* Comando "ln"
    Este comando crea un enlace a un archivo, con formato ".lnk" dentro de la ruta actual donde se quiere crear
    dicho enlace.

* Comando "touch"
    Este comando crea un archivo con extensión en la ruta donde está el usuario está actualmente.

* Comando "mkdir"
    Este comando crea un directorio en la ruta donde está el usuario está actualmente.

* Comando "plot"
    Este comando abre una ventana donde se mostrará, de forma gráfica, el grafo previamente creado.

* Comando "rm"
    Este comando elimina un archivo en la ruta actual donde se encuentra el usuario.

* Comando "rmdir"
    Este comando elimina una carpeta en la ruta actual donde se encuentra el usuario.

* Comando "trash"
    Este comando imprime una cadena con formato, la cual contiene una lista de forma vertical de todos los 
    directorios y archivos eliminados del árbol (grafo) con su respectiva información, como ser: el nombre
    la fecha de eliminacióny la ruta a la cual pertenecía.

* Comando "cd"
    Este comando funcionará para navegar entre cada uno de los directoros, si existe el parámetro "..", se
    regresará al directorio anterior.

* Comando "findbe"
    Este comando .

* Método "save"
    Este método guarda la ruta en el archivo JSON, previamente creado e instanciado.

* Métod "read"
    Este método lee la ruta en el archivo JSON, previamente creado e instanciado.

---------------------------------------------------------------------------------------------------------------------
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.TreeGraph.TDAGraph import TreeGraph
from Core.TreeGraph.LinkedList import LinkedList

graph = TreeGraph()
list1 = LinkedList()
trashlist = graph.csvToLinked("Memory/Trash.csv")

class Function: 
    def __init__(self):
        #Arreglo de rutas en las que se navega.
        self.rootes = [graph.root]
        self.lk=[]
        

    def printHeader(self):
        logo = "%s%s%s%s%s%s%s%s%s%s%s%s%s" % (
            "\n\t%s" % ("%s            *" % (" " * (59 - 19))),
            "\n\t%s" % ("%s            ***" % (" " * (59 - 19))),
            "\n\t%s" % ("%s           *****" % (" " * (59 - 19))),
            "\n\t%s" % ("%s         **** ***" % (" " * (59 - 19))),
            "\n\t%s" % ("%s       ***** *****" % (" " * (59 - 19))),
            "\n\t%s" % ("%s    **** ** ******" % (" " * (59 - 19))),
            "\n\t%s" % ("%s  ******** ** ****" % (" " * (59 - 19))),
            "\n\t%s" % ("%s ******* ** ******" % (" " * (59 - 19))),
            "\n\t%s" % ("%s*** ***  ********" % (" " * (59 - 19))),
            "\n\t%s" % ("%s**** * *********" % (" " * (59 - 19))),
            "\n\t%s" % ("%s***** ********" % (" " * (59 - 19))),
            "\n\t%s" % ("%s **** ******" % (" " * (59 - 19))),
            "\n\t%s" % ("%s   *** **" % (" " * (59 - 19)))
        )

        header = "\n%s%s%s%s%s%s%s%s\n" % (
            "%s%s" % ("\t", "-" * 100),
            logo,
            "\n%s%s%s" % (
                "\t%s" % (("*" * 43).center(100, " ")),
                "\n\t%s" % ("* Sistema simulador de gestor de archivos *".center(100, " ")),
                "\n\t%s\n" % (("*" * 43).center(100, " "))
            ),
            "\n\t%s" % ("Creado por: ".center(100, " ")),
            "\n\t%s" % ("[Bryan Gonzales] [Edgar Benedetto] [Fabio Lagos]".center(100, " ")),
            "\n\t%s\n" % ("v 0.00.10".center(100, " ")),
            "\n\tSistema que gestiona archivos y carpetas en consola exclusivamente, almacenados en formato JSON.\n",
            "%s%s" % ("\t", "-" * 100)
        )

        print(header)
    
    def printError(self):
        commandError = "\n%s%s%s\n" % (
            "%s%s" % ("\t", "*" * 100),
            "\n\tEl comando ingresado es inválido. Corra el comando \"help\" para ayuda.\n",
            "%s%s" % ("\t", "*" * 100)
        )

        print(commandError)

    #Comandos de la consola
    def printHelp(self):
        help = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n" % (
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
            "\n\t\tfindfbe [EXTENSIÓN]\n\n\t\t\t---> Encontrar archivos por extensión.",
            #"%s%s" % ("\t", "-" * 100),
        )
        print(help)

    def plot(self):
        graph.plot(graph.lnk)
    
    def mkdir(self, name):
        refer  = self.rootes[-1]
        graph.add(name, "D", refer.value.name)
        
    def touch(self, name):
        refer = self.rootes[-1]
        graph.add(name, "F", refer.value.name)
    
    #Tratamiento de la cadena ingresada a un comando sportado por el sistema.
    def info(self, text):
        text = text.split(";")
        array = []

        for i in text:
            newArray = []
            i = i.strip()
            space = i.find(" ")

            if (space == -1):
                command, param = i[:],i[:]
            else: 
                command, param = i[:space], i[space:]

            newArray.append(command)
            newArray.append(param.strip())
            array.append(newArray)

        return array

    def cd(self, nodeName):
        if (nodeName == ".."):
            #condicional si esta en el root
            if (len(self.rootes) == 1):
                pass
            else:
                self.rootes.pop()
        else:
            nodeName = graph.navegation(nodeName)

            if (nodeName.value.nodeType == "D"):
                self.rootes.append(nodeName)
            else:
                print("\n\t\tRuta no encontrada.\n")

        return True

    def ls(self, typeLs = None):
        print(self.rootes[-1].value.edges.print(typeLs))

    def pwd(self):
        array = self.rootes
        route = ""

        for node in array:
            nameRute = node.value.name
            
            if (nameRute == "C:"):
                route = "%s%s" % (route, nameRute)
            else:
                route = "%s/%s" % (route, nameRute)

        route = "%s/" % route

        return "%s" % (route)

    #El parámetro debe ser una ruta de archivo obligatoriamente.
    def ln(self, text):
        subarray = []
        text = text.split("/")

        copyfile = text[-1]
        a = len(text)
        text = text[:a-1]
        direc = text[-1]

        file1 = self.rootes[-1].value.edges.search(copyfile)
        pos = (file1.value.name).find(".")
        
        if pos == -1:
            name = "%s.lnk" % file1.value.name
        else:
            name = "%s.lnk" % file1.value.name[:pos]

        subarray.append(name)
        subarray.append(file1.value.name)
        self.lk.append(subarray)
        graph.lnk = self.lk
        #print(graph.lnk)
        graph.saveLnk(graph.lnk)

        dir1 = graph.search(direc)
        
        if (file1 and dir1):
            graph.add(name, "F", dir1.value.name)
        else:
            print("\t\tLa dirección o el archivo no existe en el árbol")
        
    def rm(self, name):
        refer = self.rootes[-1]
                    
        if (graph.remove(name, "F", refer.value.name)):
            pass
        else:
            print("\t\tEl archivo que desea eliminar no existe")

    def rmdir(self, name):
        refer = self.rootes[-1]

        #Solo funciona para carpetas con nombres diferentes.
        if (graph.search(name)):
            graph.remove(name, "D", refer.value.name)
        else:
            print("\t\tEl directorio a eliminar no existe")
    
    def trash(self):
        listTrash = graph.trash
        print(graph.trash.print("trash"))
        graph.toCsv(listTrash,"Memory/Trash.csv")

    def findfbe(self, fileExtension):
        listOfFiles = graph.searchByExtension(fileExtension, self.rootes[-1].value.edges.first)
        trail = "\t\t"    

        for fileName in listOfFiles:
            trail += "%s%s%s" % ("\n", "\t\t", fileName)

        print("%s%s" % (trail, "\n"))

    #guarda la ruta en le JSON.
    def save(self, route):
        graph.saveJson(route)

    #Lee la ruta en el JSON.
    def read(self, route):
        graph.readJson(route)
    
    def lnk(self, route):
        graph.readLnk(route)
