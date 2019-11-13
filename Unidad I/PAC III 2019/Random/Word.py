from Random import*

class Word:

    def __init__(self):
        self.alphabet ="abcdefghijklmnñopqrstuvwxyz"
        self.rand = Randomx()
    
    def create(self,max=9,min=3):

        word = []
        tam = len(self.alphabet)
        num = self.rand.generator(max,min)

        for i in range(num):
            pos = self.rand.generator(tam)
            word.append(self.alphabet[pos])

        return "".join(word)