import networkx as nx
import matplotlib.pyplot as plt
from DinamicGraph import *

G = nx.Graph()
#Quitar el comentario y comentar 8 y 9 para el anterior programa
#g = {"A":{"B":1,"C":1}}
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