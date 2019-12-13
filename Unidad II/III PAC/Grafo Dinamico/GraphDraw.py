import networkx as nx
import matplotlib.pyplot as plt
from DinamicGraph import *

G = nx.Graph()
#Quitar el comentario y comentar 8 y 9 para el anterior programa
#g = {"C:" : {c1 : { ca1: {}, ca2: {} }, c2: { qe: "f" }, a1: "f", a2: "f"}
g = DynamicGraphGenerator()
g = g.create()

for k,v in g.items():
    G.add_node("%s" % (k))
    print("Procesando el vertice %s " % (k))

    for vertex,weight in v.items():
        G.add_edge(k,vertex , weight = weight)
        print("\t El vertice %s tiene una arista con %s con peso %s" % (k,vertex,weight))

nx.draw(G,with_labels= True)
plt.show()

def plot(self,j, parent=None):

    for k,v in j.items():

        if not parent: G.add_node(k)
        else: G.add_edge(parent,k)
        
        if isinstance(v,dict):
            for a,b in v.items():
                if isinstance(b,dict):
                    G.add_edge(k,a)
                    self.plot(b,a)
                else: G.add_edge(k,a)
    
    return True
        
        
            