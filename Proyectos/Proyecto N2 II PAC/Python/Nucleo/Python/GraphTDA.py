#-*- coding: utf-8 -*-
from Nucleo.Python.GraphJson import *

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
            self.first = Node(Vertex(value))
            return True
        else:
            if not self.alreadyExist(value):
                current = self.first
                while(current.next):
                    current = current.next
                current.next = Node(Vertex(value))
                return True
            return False
    
    def alreadyExist(self, value):
        current = self.first
        while(current):
            if (current.value.name == value):
                return True
            current = current.next
        return False
    
    def search(self, value):
        current = self.first
        while(current):
            if current.value.name == value:
                return current.value
            current = current.next
        return False
    
    def searchEdge(self, o, d):
        current = self.search(o)
        while(current):
            if(current):
                anex = current.edges.first
                while(anex):
                    if (anex.value.name == d):
                        return anex.value
                    anex= anex.next

            current = current.next
        

#Los vertices son tipo nodos
class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = LinkedList()
        self.carac = []
    
    def setEdges(self, vertex_name):
        self.edges.add(vertex_name)

class Edge:
    def __init__(self, name):
        self.name = name
        #self.characteristic = LinkedList()

class GraphInner:
    def __init__(self):
        self.vertex = LinkedList()

    def add_vertex(self, vertex_name):
        self.vertex.add(vertex_name)
    
    def add_edge(self, vertex_origin, vertex_destination):
        vertex = self.vertex.search(vertex_origin)
        if not vertex.edges.alreadyExist(vertex_destination):
            vertex.setEdges(vertex_destination)
    
    def add_caract(self,origin , destiny, array):
        edge = self.vertex.searchEdge(origin,destiny)
        edge.carac.append(array)
    
    def print1(self):
        current= self.vertex.first.value.edges.first
        while(current):
            if(current):
                print(current.value.carac)
            current=current.next

    def connectionVertices(self, x):
        vertex, s = self.vertex, {}
        current = vertex.first

        while(current):
            if(current.value.name == x):
                edges = current.value.edges
                current_edge = edges.first
                while(current_edge):
                    s[current_edge.value.name] = None
                    current_edge = current_edge.next
            elif current.value.edges.alreadyExist(x):
                s[current.value.name] = None
            current = current.next
        return list(s.keys())

    #Función para convertir lo agregado al grafo tipo json a un json total
    def convertJson(self, current=None):
        a = GraphJSON({})

        if not current:
            current = self.vertex.first
        
        while current:
            a.add_vertex1(current.value.name)
            anex = current.value.edges.first
            while anex:
                a.add_edge1(current.value.name, anex.value.name)
                anex= anex.next
            current= current.next
        #print(a.graphNew)
        return a.graphNew
    
#Pruebas del grafo tipo TDA
"""
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B")
print("El grafo es: %s" % (g.vertex))
g.convertJson()
x = "A"
print("Los vertices conectados a '%s' son '%s'" %(x, g.connectionVertices(x)))
"""
#Fin de pruebas, puede ser implementado