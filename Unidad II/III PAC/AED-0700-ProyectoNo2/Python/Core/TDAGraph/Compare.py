class Compare:
    def __init__(self):
        self.alphabet = " !#$%&/()=?¡'¿[]-:;,.+*´_0123456789abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ"

    def greaterLength(self,str1, str2):
        greater = len(str1)
        if(len(str2) > greater): greater = len(str2)
        return greater  

    def lesserLength(self,str1, str2):
        lesser = len(str1)
        if(len(str2) < lesser): lesser = len(str2)
        return lesser
        
    def compare(self,obj1,obj2):
        if(isinstance(obj1,Node)):
            obj1 = (str(obj1.value)).strip()
        if(isinstance(obj1,int)):
            obj1 = (str(obj1)).strip()
        
        if(isinstance(obj2,Node)):
            obj2 = (str(obj2.value)).strip()
        if(isinstance(obj2,int)):
            obj2 = (str(obj2)).strip()

        obj1 = obj1.strip()
        obj2 = obj2.strip()
        
        lesser = self.lesserLength(obj1,obj2)

        for i in range(lesser):
            if self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i]):
                return 1
            elif self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i]):
                return -1
                
        if (lesser == self.greaterLength(obj1,obj2)):
            return 0   
        elif len(obj1) == lesser:
            return -1
        else:
            return 1