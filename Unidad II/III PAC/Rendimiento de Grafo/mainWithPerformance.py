import networkx as nx
import matplotlib.pyplot as plt
from PerformanceMed import *
from DinamicGraph import *
debug = False
G = nx.DiGraph()
metric = PerformanceMetric()
g,t = metric.runGraph(DynamicGraphGenerator())

print("La operación de generar el grafo ha tardado %.2f sgundos" % t)

for k,v in g.items():
    G.add_node("%s" % (k))
    if debug: print("Procesando el vertice %s " % (k))

    for vertex,weight in v.items():
        G.add_edge(k,vertex , weight = weight)
        if debug: print("\t El vertice %s tiene una arista con %s con peso %s" % (k,vertex,weight))

nx.draw(G,with_labels= True)
plt.show()