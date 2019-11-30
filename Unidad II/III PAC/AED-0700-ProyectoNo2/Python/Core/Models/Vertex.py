# -*- coding:utf8 -*-

from Core.LinkedList import LinkedList

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = LinkedList()