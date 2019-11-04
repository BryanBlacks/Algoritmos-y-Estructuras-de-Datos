from tree import*
from io import*

def printSearchFunction(nodeWasFound):
    if (nodeWasFound):
        print (nodeWasFound.value.name)
    
    else:
   
        print (False)
        
prueba = Tree()
prueba.fromPlainText()
print(prueba)
"""
p = '\tCarpeta1\n'
p.replace('\t', '')
p.replace('\n', '')
print(p)

prueba.add("Carpeta1", "D")
prueba.add("Carpeta2", "D")
prueba.add("Carpeta3", "D")
prueba.add("Carpetaa", "D", "Carpeta1")
prueba.add("CarpetaNueva", "D", "Carpeta1")
prueba.add("CarpetaSS", "D", "Carpeta1")
prueba.add("Carpetaaa", "D", "Carpeta2")
prueba.add("Carpetasa", "D", "Carpetaaa")
prueba.add("Archivo1", "F", "Carpeta1")
prueba.add("Carpetosa", "D", "Carpetasa")
prueba.add("Archivo3", "F", "CarpetaSS")
prueba.add("Archivo4", "F", "Carpetosa")

prueba.add("Carpeta1","D")
prueba.add("Carpeta2","D")
prueba.add("Nodo3","F")
prueba.add("hola","F","Carpeta2")
prueba.add("El Ultimo", "D", "Carpeta1")
prueba.add("El Final", "D", "El Ultimo")
prueba.add("Tu mama","D","El Final")
prueba.add("Hijo2","F","Carpeta2")
prueba.add("El Final", "F", "Carpeta1")
prueba.add("Archivo", "F", "El Ultimo")
prueba.add("El Final", "F", "El Ultimo")



foundNode0 = prueba.search("Carpeta3")
foundNode1 = prueba.search("Carpetaaa")
foundNode2 = prueba.search("Archivo3")

printSearchFunction(foundNode0)
printSearchFunction(foundNode1)
printSearchFunction(foundNode2)
current=prueba.search("hola")
#print(current.value.name)

f = open("PRUEBA.txt","r+")
lines = f.readlines()
for i in range(len(lines)):
    print(lines[i])
f.close()

f=open("PRUEBA.txt","w")
f.write(prueba.save())
f.close() 
"""

