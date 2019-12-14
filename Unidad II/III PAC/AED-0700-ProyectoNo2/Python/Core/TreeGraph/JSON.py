# -*- coding:utf-8 -*-

class Json:
    def __init__(self,json):
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