#-*- coding:utf8 -*-
"""
----------------------------Balanceo-----------------------------
*Simbolos --> Numeros --> Letras Minusculas --> Letras Mayusculas

Se hace un metodo que compare el current.value
    Si es -1 el parametro 1 es menor que el parametro 2
    Si es 0 parametro 1 y parametro 2 son iguales
    Si es 1 el parametro 1 es mayor que parametro 2

"""

class LinkedList:
    def __init__(self):
        self.first = None

    #Agregar y ordenar los valores que se insertan
    def add(self,value):
        if not self.first:
            self.first = Node(value)
        else:
            while(current):
                current = self.first
                if current.value = value:
                    #Se debe saber la lógica del sistema,es decir,sí se reemplazan
                    #los nodos con el mismo nombre o no
                    pass
                elif (self.compare(current,value) == 0):
                    pass
                elif (self.compare(current,value)<0):
                    #value va despues
                    current = current.next
                else:
                    #value va antes
                    stack = self.first
                    self.first = Node(value)
                    self.first.next = stack
                
