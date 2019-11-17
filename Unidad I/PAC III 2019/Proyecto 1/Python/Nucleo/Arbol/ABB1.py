#-*- coding:utf8 -*-
from Nucleo.Arbol.Node import *
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
image = plt.figure()

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
            elif current.value > value:
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

    """
    def toMap(self):
        return self.toMapInner(self.root)
        
    def toMapInner(self,current):
        if current.rightChild or current.leftChild:
            if current.rightChild and current.leftChild:
                G.add_node(current.leftChild)
                G.add_node(current.rightChild)
                G.add_edge(current, current.leftChild)
                G.add_edge(current, current.rightChild)
            elif current.leftChild and not current.rightChild:
                G.add_node(current.leftChild)
                G.add_edge(current,current.leftChild)
                return self.toMapInner(current.leftChild)
            elif current.rightChild and not current.leftChild:
                G.add_node(current.rightChild)
                G.add_edge(current, current.rightChild)
                return self.toMapInner(current.rightChild)
        plt.show()
        
            current = self.root
            G.add_node(self.root)
            while current.leftChild or current.rightChild:
                if current.rightChild and current.leftChild:
                    G.add_node(current.leftChild)
                    G.add_node(current.rightChild)
                    G.add_edge(current, current.leftChild)
                    G.add_edge(current, current.rightChild)
                    if current.rightChild.rightChild:
                        current = current.rightChild
                    else: 
                elif current.leftChild and not current.rightChild:
                    G.add_node(current.leftChild)
                    G.add_edge(current,current.leftChild)
                    current = current.leftChild
                elif current.rightChild and not current.leftChild:
                    G.add_node(current.rightChild)
                    G.add_edge(current, current.rightChild)
                    current = current.rightChild
        
        plt.show()
        """

    def toMap(self):
        G.add_node("%s | %s"%(self.root.value, self.root.name))
        return mappInner(self.root)

    def toMapInner(self,current):

        if current.left:
            G.add_node("%s | %s"%(current.left.value, current.left.name))
            G.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.left.value, current.left.name))
            self.mapp(current.left)

        if current.right:
            G.add_node("%s | %s"%(current.right.value, current.right.name))
            G.add_edge("%s | %s"%(current.value,current.name), "%s | %s"%(current.right.value, current.right.name))
            self.mapp(current.right)
            
        return True


