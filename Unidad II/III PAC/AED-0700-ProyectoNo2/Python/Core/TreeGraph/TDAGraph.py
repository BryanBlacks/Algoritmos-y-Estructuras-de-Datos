# -*- coding:utf8 -*-
import datetime
from Core.TreeGraph.Compare import*
from Core.TreeGraph.Node import*
from Core.TreeGraph.LinkedList import*
from Core.TreeGraph.Vertex import Vertex

class TreeGraph:
    def __init__(self):
        self.root = Node(Vertex("C:\"","D"))
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
                if(current.value.nodeType == 'D'):
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
            if(comp.compare(current.value.name,value)):
                return current
            
            else:                

                if(current.value.nodeType == 'D'):
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
        
    
        parent = self.search(reference)
        
        node = parent.value.edge.pop(value)
        date= datetime.datetime.now()

        nodeDelete = Node(node.value,date,parent)
        self.trash.addList(nodeDelete)

    def navegation(self, name):

        present = self.search(name)
        if present:
            return present

        return False
    
    def searchByExtension(self, )

"""
tree = TreeGraph()

tree.add("Tu Mama","D")
tree.add("Tu Papa","D")
tree.add("Hijo1","F","Tu Mama")
tree.add("Hijoa2","D","Tu Mama")
tree.add("sohan","F","Tu Mama")
tree.add("pedro","D","Tu Mama")
tree.add("NuevoPedro","D","pedro")
tree.add("NuevoPedro1","F","pedro")

tree.add("Hijoa1","D","Tu Papa")
tree.add("Hijo2","F","Tu Papa")
tree.add("Hijo3","D","Tu Papa")
tree.add("Hijo1","D","Tu Papa")
tree.add("elsr","F","Tu Papa")
tree.add("tupak","F","Tu Papa")
tree.add("wer","D","Tu Papa")
tree.add("Nuevo","D","Hijo1")
tree.add("Nuevo2","F","Hijo1")
tree.add("Nuevo3","F","Hijo1")
tree.add("Nuevo3","F","Hijo3")

print(tree.root.value.edge)

a = tree.root.value.edge.first
print(a.value.edge)

b = tree.search("Tu Mama")
print(b.value.edge)

c = tree.search("Hijo1")
print(c.value.edge)

d = tree.search("Hijo3")
print(d.value.edge)

e = tree.search("pedro")
print(e.value.edge)
"""