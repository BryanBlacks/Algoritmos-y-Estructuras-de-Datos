import random

class Randomx:

    def __init__(self):
        pass

    def generator(self,max=100,min=0):
        
        r = random.random()

        return int(r*(max-min)+min)