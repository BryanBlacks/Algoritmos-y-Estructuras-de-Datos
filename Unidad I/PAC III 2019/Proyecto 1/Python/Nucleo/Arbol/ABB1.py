#-*- coding:utf8 -*-
from Nucleo.Arbol.Node import *

import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt


class BST:
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
                current = Node(value,name)
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


    def showMapHNL(self):
        G = nx.DiGraph()
        images = plt.figure()

        self.toMap(G)
        nlist = [node for node in G.nodes()]
        elist = [edge for edge in G.edges()]
        write_dot(G,'Memoria/test.dot')
        pos = graphviz_layout(G, prog='dot')
        nx.draw(G,pos, with_labels=True, arrows=True, node_size=5000,node_color='#a8dee3',node_shape='8')
        #so^>v<dph8
        #plt.show()
        images.savefig("Memoria/BST1.png")

    def toMap(self,G):
        G.add_node("%s | %s"%(self.root.value, self.root.name))
        return self.toMapInner(G,self.root)

    def toMapInner(self,G,current):

        if current.left:
            G.add_node("%s | %s"%(current.left.value, current.left.name))
            G.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.left.value, current.left.name))
            self.toMapInner(G,current.left)

        if current.right:
            G.add_node("%s | %s"%(current.right.value, current.right.name))
            G.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.right.value, current.right.name))
            self.toMapInner(G,current.right)

            
        return True