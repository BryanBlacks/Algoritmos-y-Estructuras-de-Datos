# -*- coding:utf8 -*-

class Compare:
    def __init__(self):
        self.alphabet = "zyxwvutsrqpoñnmlkjihgfedcbaZYXWVUTSRQPOÑNMLKJIHGFEDCBA9876543210 !#$%&/()=?¡'¿[]-:;,.+*´_"

    def greaterLength(self, str1, str2):
        greater = len(str1)
        if(len(str2) > greater): greater = len(str2)
        return greater  

    def lesserLength(self, str1, str2):
        lesser = len(str1)
        if(len(str2) < lesser): lesser = len(str2)
        return lesser
        
    #Define cua de las cadenas va primero por jerarquia alfabetica
    def order(self,obj1,obj2):

        obj1 = obj1.strip()
        obj2 = obj2.strip()
        
        lesser = self.lesserLength(obj1,obj2)

        for i in range(lesser):
            if self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i]):
                return 1
            elif self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i]):
                return -1
                
        if (lesser == self.greaterLength(obj1, obj2)):
            return 0   
        elif len(obj1) == lesser:
            return -1
        else:
            return 1
    
    # Compara si la cadena es igual, si lo es se retorna cualquiera de las cadenas ya que serian iguales
    def compare(self,name1,name2):
        
        if(len(name1) > len(name2)):
            return None
        else:
            if(len(name2) > len(name1)):
                return None
        for i in range(self.lesserLength(name1,name2)):
            if(name1[i] == name2[i]):
                pass
            else:
                return None
        return name1