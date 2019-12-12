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
import json
from Core.TreeGraph.Compare import Compare
from Core.TreeGraph.Node import Node
from Core.TreeGraph.LinkedList import LinkedList
from Core.TreeGraph.Vertex import Vertex
from Core.TreeGraph.JSON import Json

class TreeGraph:
    def __init__(self):
        #Ruta raiz del gestor de archivos.
        self.root = Node(Vertex("C:","D"), None, None)
        #Papelera de reciclaje.
        self.trash = LinkedList()
        self.json = None

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
        parent1 = self.search(reference)
        
        node = parent1.value.edges.pop(value)
        date1= datetime.datetime.now()

        #nodeDelete = Node(node.value,date,parent)
        self.trash.addList(value=node.value,date=date1,parent=parent1)

    def navegation(self, name):
        present = self.search(name)
        if present:
            return present

        return False
    
    def searchByExtension(self):
        pass

    def convertJson(self):

        self.json = Json({})
        current = self.root

        self.json.add(current.value.name, current.value.nodeType)

        return self.convertInner(current)

    def convertInner(self, current, parent = None):

        if parent:
            self.json.add(current.value.name, current.value.nodeType, parent.value.name)
        
        children = self.array(current)
        for node in children:
            parent1 = current
            self.convertInner(node, parent1)
        return True

    def array(self, current):
        
        array = []
        son = current.value.edges.first

        while son:
            array.append(son)
            son = son.next
        
        return array

    def saveJson(self, rute):

        self.convertJson()
        
        f = open(rute,"w")
        #f.write("self.json.json")
        f.write("%s"%(self.json.json))

        f.close()

    def readJson(self, rute= None):
        
        f = open(rute,'r')
        s = f.read()
        s = s.replace('\t','')
        s = s.replace('\n','')
        s = s.replace("'",'"')
        jsonx = json.loads(s)

        f.close()
        for k,v in jsonx.items():
            root = k
            d = v
            break

        #self.JsonToTree(d,root)

    def JsonToTree(self,json, parent):

        for k,v in json.items():

            if isinstance(v,dict):
                pass

        
        