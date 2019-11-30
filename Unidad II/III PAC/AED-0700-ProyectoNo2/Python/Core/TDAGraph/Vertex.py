# -*- coding:utf8 -*-

from TDAGraph.LinkedList import LinkedList

class Vertex:
    def __init__(self,name,nodeType):
        self.name = name
        self.nodeType = nodeType
        self.edges = LinkedList()
    
    def setEdges(self, vertex_name):
        self.edges.add(vertex_name)