# -*- coding: utf 8 -*-

import math

from Core.TreeGraph.Compare import *
from Core.TreeGraph.Node import *

class LinkedList:
    def __init__(self):
        self.first = None
        self.compare = Compare()

    #Agrega jerarquicamente en orden ascendente( siendo la carpetas antes que los archivos)
    def addList(self, value, prev = None, current = None):
            
            if(not self.first):
                self.first = Node(value)
                return True

            if(not prev):
                prev = self.first
                #current = prev

            if not self.alreadyExist(value):
            
                if( value.nodeType == 'D'):
                        if( prev.value.nodeType == 'D'):
                            
                            if( self.compare.order(value.name,prev.value.name) > 0 ):
                                if(prev is self.first):
                                    self.first = Node(value)
                                    self.first.next = prev
                                    return True
                                else:
                                    current.next = Node(value)
                                    current.next.next = prev
                                    return True

                            else:
                                current = prev
                                prev = prev.next
                                if prev:
                                    return self.addList(value,prev,current)
                                else:
                                    current.next = Node(value)
                                    return True

                                


                        else:
                            if( prev.value.nodeType == 'F'):
                                if prev is self.first:
                                    self.first = Node(value)
                                    self.first.next = prev
                                    return True
                                
                                current.next = Node(value)
                                current.next.next = prev
                                return True
                            
                            if(prev is None):
                                current.next = Node(value)
                                return True

                else:
                        if(prev.value.nodeType == 'F'):

                            if( self.compare.order(value.name,prev.value.name) > 0 ):
                                if(prev is self.first):
                                    self.first = Node(value)
                                    self.first.next = prev
                                    return True
                                else:
                                    current.next = Node(value)
                                    current.next.next = prev
                                    return True

                            else:
                                if(prev):
                                    current = prev
                                    prev = prev.next
                                    if prev:
                                        return self.addList(value,prev,current)
                                    else:
                                        current.next = Node(value)
                                        return True

                        else:
                            while(not(prev is None) and prev.value.nodeType == 'D' ):
                                current = prev
                                prev = prev.next

                            if(prev is None):
                                current.next = Node(value)
                                return True
                            
                            else:
                                return self.addList(value,prev,current)


    def alreadyExist(self, value):
            current = self.first
            while(current):
                if (current.value.name == value.name):
                    return True
                current = current.next
            return False

    def search(self,value):
        if not self.first:
            return False
        else:
            current  = self.first
            while current:
                if current.value.name == value:
                    return current
                current = current.next
            return False
    
    #Elimina el nodo(value = nombre de carpeta o archivo), y retorna el nodo eliminado
    def pop(self,value):
        if not self.first:
            return False
        else:
            current  = self.first
            if current.value.name == value:
                parent = current
                self.first = self.first.next
                return parent
            else:
                prev = current
                current = current.next
                while current:
                    if current.value.name == value:        
                        parent = current
                        prev.next = current.next
                        return parent
                    current = current.next
                return False

    def print(self, typeLs = None):
        trail = "\t\t"

        current = self.first
        
        if (typeLs == "-1"):
            while (current):
                trail += "{:96}\n\t\t".format(current.value.name)
                
                current = current.next
        else:
            ln = 1
            
            while (current):
                if (ln == 4):
                    trail += "{:23}\n\t\t".format(current.value.name)
                    ln = 1
                else:
                    trail += "{:23}".format(current.value.name)
                    ln += 1

                current = current.next

        return trail