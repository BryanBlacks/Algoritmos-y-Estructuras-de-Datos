#-*- coding: utf-8 -*-
from Python.Stack import *

stack = Stack()

stack.push("Coca-Cola")
stack.push("Pepsi")
stack.push("Coca-Cola Sabores")
stack.push("Montain Dew")
print("Las cajas de fresco son: %s" %(stack.printS()))

print("%sLa caja que sale es: %s" %("\n",stack.pop()))
print("La caja que sale es: %s" %(stack.pop()))
print("La caja que sale es: %s" %(stack.pop()))
print("La caja que sale es: %s" %(stack.pop()))

print("%sLas cajas de fresco son: %s" %("\n",stack.printS()))