class Vertex:

    def __init__(self,name):
        self.name = name
        self.type = None
        self.edge = LinkeList()
    
    def setEdges(self, vertex_name):
        self.edges.add(vertex_name)

class Edge:
     def __init__(self, )