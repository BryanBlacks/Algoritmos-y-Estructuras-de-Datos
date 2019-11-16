#-*- coding:utf8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
image = plt.figure()

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
            elif current.value > value:
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
        """
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
        """
        plt.show()