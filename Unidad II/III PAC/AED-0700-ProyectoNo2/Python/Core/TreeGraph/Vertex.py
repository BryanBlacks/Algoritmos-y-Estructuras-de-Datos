# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
Vertex (Vértice)
---------------------------------------------------------------------------------------------------------------------

* Esta clase se usará como modelo para almacenar los archivos y carpetas.
* Esta clase representarán cada uno de los directorios y archivos cuyo nombre será el identificador de los mismos.
* Si el tipo de elemento es un directroio, se podrán agregar mas carpetas y archivos dentro de sí, en la
  propiedad edges. 

---------------------------------------------------------------------------------------------------------------------
"""

from Core.TreeGraph.LinkedList import*

class Vertex:
    def __init__(self, name, nodeType):
        self.name = name
        self.nodeType = nodeType
        self.edges = LinkedList()
    
    def setEdges(self, vertexName):
        self.edges.addList(vertexName)

