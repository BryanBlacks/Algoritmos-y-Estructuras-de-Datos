#-*- coding:utf8 -*-
"""
------------------------------------Grafo de Diccionario------------------------------------
* Planteamiento básico de un grafo haciendo uso de Dict en Python
* Las aristas se representan como un arreglo
* Procedimiento de recorrido de grafo para encontrar incognita X
* El peso es un valor muerto que representa un salto sino se define(De C a D es un salto)
"""

graph = {
    "A":["C"],
    "B":["A","C"],
    "C":["D"],
    "D":[]
}

X = "C"

#Search en el grafo al ser dirigido solo se compará el valor de v
#Si se guarda en un arreglo pueden haber elementos duplicados
json = {}
for k,v in graph.items():
    if X in v:
        #Se pone none porque los valores en un json no se pueden repetir
        json[("%s" %k).strip()] = None
json = list(json.keys())
print("Para el grafo dirigido %s, los nodos que se conectan con %s son: %s" % (graph,X,json))


#Caso cuando es un Grafo no dirigido 
graph = {
    "A":["B","C"],
    "B":["A","C"],
    "C":["A","B","D"],
    "D":["C"]
}

r = {}
for k,v in graph.items():
    if X == k:
        for i in v:
            r[("%s" % i).strip()] = None
    elif X in v:
        r[("%s" %k).strip()] = None
r = list(r.keys())
print("Para el grafo no dirigido %s, los nodos que se conectan con %s son: %s" % (graph,X,r))

from DirectedGraph import *
g = Graph(graph)
print("\n\n")
print("Para el grafo no dirigido %s, los nodos que se conectan con %s son: %s" % (graph,X,g.conectWith(X)))
