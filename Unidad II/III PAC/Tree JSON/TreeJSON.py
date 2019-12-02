#-*- coding:utf8 -*-

"""
Arbol de n nodos con JSON
(3*1024*1024) kilobytes
(3*1024) megabytes

"""

"""
En TDA lo equivalentes es esto
tree = Tree()
tree.add(File(...))
tree.add(Folder(...))
tree.add(File(...), tree.search(...))
tree.add(Folder(...), tree.search(...))
"""

tree = {
    "root/":{
        "main.py":{
            "size":7841,
            "author":"AED",
            "date":"2019-10-25 07:28"
        },
        "carpeta/":{
            "music.mp3":{
                "size":4096,
                "author":"AED",
                "date":"2019-11-25 07:28"
            },
            "carpeta/":{
                "document.pdf":{
                    "size":(3*1024*1024),
                    "author":"AED",
                    "date":"2019-11-25 07:28"
                }
            }
        }
    }
}

#Recorrer el árbol 
def treePrint(tree,tab=""):
    for k,v in tree.items():
        #if k[len(k)-1] == "/":
        #if ("/" in k):
        #if (k.index("/")>-1):
        #Se puede usar el negativo de una cadena y devuelve el ultimo caracter
        if (k[-1] == "/"):
            print("%s%s"%(tab,k))
            treePrint(v,"%s%s" % (tab,"\t"))
        else:
            print("%s%s"%(tab,k))
            #siempre usar la notación con corchete en el los value de los keys del JSON
            print("%sSize: %s" % ("%s%s" % (tab,"\t"),v["size"]))
            print("%sAuthor: %s" % ("%s%s" % (tab,"\t"),v["author"]))
            print("%sDate: %s" % ("%s%s" % (tab,"\t"),v["date"]))


treePrint(tree)