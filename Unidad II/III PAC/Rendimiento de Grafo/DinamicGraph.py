import random

class RandomGenerator:
    def __init__(self):
        pass
    def randomToInt(self, min = 1, max= 10):
        return int(random.random()*(max-min)+min)

class DynamicGraphGenerator:

    def __init__(self, debug = False):
        self.alphabet = "ABCDEFGHIJKLMNÑOPQRSTVWXYZ"
        self.r = RandomGenerator()
        self.debug = debug
    
    def create(self):
        g={}
        alphabetI = list(self.alphabet)
        vertexAmount = self.r.randomToInt(min = 0, max = len(self.alphabet))

        for i in range(vertexAmount):
            vertexA = alphabetI.pop(self.r.randomToInt(min = 0, max = len(alphabetI)))
            alphabetJ = list(self.alphabet)
            edgeAmount = self.r.randomToInt(min= 0, max = len(self.alphabet))

            g["%s"%vertexA] = {}

            if self.debug : print("Para el vertice %s, las aristas son: " % vertexA)

            for j in range(edgeAmount):
                vertexB = alphabetJ.pop(self.r.randomToInt(min = 0, max = len(alphabetJ)))
                if self.debug : print("\t %s" % vertexB)

                g["%s" % vertexA]["%s" % vertexB] = 1
        return g