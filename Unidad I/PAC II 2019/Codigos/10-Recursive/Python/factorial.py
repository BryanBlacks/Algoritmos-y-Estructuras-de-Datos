#-*-coding: utf-8 -*-

class OtherAlgorithm:
    def __init__(self):
        pass
    
    def factorialAsc(self,n):
        result = 1
        for i in range(1,n+1):
            print ("i=%s" %i)
            result = result*i
        return result
    
    def factorialDes(self,n):
        result = 1
        for i in range(n,0,-1):
            result = result*i
        return result

oa = OtherAlgorithm()
n = int(input("Valor a sacar factorial: "))


print ("El factorial (Ascendente) de %s es %s" %(n,oa.factorialAsc(n)))
print ("El factorial (Descendente de %s es %s" %(n,oa.factorialDes(n)))