#-*- coding: utf-8 -*-

g,s = {
    "A":["B","C","B","B"],
    "B":["A","C"],
    "C":["A","B","D"],
    "D":["C"]
},{}

x = "C"

print("El grafo inicial: %s" % g )
print("-"*20)

#Imprime el camino para llegar a x
for k,v in g.items():
    if(x == k):
        for i in v:
            s[i] = None
    elif(x in v):
        s[k] = None

print("La solucion es: %s" % s.keys())