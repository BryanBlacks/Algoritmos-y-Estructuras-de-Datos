class Vertex:

    def __init__(self,name,nodeType):
        self.name = name
        self.nodeType = nodeType
        self.edge = LinkeList()
    
    def setEdges(self, vertex_name):
        self.edges.add(vertex_name)
