from Word import *
from Random import *

class Sentence:

    def __init__(self):
        self.rand = Randomx()
        self.word = Word()

    def create(self,max=9,min=5):

        sentence = []
        num = self.rand.generator(max,min)

        for i in range(num):
            sentence.append(self.word.create())
        
        return " ".join(sentence)