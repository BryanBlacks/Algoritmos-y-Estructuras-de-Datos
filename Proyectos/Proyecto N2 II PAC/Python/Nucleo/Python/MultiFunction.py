#-*- coding: utf-8 -*-
from os import scandir
from Nucleo.Python.GraphTDA import *
import networkx as nx
import matplotlib.pyplot as plt
import math

class TxtFile:
    def lines(self, path1):
        return [obj.name for obj in scandir(path1) if obj.is_file()]

class Arista:
    def __init__(self):
        self.grafo=None
        self.anex = None
        self.arrayRutes = []
        self.arrayWeight = []

    #Función que crea el grafo tipo TDA con los datos del TextEdit
    def process(self, value):

        graph = GraphInner()
        array,t= [],[]
        q= len(value)-1
        
        #Inicio de contador que se usará para convertir a entero las primeras cuatro caracteristicas
        count=0
        for i in range(q):
            
            #Dependiendo el tabulado se sabrá si es vertice, arista o caracteristica
            if(value[i].count("\t") == 0):
                currentVertex = value[i]

                #Se agraga al grafo tipo TDA como vertice por poseer 0 Tab en su cadena
                graph.add_vertex(currentVertex)

            else:
                if (value[i].count("\t") == 1):
                    #Se elimina el tabulado de la cadena quedando el nombre real de la arista
                    currentEdge = value[i].lstrip("\t")

                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    graph.add_edge(currentVertex, currentEdge)

                    #Reinicio de contador por si las caracteristicas son de una nueva arista
                    count=0
                
                else:
                    char=""

                    #Contador aumenta hasta llegar a la ultima caracteristica tipo entero
                    count=count+1
                    if(value[i].count("\t") == 2):
                    
                        currentChar = value[i].lstrip("\t")
                        large = len(currentChar)

                        #Solo obtener los datos que están después de los dos puntos
                        data = 1+currentChar.index(':')
                        
                        for k in range(data,large):
                            char = "%s%s"%(char,currentChar[k])
                        if(count <= 4):
                            #Cuando llegue a la quinta caracteristica no lo convertira a entero
                            char=int(char)
                            #La quinta caracteristica es el tipo de medio que es un string
                        
                        #Se agrega las caracteristicas de esa arista con su vertice respectivo
                        graph.add_caract(currentVertex,currentEdge,char)

        #El grafo es ingresado como lista para ser convertido a Diccionario/JSON
        self.anex = graph.vertex             
        self.grafo = graph.convertJson()

    #Funcion recursiva para la busqueda de rutas
    def findPaths(self, vertex, destination, json = None ,  path = [], visited = []):
        if(not json):
            json = self.grafo
        
        path.append(vertex)
        visited.append(vertex)

        if (vertex != destination):
            for edge in json[vertex]:
                if(not edge in visited):
                    self.findPaths( edge, destination,json, path, visited)

        else:
            rute = len(path)
            row =""  
            for i in range(rute):

                #Se transforma de numero a caracter para que el arreglo con los caminos no se borre dinamicamente
                row = "%s%s "%(row,chr(ord(path[i])))
                #El arreglo Path con el metodo .pop() elimina elemoentos dinamicamente

            row = row.split(" ")
            while "" in row:

                #Se eliminan los espacios del arreglo de arreglos que contiendra las rutas 
                row.remove("")

            #Arreglo con rutas en arreglos
            self.arrayRutes.append(row)
                    
        path.pop()
        visited.pop()

    #Funcion para determinar el peso de cada arista de manera individual
    def findWeight(self, vertex, destination, json = None, weight = [], visited = []):
        if(not json):
            json = self.grafo
            weight.append("first")
        
        visited.append(vertex)
        

        if (vertex == destination):
            rute = len(weight)
            row =""  
            for i in range(rute): 
                row = "%s%s "%(row,weight[i])
                
            row = row.split(" ")
            while "" in row:
                row.remove("")
            while "first" in row:
                #Eliminar el elemento first del arreglo, utilizado como pegamento
                row.remove("first")
            for z in range(len(row)):
                #Convertir a flotante el numero entregado
                row[z]= float(row[z])

            self.arrayWeight.append(row)


        else:
            for edge in json[vertex]:
                #Busca el vertex en el grafo
                current = self.search1(vertex)
                if(not edge in visited):
                    peso = self.searchEdge2(current.name,edge)
                    a= peso.carac
                    #Uso del metodo que calcula el peso en mbps de la arista
                    b= self.mbpsWeight(a[0],a[1],a[2],a[3],a[4])
                    #Agrega al arreglo los pesos de las aristas
                    weight.append(b) 
                    self.findWeight(edge, destination, json,  weight, visited)

        #while "" in weight:
            #weight.remove("")
                   
        weight.pop()
        visited.pop()

        
    #Funcion para la busqueda de vertices dentro del grafo TDA
    def search1(self, value):
        current = self.anex.first
        while(current):
            if current.value.name == value:
                return current.value
            current = current.next
        return False
    
    #Funcion para la busqueda de aristas en el grafo TDA
    def searchEdge2(self, o, d):
        current = self.search1(o)
        while(current):
            if(current):
                anex = current.edges.first
                while(anex):
                    if (anex.value.name == d):
                        return anex.value
                    anex= anex.next

            current = current.next

    #Funcion que calcula la confiabilidad que da cada tipo de conexión
    def confidence(self, distance, typeConect):
        
        confidence = 0.00

        if(typeConect == "CAT5"):
            if (distance >= 50): 
                quantity = math.floor(distance/50)
                confidence = 0.0002*quantity
                return float(0.98-confidence)
            else:
                confidence = 0.98
                return confidence

        else:
            if(typeConect == "CAT6"):
                if (distance >= 50):
                    quantity = math.floor(distance/50)
                    confidence = 0.0001*quantity
                    return float(0.98-confidence)
                else:
                    confidence = 0.98
                    return confidence 

            else:
                if(typeConect == "Fibra"):
                    if (distance >= 100):
                        quantity = math.floor(distance/100)
                        confidence = 0.0005*quantity
                        return float(0.90-confidence)
                    else: 
                        confidence = 0.90
                        return confidence

                else:
                    if(typeConect == "WIFI"):
                        if (distance >= 6):
                            quantity = math.floor(distance/6)
                            confidence = 0.006*quantity
                            return float(0.7-confidence) 
                        else:
                            confidence = 0.70
                            return confidence

                    else:
                        if(typeConect == "Coaxial"):
                            if (distance >= 100):
                                quantity = math.floor(distance/100)
                                confidence = 0.0004*quantity
                                return float(1-confidence)
                            else:
                                confidence = 1.00
                                return confidence 

                        else:
                            if(typeConect == "Par-Trenzado"):
                                if(distance >= 100):
                                    quantity = math.floor(distance/100)
                                    confidence = 0.0001*quantity
                                    return float(1-confidence)

                                else:
                                    confidence = 1.00
                                    return confidence
    #Peso bruto en mbps
    def mbpsWeight(self, d, b, u, t, m):
        return float('%.2f' % ((t*u)/(b - self.confidence(d,m)))) 

    #Función que usa el grafo tipo JSON con matplotlib para la figura y networkx para el dibujado del mapa
    def toMap(self, graph=None):
        #Grafo direccionado
        G = nx.DiGraph()

        #variable que contendra la imagen
        image = plt.figure()
        if not graph:
            graph = self.grafo
        for vertice, aristas in graph.items():
            G.add_node("%s" % vertice)
            for arista in aristas:
                G.add_node("%s" % arista)
                G.add_edge("%s" % vertice, "%s" % arista, weight=1)
                #print("'%s' se conecta con '%s'" % (vertice, arista))

        pos = nx.circular_layout(G)
        
        #lista de nodos del grafo
        nlist = [node for node in G.nodes()]

        #lista de aristas del grafo
        elist = [edge for edge in G.edges()]

        nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = nlist, node_size= 4000)
        nx.draw_networkx_labels(G,pos)
        #nx.draw_networkx_edge_labels(G,pos)
        nx.draw_networkx_edges(G, pos,edgelist=elist,width=4, arrowstyle='-|>',arrowsize=50, node_size= 4000 )

        #Guardado de la imagen/Mapa de los nodos y aristas edge_labels={('A','B'):'8',('B','C'):'12',('C','D'):'7',('E','D'):'15',('B','D'):'9'}
        image.savefig('/home/benedetto/Documentos/Proyecto #2/Python/Map/map.png')

    #Funcion para ordenar las rutas de manera ascendente
    def orderRutes(self, rutes = None, weights = None):
        if(not rutes and not weights):
            #Usando el arreglo de rutas y el arreglo de pesos para dinamicamente ordenar ambos a la vez
            rutes = self.arrayRutes
            weights = self.arrayWeight
            array=[]
        #Variable total que tendra la suma de los pesos de todas las aristas
        total=0.00
        for i in weights:
            for j in range(len(i)):
                total= total + i[j]
            array.append(float('%.2f' % (total)))
            total=0.00
        
        #Uso del ordenamiento Burbuja para ambos arreglos
        self.bubleOrder(array,len(array),rutes)

        #Arreglos actualizados, ordenados de manera ascendete
        self.arrayWeight = array
        self.arrayRutes = rutes

    #Famoso algoritmo Ordenamiento Burbuja
    def bubleOrder(self,list1,tam,list2):
        for i in range(1,tam):
            for j in range(0,tam-i):
                if(list1[j] > list1[j+1]):
                    k = list1[j+1]
                    list1[j+1] = list1[j]
                    list1[j] = k

                    t = list2[j+1]
                    list2[j+1] = list2[j]
                    list2[j] = t
    #Funcion que crea la tabla con caracteres ASCII que se embeberá en la pantalla que se despliega al apretar boton crear tabala
    def toTable(self, node1,node2):
        string=""
        array = self.arrayRutes
        array1 = [ ",".join(array[d]) for d in range(len(array))]
        weight = self.arrayWeight
        origin = node1
        destiny = node2

        for i in range(90):
            string = string + "%s" % chr(45)

        string = string + "\n\n                                       %s%s%s%s%s %s%s %s%s%s%s%s %s%s %s %s %s\n\n" % (chr(84),chr(65),chr(66),chr(76),chr(65), chr(68),chr(69),
                            chr(82),chr(85),chr(84),chr(65),chr(83), chr(68),chr(69), origin, chr(65), destiny)
        for i in range(90):
            string = string + "%s" % chr(45)

        string = string + "\n\n                                             %s%s%s%s       %s      %s%s%s%s%s \n\n" % (chr(80),chr(69),chr(83),chr(79),chr(124),chr(82),chr(85),
                            chr(84),chr(65),chr(83))

        for i in range(90):
            string = string + "%s" % chr(45)

        for m in range(len(array)):
            string = string + "\n\n                                                %s       %s      %s     \n\n" % (weight[m],chr(124),array1[m])
            for i in range(90):
                string = string + "%s" % chr(45)
        
        return string






        


            
