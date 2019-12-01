# -*- coding: utf 8 -*-
from Core.TreeGraph.LinkedList import*

class Vertex:

    def __init__(self, name, nodeType):
        self.name = name
        self.nodeType = nodeType
        self.edges = LinkedList()
    
    def setEdges(self, vertexName):
        self.edges.addList(vertexName)

