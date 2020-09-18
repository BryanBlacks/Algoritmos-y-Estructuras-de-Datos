#-*- coding:utf8 -*-
"""
-------------------Nodo del Árbol Binario-------------------
* Nodo que almacenará el value (Precio) y el nombre del 
    nodo tipo Producto que proviene de la lista enlazada.
------------------------------------------------------------
"""
class Node:
    def __init__(self,value,name):
        self.value = value
        self.name = name
        self.left = None
        self.right = None