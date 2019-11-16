#-*- coding:utf8 -*-
import networkx as nx
import matplotlib.pyplot as plt

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        return self.addInner(value,self.root)

    def addInner(self, value, current):
        if not self.first:
            self.root = Node(value)
            return True
        else:
            if current.value = value:
                current = Node(value)
                return True
            elif current.value > value:
                if not self.leftChild:
                    current.leftChild = Node(value)
                    return True
                else:
                    return self.addInner(value,current.leftChild)
            else:
                if not self.rightChild:
                    current.rightChild = Node(value)
                    return True
                else:
                    return self.addInner(value,current.rightChild)
            return False
