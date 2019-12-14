# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
LinkedList (Lista enlazada)
---------------------------------------------------------------------------------------------------------------------

* Método "addList"
    Este método agrega jerárquicamente en orden ascendente (siendo la carpetas antes que los archivos) un directorio
    (D) o un archivo (F), verifcando primero si existe ya un directorio o archivo con el mismo nombre, si es así,
    muestra un mensaje indicandole al usario que no se puede agregar un elemento con el mismo nombre.

* Método "alreadyExist"
    Este método verifica si ya existe una carpeta o un archivo con el mismo nombre.

* Método "search"
    Este método busca y retorna la coincidencia del valor que es pasado como parámetro.

* Método "pop"
    Este método busca un nodo cuyo valor es el nombre del directorio o archivo, si determina que existe dicho valor,
    lo guarda en una variable temporal,lo elimina y retorna ese elemento eliminado guardado previamente en la
    variable temporal.

* Método "print"
    Este método retorna una cadena con formato, los valores de cada uno de los nodos de la lista enlazada,
    previamente ordenados mediante jerarquía alfabética y tipo de elemento (carpeta o archivo).

---------------------------------------------------------------------------------------------------------------------
"""

import math

from Core.TreeGraph.Compare import Compare
from Core.TreeGraph.Node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.compare = Compare()

    def addList(self, value, prev = None, current = None, date = None, parent = None):
        if (not self.first):
            self.first = Node(value, date, parent)
            return True

        if (not prev):
            prev = self.first
            #current = prev

        #Verifica su ya existe un elemento con el mismo valor.
        if (not self.alreadyExist(value)):
            #El directorio se interpretará como "D"
            if (value.nodeType == 'D'):
                if (prev.value.nodeType == 'D'):
                    if (self.compare.order(value.name, prev.value.name) > 0):
                        if (prev is self.first):
                            self.first = Node(value, date, parent)
                            self.first.next = prev

                            return True
                        else:
                            current.next = Node(value, date, parent)
                            current.next.next = prev

                            return True
                    else:
                        current = prev
                        prev = prev.next

                        if (prev):
                            return self.addList(value, prev, current, date, parent)
                        else:
                            current.next = Node(value, date, parent)

                            return True
                else:
                    if (prev.value.nodeType == 'F'):
                        if  (prev is self.first):
                            self.first = Node(value, date, parent)
                            self.first.next = prev
                            
                            return True
                        
                        current.next = Node(value, date, parent)
                        current.next.next = prev

                        return True
                    
                    if (prev is None):
                        current.next = Node(value, date, parent)

                        return True
            else:
                #El archivo se interpretará como "F"
                if (prev.value.nodeType == 'F'):
                    if (self.compare.order(value.name, prev.value.name) > 0):
                        if (prev is self.first):
                            self.first = Node(value, date, parent)
                            self.first.next = prev

                            return True
                        else:
                            current.next = Node(value, date, parent)
                            current.next.next = prev

                            return True
                    else:
                        if (prev):
                            current = prev
                            prev = prev.next

                            if (prev):
                                return self.addList(value, prev, current, date, parent)
                            else:
                                current.next = Node(value, date, parent)
                                return True
                else:
                    while (not (prev is None) and prev.value.nodeType == 'D'):
                        current = prev
                        prev = prev.next

                    if (prev is None):
                        current.next = Node(value, date, parent)

                        return True
                    else:
                        return self.addList(value, prev, current, date, parent)

    def alreadyExist(self, value):
        current = self.first
        
        while (current):
            if (current.value.name == value.name):
                return True

            current = current.next

        return False

    def search(self, value):
        if (not self.first):
            return False
        else:
            current = self.first

            while (current):
                if current.value.name == value:
                    return current

                current = current.next

            return False
    
    def pop(self, value, tp):
        if (not self.first):
            return False
        else:
            current = self.first

            if (current.value.name == value and current.value.nodeType == tp):
                parent = current
                self.first = self.first.next

                return parent
            else:
                prev = current
                current = current.next

                while (current):
                    if (current.value.name == value and current.value.nodeType == tp):        
                        parent = current
                        prev.next = current.next

                        return parent

                    prev = current
                    current = current.next

                return False

    def print(self, typeLs = None):
        trail = "\n\t\t"

        current = self.first
        
        #Valida la existencia de un parametro.
        if (typeLs == "-1"):
            #Construye una lista vertical.
            while (current):
                if (current.next):
                    trail += "{:96}\n\t\t".format(current.value.name)
                else:
                    trail += "{:96}".format(current.value.name)
                
                current = current.next
        else:
            #Construye una lista horizontal.
            ln = 1
            
            while (current):
                if (ln == 4):
                    #Asigna un ancho mínimo por cada valor de los nodos.
                    trail += "{:23}\n\t\t".format(current.value.name)
                    ln = 1
                else:
                    trail += "{:23}".format(current.value.name)
                    ln += 1

                current = current.next

        trail += "\n"

        return trail
