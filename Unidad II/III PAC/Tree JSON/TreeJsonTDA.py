#-*- coding:utf8 -*-

"""
Combinar los conceptos de TDA y JSON

Construir un árbol usando un TDA que controla un JSON como base del programa 
"""
import random
class RandomGenerator:
    def __init__(self):
        pass
    def random2Int(self, max= 101, min = 0):
        return int(random.random()*(max - min) + min)

class MegaByteTransformer:
    def __init__(self):
        pass
    def convert(self,value):
        value = int(value)
        if value<= 1024:
            return ("%.2f Byters " % (value))
        if value<= 1024*1024:
            return ("%.2f KB " % (value/1024))
        if value<= 1024*1024*1024:
            return ("%.2f MB " % (value/1024/1024))
        if value<= 1024*1024*1024*1024:
            return ("%.2f GB " % (value/1024/1024/1024))
        else:
            return ("%.2f TB " % (value/1024/1024/1024/1024))
class Tree:
    def __init__(self):
        self.mbt = MegaByteTransformer()
        self.rand = RandomGenerator()
        self.json = {"root/":{}}

    def add(self,value, current = "root/"):
        #Current existe y en current queremos crear un nuevo indice que se va a llamar value
        self.json["%s" % current]["%s" % value] = {"size":self.rand.random2Int(1024*1024*1024*1024),"author":"","date":"2019-25-11 08:18"}
 
    def __str__(self):
        return self.innerPrint(self.json)

    def innerPrint(self,tree,tab=""):
        r = []
        for k,v in tree.items():
            if (k[-1] == "/"):
                r.append("%s%s"%(tab,k))
                r.append(self.innerPrint(v,"%s%s" % (tab,"\t")))
            else:
                r.append(("%s%s"%(tab,k)))
                #siempre usar la notación con corchete en el los value de los keys del JSON
                r.append(("%sSize: %s" % ("%s%s" % (tab,"\t"),self.mbt.convert(v["size"]))))
                r.append(("%sAuthor: %s" % ("%s%s" % (tab,"\t"),v["author"])))
                r.append(("%sDate: %s" % ("%s%s" % (tab,"\t"),v["date"])))
        return "\n".join(r)

tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
print(tree)