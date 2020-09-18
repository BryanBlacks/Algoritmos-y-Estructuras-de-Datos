#-*- coding:utf8 -*-
from datetime import datetime
import random

class TestPerformance:
    def __init__(self):
        self.execution = ExecutionTime()


    def test(self, function):
        #Instancia del algoritmo
        #Instancia de la clase que maneje el tiempo y el arreglo

        initTime = self.execution.getTime()
        r = function()
        finalTime = self.execution.getTime()

        #Tupla
        return (r , self.execution.diff(initTime, finalTime))

class ExecutionTime:
    def __init__(self):
        pass

    def getTime(self):
        return datetime.now()

    def diff(self, i , f):
        #En milisegundos
        r = ( f - i )
        milliseconds = r.days*24*60*60*1000
        milliseconds += r.seconds*1000
        milliseconds += r.microseconds/1000

        return milliseconds

class ArrayGenerator:
    def __init__(self):
        pass

    def generate(self, n = 1000):
        array = [int(random.random()*100) for i in range(n)]
        #Duplicado de un arreglo
        return array[:]
