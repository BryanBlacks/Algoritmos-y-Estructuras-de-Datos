# -*- coding:utf8 -*-

from TDAGraph.Node import Node
from TDAGraph.Vertex import Vertex

class TreeGraph:
    def __init__(self):
        self.root = Node(Vertex("C:\""))

    def add(self, value, current=None):
        if not current:
            current = self.root
            return current.children.add(value)
        else:
            pass

    def search(self):
        pass
