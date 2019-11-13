from Sentence import *
from Random import *

class Paragraph:
    
    def __init__(self):
        self.sentence = Sentence()
        self.rand = Randomx()
    
    def create(self,max=15,min=10):

        paragragh = []
        num = self.rand.generator(max,min)

        for i in range(num):
            paragragh.append(self.sentence.create())

        return ". ".join(paragragh)