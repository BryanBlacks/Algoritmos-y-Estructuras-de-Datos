<<<<<<< HEAD
from Compare import*
from LinkedList import*
=======
# -*- coding:utf8 -*-

from TDAGraph.Node import Node
from TDAGraph.Vertex import Vertex
>>>>>>> 2851268404ffc3884d93db15c300a1b8b9e7c58d

class TreeGraph:
    def __init__(self):
        self.root = Node(Vertex("C:\""))
        self.trash = LinkedList()

    def add(self, name, type_, reference =None):

        if(not reference):
            parentNode = self.root
            parentNode.value.edge.addList(Vertex(name,type_))

        else:
            parent = self.search(reference)
            parent.value.edge.addList(Vertex(name,type_))
        
    # Se busca en el arbol el nodo a tratar(value = nombre de archivo o carpeta)
    def search(self, value, current = None):

        comp = Compare()

        if(not current):
            current=  self.root

        if current.next:
            if(comp.compare(current.value.name,value)):
                return current
            
            else:
                if(current.value.type == 'D'):
                    if (current.value.edge.first):
                        if (self.search(value, current.value.edge.first)):
                            current = current.value.edge.first
                            return self.search(value, current)
                        
                        else:
                            current = current.next
                            return self.search(value, current)

                    else:
                        current = current.next
                        return self.search(value, current)
                else:
                    current = current.next
                    return self.search(value,current)



        else:
<<<<<<< HEAD
            if(comp.compare(current.value.name,value)):
                return current
            
            else:                

                if(current.value.type == 'D'):
                    if(current.value.edge.first):
                        if(self.search(value,current.value.edge.first)):
                            current = current.value.edge.first
                            return self.search(value, current)
                        
                        else:
                            return None

                    else:
                        return None
                else:
                    return None
 
    # se borra de la ruta actual(carpeta actual) que es reference, el nodo(value)
    def remove(self, value, reference = None):
        
        if not reference:
            parentNode = self.root
            parentNode.value.edge.pop(value)

        else:
            parent = self.search(reference)
            parent.value.edge.pop(value)

    def navegation(self, name):

        present = self.search(name)
        if present:
            return present

        return False
=======
            pass

    def search(self):
        pass
>>>>>>> 2851268404ffc3884d93db15c300a1b8b9e7c58d
