#-*- coding:utf8 -*-
from Nucleo.Arbol.Node import *
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

H = nx.DiGraph()
image = plt.figure()

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

    def toMap(self):
        H.add_node("%s | %s"%(self.root.value, self.root.name))
        return self.toMapInner(self.root)

    def toMapInner(self,current):

        if current.left:
            H.add_node("%s | %s"%(current.left.value, current.left.name))
            H.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.left.value, current.left.name))
            self.toMapInner(current.left)

        if current.right:
            H.add_node("%s | %s"%(current.right.value, current.right.name))
            H.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.right.value, current.right.name))
            self.toMapInner(current.right)
            
        return True

    def showMapUSD(self):
        self.toMap()
        nlist = [node for node in H.nodes()]
        elist = [edge for edge in H.edges()]
        write_dot(H,'Memoria/test.dot')
        pos = graphviz_layout(H, prog='dot')
        nx.draw(H,pos, with_labels=True, arrows=True, nodelist=nlist, edgelist=elist,node_size=7000,node_color='#a8dee3',node_shape='8',linewidths=True,style='solid',arrowsize=30)
        #so^>v<dph8
        image.savefig("Memoria/BST2.png")
