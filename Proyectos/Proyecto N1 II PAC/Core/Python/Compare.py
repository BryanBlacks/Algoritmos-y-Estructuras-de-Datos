class Compare():

    alfabeth= "/.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self):
        pass


    def LesserLength(self,name1,name2):
        l = len(name1)
        if(len(name2) < l):
            l = len(name2)

        return l

    def GreaterLength(self,name1,name2):
        g = len(name1)
        if(len(name2) > g):
            g = len(name2)

        return g


    def compare_(self,name1,name2):
        if(len(name1) > len(name2)):
            return None
        else:
            if(len(name2) > len(name1)):
                return None
        for i in range(self.LesserLength(name1,name2)):
            if(name1[i] == name2[i]):
                pass
            else:
                return None
        return name1





    
    

