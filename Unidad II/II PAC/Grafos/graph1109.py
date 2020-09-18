#-*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

grafo = {"a":["b","c","d","e"]}

graph = {
    "A":["B", "C", "E"],
    "B":["A","C", "D"],
    "C":["A", "B", "E"],
    "D":["B"],
    "E":["A", "C"]
}

for vertice, aristas in graph.items():
    G.add_node("%s" % vertice)

    for arista in aristas:
        G.add_node("%s" % arista)
        G.add_edge("%s" % vertice, "%s" % arista, weight=1)
        print("'%s' se conecta con '%s'" % (vertice, arista)) 
    
nx.draw(G, with_labels = True)
plt.show()