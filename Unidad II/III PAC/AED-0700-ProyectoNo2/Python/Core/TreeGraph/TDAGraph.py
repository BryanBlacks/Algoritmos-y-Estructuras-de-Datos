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
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

from Core.TreeGraph.Compare import Compare
from Core.TreeGraph.Node import Node
from Core.TreeGraph.LinkedList import LinkedList
from Core.TreeGraph.Vertex import Vertex
from Core.TreeGraph.JSON import Json

G = nx.DiGraph()

class TreeGraph:
    def __init__(self):
        #Ruta raiz del gestor de archivos.
        self.root = Node(Vertex("C:", "D"), None, None)
        #Papelera de reciclaje.
        self.trash = LinkedList()
        self.json = None

    def add(self, name, type_, reference = None):
        if (not reference):
            parentNode = self.root
            parentNode.value.edges.addList(Vertex(name, type_))
        else:
            parent = self.search(reference)
            parent.value.edges.addList(Vertex(name, type_))
        
    # Se busca en el arbol el nodo a tratar(value = nombre de carpeta)
    def search(self, value, current = None):
        comp = Compare()

        if (not current):
            current = self.root

        if (current.next):
            if (comp.compare(current.value.name, value)):
                return current
            else:
                #El directorio se interpretará como "D"
                if (current.value.nodeType == 'D'):
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
            if (comp.compare(current.value.name, value)):
                return current
            else:                
                if (current.value.nodeType == 'D'):
                    if (current.value.edges.first):
                        if (self.search(value, current.value.edges.first)):
                            current = current.value.edges.first

                            return self.search(value, current)
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
 
    # se borra de la ruta actual(carpeta actual) que es reference, el nodo(value)
    def remove(self, value,type_, reference = None):
        parent1 = self.search(reference)
        
        node = parent1.value.edges.pop(value, type_)
        if node:
            date1= datetime.datetime.now()

            #nodeDelete = Node(node.value,date,parent)
            self.trash.addList(value=node.value,date=date1,parent=parent1.value.name)
            return True
        
        else: return False

    def navegation(self, name):
        present = self.search(name)

        if (present):
            return present

        return False
    
    def searchByExtension(self, fileExtension, current):
        compare = Compare()

        files = []

        while (current):
            if (current.value.nodeType == 'F'):
                name = (current.value.name).partition(".")

                if compare.compare(str(name[2]), fileExtension):
                    files.append("".join(name))

            current = current.next

        return files[:] 
                          
    def convertJson(self):
        self.json = Json({})
        current = self.root

        self.json.add(current.value.name, current.value.nodeType)

        return self.convertInner(current)

    def convertInner(self, current, parent = None):
        if (parent):
            self.json.add(current.value.name, current.value.nodeType, parent.value.name)
        
        children = self.array(current)

        for node in children:
            parent1 = current
            self.convertInner(node, parent1)

        return True

    def array(self, current):
        array = []
        son = current.value.edges.first

        while (son):
            array.append(son)
            son = son.next
        
        return array

    def saveJson(self, rute):
        self.convertJson()
        
        f = open(rute, "w")
        #f.write("self.json.json")
        f.write("%s"%(self.json.json))

        f.close()

    def readJson(self, rute = None):
        f = open(rute, 'r')
        s = f.read()
        s = s.replace('\t', '')
        s = s.replace('\n', '')
        s = s.replace("'", '"')
        jsonx = json.loads(s)

        f.close()

        for k, v in jsonx.items():
            root = k
            d = v

            break

        self.JsonToTree(d, root)

    def JsonToTree(self,json, parent):
        #parent = C:
        #json = {'c1': {'q7': {}, 'q8': {'96': 'F'}}, 'c2': {'ae5': {}}, 'a5': 'F'}
        for k, v in json.items():
            if (isinstance(v, dict)):
                self.add(k, "D", parent)
                self.JsonToTree(v, k)
            else:
                self.add(k, "F", parent)

        return True
            

                
    def plot(self, array):
        
        self.convertJson()
        json = self.json.json
        self.plotInner(json)

        for i in array:
            G.add_edge(i[0],i[1])

        write_dot(G,'Memory/test.dot')
        pos = graphviz_layout(G, prog='dot')
        nx.draw(G,pos, with_labels=True, arrows=True)

        plt.show()

    def plotInner(self,j, parent = None):
        for k, v in j.items():
            if (not parent): G.add_node(k)
            else: G.add_edge(parent, k)
            
            if (isinstance(v, dict)):
                for a, b in v.items():
                    if (isinstance(b, dict)):
                        G.add_edge(k, a)
                        self.plotInner(b, a)
                    else: G.add_edge(k, a)

        
        return True    
        
    def toCsv(self,listTrash,filename):
        current = listTrash.first
        csv = "Nombre, Tipo, Fecha, Directorio Origen\n"

        while(current):
            csv = "%s%s,%s,%s,%s%s"%(csv,current.value.name,current.value.nodeType,current.date,current.parent,"\n") 
            current = current.next

        file1 = open(filename,"w")
        file1.write(csv)
        file1.close()

    def csvToLinked(self,file1):
        pd=[]
        con = open(file1,"r")
        contenc = con.read()
        rows = contenc.split("\n")
        con.close()
        for row in rows:
            cont = row.split(",")
            pd.append(cont)
        
        #nodeDelete = Node(node.value,date,parent)
        
        for i in range(1,len(pd)-1):
            newVertex = Vertex(str(pd[i][0]),str(pd[i][1]))
            print(pd[i][3])
            newParent = self.search(pd[i][3])

            self.trash.addList(value =newVertex,date=str(pd[i][2]),parent=newParent.value.name)
        
        