#-*- coding:utf8 -*-
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

G = nx.DiGraph()
image = plt.figure()

class Node:
    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        return self.addInner(value,self.root)

    def addInner(self, value, current):
        if not self.root:
            self.root = Node(value)
            return True
        else:
            if current.value == value:
                current = Node(value)
                return True
            if current.value > value:
                if not current.leftChild:
                    current.leftChild = Node(value)
                    return True
                else:
                    return self.addInner(value,current.leftChild)
            else:
                if not current.rightChild:
                    current.rightChild = Node(value)
                    return True
                else:
                    return self.addInner(value,current.rightChild)
            return False

    def toMap(self):
        G.add_node("%s" %(self.root.value))
        return self.toMapInner(self.root)

    def toMapInner(self,current):

        if current.leftChild:
            G.add_node("%s"%(current.leftChild.value))
            G.add_edge("%s"%(current.value), "%s"%(current.leftChild.value))
            self.toMapInner(current.leftChild)

        if current.rightChild:
            G.add_node("%s"%(current.rightChild.value))
            G.add_edge("%s"%(current.value), "%s"%(current.rightChild.value))
            self.toMapInner(current.rightChild)
            
        return True

    def showMap(self):
        self.toMap()
        nlist = [node for node in G.nodes()]
        elist = [edge for edge in G.edges()]
        #pos = nx.bipartite_layout(G, nlist, align='vertical', scale=1, center=None, aspect_ratio=4/3)
        pos = nx.bfs_tree(G,self.root.value)
        nx.draw(G,nodelist=nlist,edgelist=elist,with_labels=True,node_size=300)
        image.savefig('/home/benedetto/Documentos/AED 0700 III PAC/Unidad I/PAC III 2019/map.png')

bst = BST()
bst.add(2)
bst.add(4)
bst.add(3)
bst.add(6)
bst.add(7)
bst.add(5)
bst.add(8)
bst.add(9)


bst.showMap()