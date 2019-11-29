#-*- coding:utf8 -*-
file,string,array = open("Node.py","r"),"Hola Mundo",["Esto","es","un","ejemplo"]
for i in file: print(i)
for i in string: print(i)
for i in array: print(i)

#Codificación de una línea
array = [1,2,3,4,5,6,7,8,9]
print(2 in array)

#Ciclo en una sola línea
array = [i for i in range(10)]
print(2 in array)

import random
r = int(random.random()*(100)) #Numero random entero de 0 a 100
#Cada vez que se llame a r devolvera un numero aleatorio
def r(n=0) :return int(random.random()*(100)) 
matrix = [[r() for j in range(100)] for i in range(100)]
print(matrix)
"""
------------------------------Función Map--------------------------------------
    *Producir un iterable donde el map tendra una funcion donde esa funcion
        operara cada elemento de ese iterable

    *Todo elemento del segundo parametro sera utilizado por la función del 
        primer parametro

    *La funcion no se pone con los parentesis ejemplo() NO , ejemplo YES
    
    *Cualquier cosa que se pueda recorrer es un iterable
    *Cuando hay un * significa que es dinamico (como la función map)
""" 

def increment(n): return n+1
#Esto retorna un objeto
result1 = map(r,[1,2,3]) 
result2 = map(increment,[1,2,3]) 
#Casteo a lista (donde solo se puede si es cadena)
for i in result1: print(i)
for j in result2: print(j)

"""
------------------------------Operador Lambda-----------------------------------
    *Crea una función momentanea que usa los iterables del map
""" 

result = map(lambda a: a+1,[1,2,3])
for i in result: print(i)

result = map(lambda a,b: a+b,[1,2,3],[2,3,4])
for i in result: print(i)

#Numeros Impares en una línea
print([i for i in range(10) if i%2==1])
#Numeros Pares en una línea
print([i for i in range(10) if i%2==0])