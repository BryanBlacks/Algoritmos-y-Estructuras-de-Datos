#-*- coding: utf-8 -*-
class GraphJSON:
    def __init__(self, json):
        self.graphNew = json

    def add_vertex1(self, vertex_name):
        self.graphNew["%s" % (vertex_name)] = []

    def add_edge1(self, vertex_origin, vertex_destination):
        if not (vertex_destination in self.graphNew["%s" % (vertex_origin)]):
            self.graphNew["%s" % (vertex_origin)].append(vertex_destination)
        
    def connectedVertices(self, x):
        graph,s = self.graphNew,{}
        for k,v in graph.items():
            if k == x:
                for i in v: 
                    s[i] = None
            elif x in v:
                s[k] = None
        return s.keys()

#Pruebas de Funcionamiento
"""
x = "A"
g = Graph1({})
g.add_vertex1("A")
g.add_vertex1("B")
g.add_vertex1("C")
g.add_vertex1("D")
g.add_edge1("B","A")
g.add_edge1("B", "A")
g.add_edge1("C", "A")
print("La conexion del nodo %s es: %s" % (x,g.connectedVertices(x)))
print("El grafo es: %s" % (g.graph))
"""
#Pruebas Pasadas, Puede ser implementado
