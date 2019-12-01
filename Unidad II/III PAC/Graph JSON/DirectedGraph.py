#-*- coding:utf8 -*-
class Graph:
    def __init__(self,graph = {}):
        self.graph = graph

    def add(self,vertex):
        #Hay que agregar un nuevo indice(key) en el diccionario
        print("Se ha agregado el vertex %s" %(vertex))
        self.graph[("%s" % vertex).strip()] = {}

    def edge(self,vertexA,vertexB,weight = 1):
        #Para conectar los vertices recien agregados
        #Puede que el vertice A y B no existan en el grafo

        #Si se quiere crear un nuevo edge 
        if ((self.graph[("%s" % vertexA).strip()] or self.graph[("%s" % vertexA).strip()] =={}) and (self.graph[("%s" % vertexB).strip()] or self.graph[("%s" % vertexB).strip()] == {})):
            #Al tener el peso el siguiente if es innecesario ni el append
            if(self.graph[("%s" % vertexB).strip()] not in list(self.graph[("%s" % vertexA).strip()].keys())):
                #No se están quitando los duplicados
                print("Se ha conectado %s con %s" % (vertexA,vertexB))
            #self.graph[("%s" % vertexA).strip()].append(("%s" % vertexB).strip())

                self.graph[("%s" % vertexA).strip()][("%s" % vertexB).strip()] = weight
                self.edge(vertexB,vertexA,weight)
        
    def __str__(self):
        return "%s" % self.graph

    def directedConnectWith(self,X):
        graph = self.graph
        r = {}
        for k,v in self.graph.items():
            if X == k:
                for i,j in v:
                    r[("%s" % i).strip()] = None
            elif (X in list(v.keys())):
                r[("%s" %k).strip()] = None
        return list(r.keys())

    
"""
    def undirectedConnectWith(self,X):
        graph = self.graph
        r = {}
        for k,v in self.graph.items():
            if X == k:
                for i in v:
                    r[("%s" % i).strip()] = None
            elif X in v:
                r[("%s" %k).strip()] = None
        return list(r.keys())

    def directedConnectWith(self,X):
        graph = self.graph
        json = {}
        for k,v in graph.items():
            if X in v:
                #Se pone none porque los valores en un json no se pueden repetir
                json[("%s" %k).strip()] = None
        return list(json.keys())
"""
"""
Considerando  un JSOn que tenga los pesos en las aristas, ese JSON debe ser modificado dependiendo
    el problema, por ejemplo que cada uno de los elementos tengan un JSON 

    'A' : ['B':0.1, 'C':0.1]
    'B' : ['C':0.1, 'A':0.1]
    'C' : ['A':0.1, 'C':0.1, 'D':0.1]
    'D' : ['B':0.1, 'C':0.1]
"""
X = "A"
g = Graph()
g.add("A")
g.add("B")
g.add("C")
g.add("D")
g.edge("A","B",0.1)
g.edge("A","C",0.1)
g.edge("B","C",0.1)
g.edge("C","D",0.1)
print("\n"*2)
print("Para el grafo no dirigido %s, los nodos que se conectan con %s son: %s" % (g,X,g.directedConnectWith(X)))
