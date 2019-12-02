#-*- coding:utf8 -*-
"""
---------------------------JSON / DICT---------------------------
* JSON ---> JavaScript Object Notation
* Dict ---> Es el equivalente en Python de JSON en JS
* En json los indices son dinamicos dict = {indice:valor}
-----------------------------------------------------------------
"""
from Queue import *

cadena = "valor"
arreglo = ["valor","valor","valor"]
dict = {"indice":"valor"}

class LinkedList:
    pass
class Node:
    def __init__(self, value):
        self.value = value
        self.children = LinkedList()

#Con TDA
node = Node("Value")
print(node.value)

#Con JSON / Dict
#Se ignoran los dupolicados y se asigna el nuevo valor al indice duplicado
node = {"value":None,"value":1}
#Se hace referencia al indice
print(node["value"])
node["value"]=2
print(node)
node["value1"]=2
print(node)

"""
------------------------------------JSON / DICT-------------------------------------
* Con Dict se tiene control del algoritmo completo.
* Dict ofrece caracteristicas implicitas que se pueden aprovechar en la 
    construcción de algoritmos.
* Se crean indices en posiciónes que suelen no existir, cosa que no pasa en un array
* Las keys son los indices .keys() solo devuelven solo los indices
    Etiquetal, Llave, Indice, Atributo son sinonimos de Keys
* Con items o values devuelven el valor de los indices
* Se puede hacer JSON/Dict de cualquier objeto ya que es un objeto en si
------------------------------------------------------------------------------------
"""

import random
def randomZeroOrOne():
    return int(random.random()*(101-1)+1)
array = [randomZeroOrOne() for i in range(1000)]
print(array)

#Algoritmo de diccionario que genere arreglo sin valores duplicados
cleanArray = {}
for i in array:
    #Tarea: Como contar cuantos unos y ceros hay? 
    #   (con if dentro del for el primer valor en cero y empezar a contar)
    cleanArray["%s" % i] = None 

print(cleanArray)
print(list(cleanArray.keys()))

dict = {"value": 0, "value1": 1.0, "value2": "Cadena", "value3":[1,2,3,4],"value4":{"esto es un JSON??":True}}

#Solución generica para recorrer el dict (arreglo de elementos con diferentes indices)
for i in dict:
    #No confiar en como ordena JSON los elementos ingresados
    print(i)
    #print("%s:%s"%(i,dict[i]))

#Siguientes for son lo mismo
for i in dict.items():
    index = i[0]
    value = i[1]
    print("%s:%s"%(index,value))

for index,value in dict.items():
    print("%s:%s" % (index,value))

"""
-------------------------------------OverWrite-------------------------------------
* Herencia que se puede hacer en python
* Los metodos que no tenga Queue igual se heredarán de LinkedList por herencia
"""
class Queue(LinkedList):
    pass

q = Queue()
q.add("2")
q.add("4")
q.add("6")
q.add("8")
print(q.printLL())
print(q)