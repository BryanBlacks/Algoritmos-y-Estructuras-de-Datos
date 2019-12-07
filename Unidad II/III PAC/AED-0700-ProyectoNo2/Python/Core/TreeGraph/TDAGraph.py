# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
TDAGraph (Grafo)
---------------------------------------------------------------------------------------------------------------------

* Método "add"
    Este método agrega un vértice en la raiz del árbol, cuyo valor es una carpeta o un archivo. La secuencia de
    escritura en el árbol consiste en guardar un directorio o un archivo en un modelo Vertex, que a su vez este
    será almacenado en un modelo Node, para finalmente guardarlo en una lista enlazada que será utilizada como
    almacen de los subdirectorios y archivos hijos del mismo, es decir, esta lista serán las aristas del árbol.

* Método "search"
    Este método recursivo busca una coincidencia del valor recibido como parámetro con cada uno de los elementos en
    el árbol, retornando así un nodo para luego ser tratado u procesado durante la ejecución del programa.

* Método "remove"
    Este método remueve un directorio o archivo del árbol, utilizando la misma función de la lista enlazada.

* Método "navegation"
    Este método buscará dentro del árbol, utilizando la función "search", para obtener una arista especifica 
    que es requerida por el usuario, y que es buscada por el nombre de la arista a encontrar.

* Método "searchByExtension"
    Este método busca dentro del árbol, en cada una de sus subdirectorios, los archivos cuya extensión 
    concuerden con la entrada obtendina del usuario.


---------------------------------------------------------------------------------------------------------------------
"""

import datetime
from Core.TreeGraph.Compare import*
from Core.TreeGraph.Node import*
from Core.TreeGraph.LinkedList import*
from Core.TreeGraph.Vertex import Vertex

class TreeGraph:
    def __init__(self):
        #Ruta raiz del gestor de archivos.
        self.root = Node(Vertex("C:","D"), None, None)
        #Papelera de reciclaje.
        self.trash = LinkedList()

    def add(self, name, type_, reference = None):
        if(not reference):
            parentNode = self.root
            parentNode.value.edges.addList(Vertex(name, type_))

        else:
            parent = self.search(reference)
            parent.value.edges.addList(Vertex(name, type_))
        
    # Se busca en el arbol el nodo a tratar(value = nombre de archivo o carpeta)
    def search(self, value, current = None):
        comp = Compare()

        if (not current):
            current=  self.root

        if (current.next):
            if (comp.compare(current.value.name, value)):
                return current

            else:
                #El directorio se interpretará como "D"
                if(current.value.nodeType == 'D'):
                    if (current.value.edges.first):
                        if (self.search(value, current.value.edges.first)):
                            current = current.value.edges.first
                            return self.search(value, current)

                        else:
                            current = current.next
                            return self.search(value, current)

                    else:
                        current = current.next
                        return self.search(value, current)

                else:
                    current = current.next
                    return self.search(value, current)

        else:
            if(comp.compare(current.value.name, value)):
                return current

            else:                
                if(current.value.nodeType == 'D'):
                    if(current.value.edges.first):
                        if(self.search(value,current.value.edges.first)):
                            current = current.value.edges.first
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
        
        node = parent.value.edges.pop(value)
        date= datetime.datetime.now()

        nodeDelete = Node(node.value,date,parent)
        self.trash.addList(nodeDelete)

    def navegation(self, name):
        present = self.search(name)
        if present:
            return present

        return False
    
    def searchByExtension(self):
        pass

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

print(tree.root.value.edges)

a = tree.root.value.edges.first
print(a.value.edges)

b = tree.search("Tu Mama")
print(b.value.edges)

c = tree.search("Hijo1")
print(c.value.edges)

d = tree.search("Hijo3")
print(d.value.edges)

e = tree.search("pedro")
print(e.value.edges)
"""