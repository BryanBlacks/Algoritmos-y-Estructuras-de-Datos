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

    def greaterLength(self,str1, str2):
        greater = len(str1)
        if(len(str2) > greater): greater = len(str2)
        return greater  

    def lesserLength(self,str1, str2):
        lesser = len(str1)
        if(len(str2) < lesser): lesser = len(str2)
        return lesser
        
    def compare(self,obj1,obj2):
        if(isinstance(obj1,Node)):
            obj1 = (str(obj1.value)).strip()
        if(isinstance(obj2,Node)):
            obj2 = (str(obj2.value)).strip()

        if(isinstance(obj1,int)):
            obj1 = (str(obj1)).strip()
        if(isinstance(obj2,int)):
            obj2 = (str(obj2)).strip()

        obj1 = obj1.strip()
        obj2 = obj2.strip()
        
        lesser = self.lesserLength(obj1,obj2)

        for i in range(lesser):
            if self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i]):
                return 1
            elif self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i]):
                return -1
                
        if (lesser == self.greaterLength(obj1,obj2)):
            return 0   
        elif len(obj1) == lesser:
            return -1
        else:
            return 1

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.compare = Compare()

    #Agregar y ordenar los valores que se insertan
    def add(self,value):
        if not self.first:
            self.first = Node(value)
        else:
            current = self.first
            prev = None
            compare = Compare()
            
            while(current):
            #Si el valor del actual es menor al valor del que deseo agregar
                if (compare.compare(value, current.value) < 0):
                    if not current.next:
                    #Si no hay siguiente del actual y se debe de seguir avanzando,
                      #el nuevo nodo se agrega al final de la lista.
                        current.next = Node(value)
                        return True
                    else:
                        #Si tiene siguiente se sigue avanzando en la lista
                        prev = current
                        current = current.next

            #Si el valor del actual es el mismo al que deseo agregar, reemplazo el nodo
                elif (compare.compare(value, current.value) == 0):
                    if not prev:
                        #Si no tiene previo, esto indica que el nodo a reemplazar es el primero de la lista
                        self.first.next = current.next
                        self.first = Node(value)
                        return True
                    else:
                        #Si el atual no tiene siguiente no hay necesidad de enlazar un nulo al nuevo nodo, ya lo tiene
                        if not current.next:
                            prev.next = Node(value)
                            return True
                        
                        #Si no se reemplaza normalmente
                        else:
                            prev.next = Node(value)
                            prev.next.next = current.next
                            return True

                #Si el actual es mayor al que se desea agregar
                else:
                    #Si no tiene previo, el nuevo será el primero en la lista
                    if not prev: 
                        self.first = Node(value)
                        self.first.next = current
                        return True
                    else:
                        #current.next = current
                        #ARREGLAR AQUÍ
                        #prev = current.next
                        #current = Node(value)
                        #current.next = prev
                        prev.next = Node(value)
                        prev.next.next = current
                        return True
            return False
        
    def PrintLL(self):    
        current = self.first
        trail = " "
        while (current.next):
            trail += str(current.value) 
            trail += " --> "
            current = current.next

        trail += str(current.value)
        print(trail)

list = LinkedList()
list.add("Hola")
list.add("Hola            ")
list.add(2)
list.add("Adios")
list.add("Bye")
list.add(982)
list.PrintLL()