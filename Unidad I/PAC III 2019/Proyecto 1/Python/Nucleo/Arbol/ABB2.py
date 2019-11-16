#-*- coding:utf8 -*-
from Node import*
import networkx as nx
import matplotlib.pyplot as plt

class BST1:
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
                if not self.left:
                    current.left = Node(value)
                    return True
                else:
                    return self.addInner(value,current.left)
            else:
                if not self.right:
                    current.right = Node(value)
                    return True
                else:
                    return self.addInner(value,current.right)
            return False
