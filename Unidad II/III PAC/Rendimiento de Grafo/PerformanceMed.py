#-*- coding: utf8 -*-
from datetime import datetime

class ExecutionTime:
    def __init__(self):
        pass

    def now(self):
        return datetime.now()

    def diff(self, initTime, endTime):
        diff = endTime-initTime
        #Resultado en segundos
        t = diff.days*24*60*60
        t += diff.seconds
        t += diff.microseconds/1000/1000

        if (int(t*100) == 0):
            #Resultado en milisegundos
            t = t*1000
        else:
            #Resultado en microsegundos
            t = t*1000*1000


        print(initTime)
        print(endTime)
        return t

class PerformanceMetric:
    def __init__(self):
        self.et = ExecutionTime()

    def runGraph(self,generatedGraph):

        initTime = self.et.now()
        g = generatedGraph.create()
        endTime = self.et.now()

        return (g,self.et.diff(initTime,endTime))

        