class Graph:
    def __init__(self, json):
        self.graph = json

    def add_vertex(self, vertex_name):
        self.graph["%s" % (vertex_name)] = []

    def add_edge(self, vertex_origin, vertex_destination):
        if not (vertex_destination in self.graph["%s" % (vertex_origin)]):
            self.graph["%s" % (vertex_origin)].append(vertex_destination)
        
    def connectedVertices(self, x):
        graph,s = self.graph,{}
        for k,v in graph.items():
            if k == x:
                for i in v: 
                    s[i] = None
            elif x in v:
                s[k] = None
        return s.keys()

x = "A"
g = Graph({})
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("B","A")
g.add_edge("B", "A")
g.add_edge("C", "A")
print("La conexion del nodo %s es: %s" % (x,g.connectedVertices(x)))
print("El grafo es: %s" % (g.graph))
