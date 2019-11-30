#-*- coding: utf8 -*-

"""
--------------------------------------Grafo exclusivo con TDA´s--------------------------------------

"""
class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, value):
        #Usar el search para que no hayan repetidos
        if not self.first:
            self.first = Node(value)
            return True
        else: 
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True
        return False
    
    def search(self,value):
        if not self.first:
            return False
        else:
            current = self.first
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Vertex:
    def __init__(self, name):
        self.name = name
        #El vertice puede estár conectado con infinitos vertices teniendo así una lista de aristas
        self.edge = LinkedList()

class Edge:
    def __init__(self,vertexName,weight):
        self.vertexName = vertexName
        self.weight = weight

class Graph:
    def __init__(self):
        self.graph = LinkedList()

    def add(self,vertexName):
        #El add de la lista enlazada tiene que no agregar valores duplicados (adentro del add usar el search)
        self.graph.add(Vertex(vertexName))

    def edge(self,vertexA,vertexB,weight):
        #Comprobar si el vertice A existe y si el vertice B no existe(aunque la lista no duplica asi que buah)
        if self.graph.search(vertexA):
        self.graph.search(vertexA).value.edges.add(Edge(vertexB,weight))

    def calculateWeight(self, bumbp, crossWalk, delayByTimeOfDay, delayByDayOfWeek)
        return bump+crossWalk+delayByTimeOfDay+delayByDayOfWeek

    def __str__(self):
        pass
        #Imprimir cada indice con su valor (nombre del vertice junto a sus aristas) 
        #Usar el imprimir de "grafos y arboles" enlistado abajo
"""
    def __str__(self):
        return self.innerPrint(self.json)

    def innerPrint(self,tree,tab=""):
        r = []
        for k,v in tree.items():
            if (k[-1] == "/"):
                r.append("%s%s"%(tab,k))
                r.append(self.innerPrint(v,"%s%s" % (tab,"\t")))
            else:
                r.append(("%s%s"%(tab,k)))
                #siempre usar la notación con corchete en el los value de los keys del JSON
                r.append(("%sSize: %s" % ("%s%s" % (tab,"\t"),self.mbt.convert(v["size"]))))
                r.append(("%sAuthor: %s" % ("%s%s" % (tab,"\t"),v["author"])))
                r.append(("%sDate: %s" % ("%s%s" % (tab,"\t"),v["date"])))
        return "\n".join(r)
"""