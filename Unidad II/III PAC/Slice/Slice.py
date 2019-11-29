#-*- coding:utf8 -*-
"""
-----------------------------SLICE---------------------------------------
*Para hacer uso de argument values se llama a sys.argv
*sys.argv es un arreglo y considera como parametros, todos los parametros 
    que recibe de python
*Es un arreglo de cadenas es decir se pierde el tipo de dato que se manda 
    y se combierte en cadena
*Se llama Slice [0:] Un arreglo de un arreglo
*Se puede usar [1:2] para indicar inicio y final del sub arreglo 
*Dato: Los parametros son  antes de que se ejecute el programa pero 
    los imput son cuando se esta ejecutando
"""
import sys 
print("\n")
print("-"*20)
print(sys.argv[1:])
print("-"*20)
print("\n")