#-*- coding:utf8 -*-
from Nucleo.Arbol.Node import *
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

"""
-------------------------------Árbol De Costos en Dolares-------------------------------
* Árbol Binario que almacena el precio y el nombre de los productos existentes en la 
    lista enlazada.

* Función Agregar ---> Función recursiva en la cual el usuario solo hace uso del
    add e internamente se usa la función addInner para moverse en el árbol dependiendo
    del value (precio del nodo tipo producto) que se desee ingresar.

* Función Mostrar Mapa ---> Función que hace la instancia del graph direccionado y 
    utiliza el plt para guardar la figura en una variable temporal que prograsivamente
    será guardada en memoría para luego embeber la imagén en la pantalla respectiva 
    del árbol que internamente hace uso de la función que agrega los nodos en el graph
    Luego con el layout especifico para generar la jerarquía del árbol binario por
    último se dibuja y guarda la imagén en memoria.

* Función Hacía el Mapa ---> Función que agrega el primer nodo con su value y el nombre
    que fueron almacenados en el árbol binario, haciendo uso de una función interna 
    para agregar de manera recursiva los nodos en el graph direccionado.
-----------------------------------------------------------------------------------------
"""

class BST1:
    def __init__(self):
        self.root = None

    def add(self, value,name):
        return self.addInner(value,name,self.root)

    def addInner(self, value,name, current):
        if not self.root:
            self.root = Node(value,name)
            return True
        else:
            if current.value == value:
                currentname = current.name
                current = Node(value,'%s%s'%(currentname,name))
                return True
            else:
                if current.value > value:
                    if not current.left:
                        current.left = Node(value,name)
                        return True
                    else:
                        return self.addInner(value,name,current.left)
                else:
                    if not current.right:
                        current.right = Node(value,name)
                        return True
                    else:
                        return self.addInner(value,name,current.right)
            return False


    def showMapUSD(self):
        H = nx.DiGraph()
        image = plt.figure()

        self.toMap1(H)
        nlist = [node for node in H.nodes()]
        elist = [edge for edge in H.edges()]
        write_dot(H,'Memoria/test1.dot')
        pos1 = graphviz_layout(H, prog='dot')
        nx.draw(H, pos1, with_labels=True, arrows=True, node_size=7000,node_color='#a8dee3',node_shape='8')
        #Formas para el nodo: so^>v<dph8
        #plt.show()
        image.savefig("Memoria/BST2.png")


    def toMap1(self,H):
        H.add_node("%s | %s"%(self.root.value, self.root.name))
        return self.toMapInner1(H,self.root)

    def toMapInner1(self,H,current):

        if current.left:
            H.add_node("%s | %s"%(current.left.value, current.left.name))
            H.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.left.value, current.left.name))
            self.toMapInner1(H,current.left)
        if current.right:
            H.add_node("%s | %s"%(current.right.value, current.right.name))
            H.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.right.value, current.right.name))
            self.toMapInner1(H,current.right)

            
        return True

