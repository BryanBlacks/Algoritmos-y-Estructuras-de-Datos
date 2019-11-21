#-*- coding:utf8 -*-
"""
----------------------------Balanceo-----------------------------
*Simbolos --> Numeros --> Letras Minusculas --> Letras Mayusculas

Se hace un metodo que compare el current.value
    Si es -1 el parametro 1 es menor que el parametro 2
    Si es 0 parametro 1 y parametro 2 son iguales
    Si es 1 el parametro 1 es mayor que parametro 2

"""

class Compare:
    def __init__(self):
        self.alphabet = " !#$%&/()=?¡'¿[]-:;,.+*´_0123456789abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ"

    def compare(self,obj1,obj2):
        if(isinstance(obj1,object)):
            obj1 = str(obj1.value)
        if(isinstance(obj2,object)):
            obj2 = str(obj2.value)

        if(isinstance(obj1,int)):
            obj1 = str(obj1)
        if(isinstance(obj2,int)):
            obj2 = str(obj2)
        
        #lstrip para quitar los espacios de ambos lados
        
        max = len(obj1)
        min = len(obj1)
        if(min > len(obj2)):
            min=len(obj2)
        if(max < len(obj2)):
            max=len(obj2)

        if obj1 == obj2:
            return 0

        for i in range(min):
            if self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i]):
                return 1
            elif self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i]):
                return -1
                
        if (len(obj1)>len(obj2)):
            return 1   
        else:
            return -1

class LinkedList:
    def __init__(self):
        self.first = None
        self.compare = Compare()

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
                elif (self.compare.compare(current,value) == 0):
                    pass
                elif (self.compare.compare(current,value)<0):
                    #value va despues
                    current = current.next
                else:
                    #value va antes
                    stack = self.first
                    self.first = Node(value)
                    self.first.next = stack  
