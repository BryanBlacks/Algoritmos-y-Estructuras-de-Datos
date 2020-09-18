# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
JSON (JavaScript Object Notation)
---------------------------------------------------------------------------------------------------------------------

* Método "add"
    Este método llama a una función interna llamada "addInner".

* Método "addInner"
    Este método agregara a la estructura JSON los identificadores de las carpetas y usaurios que el
    usuario cree edurante la ejecución del programa.

---------------------------------------------------------------------------------------------------------------------
"""

class Json:
    def __init__(self, json):
        self.json = json

    def add(self, value, nodeType, dest = None):
        self.addInner(self.json, value, nodeType, dest)

    def addInner(self, json, value, nodeType, destiny):
        if (not destiny):
            if (nodeType == "D"):
                self.json["%s" % value] = {}  
            else:
                self.json["%s" % value] = nodeType  
        else:
            for k, v in json.items():
                if (json is self.json):
                    if (k is ("%s" % destiny)):
                        if (nodeType == "D"):
                            self.json[k]["%s" % value] = {}

                            return True
                        else:
                            self.json[k]["%s" % value] = nodeType

                            return True
                    elif (isinstance(v, dict)):
                        if self.addInner(v, value, nodeType, destiny):
                            return True
                else: 
                    if (k is "%s" % destiny):
                        if (nodeType == "D"):
                            json[k]["%s" % value] = {}

                            return True
                        else:
                            json[k]["%s" % value] = nodeType

                            return True
                    elif (isinstance(v, dict)):
                        if (self.addInner(v, value, nodeType, destiny)):
                            return True
