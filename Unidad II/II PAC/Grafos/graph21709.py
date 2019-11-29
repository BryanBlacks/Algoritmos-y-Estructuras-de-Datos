#-*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
    
    def __str__(self):
        p = []
        current = self.first
        while(current):
            p.append(current.value.name)
            current = current.next
        return ",".join(p)
            
    def add(self, value):
        if not self.first:
            self.first = Node(value)
            return True
        else:
            if not self.alreadyExist(value):
                current = self.first
                while(current.next):
                    current = current.next
                current.next = Node(value)
                return True
            return False
    
    def alreadyExist(self, value):
        current = self.first
        while(current):
            if (current.value.name == value.name):
                return True
            current = current.next
        return False

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = LinkedList()

class Graph:
    def __init__(self):
        self.vertex = LinkedList()

    def add_vertex(self, vertex_name):
        self.vertex.add(Vertex(vertex_name))
    
    def add_edge(self, vertex_origin, vertex_destination):
        pass
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
print("El grafo es: %s" % (g.vertex.__str__()))