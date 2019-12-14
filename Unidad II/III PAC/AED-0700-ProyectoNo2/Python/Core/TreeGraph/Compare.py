# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
Compare (Comparar)
---------------------------------------------------------------------------------------------------------------------

* Método "greaterLength"
    Este método retorna el tamaño de la cadena más grande.

* Método "lesserLength"
    Este método retorna el tamaño de la cadena más pequeña.

* Método "order"
    Este método define cual de las cadenas irá primero por jerarquía alfabética, limpiando las cadenas primero, 
    luego obteniendo el tamaño de las mismas, para después recorrer cada uno de los indices de la primera y
    compararlos con los de la segunda cadena, retornando asi, segun la nomenclatura aprendida en clase, el
    indicador 1 si va después, -1 si va antes y finalmente 0 si son iguales.

*Método "compare"
    

---------------------------------------------------------------------------------------------------------------------
"""

class Compare:
    def __init__(self):
        #Jerarquía alfabética a implementar.
        self.alphabet = "zyxwvutsrqpoñnmlkjihgfedcbaZYXWVUTSRQPOÑNMLKJIHGFEDCBA9876543210 !#$%&/()=?¡'¿[]-:;,.+*´_"

    def greaterLength(self, str1, str2):
        greater = len(str1)

        if (len(str2) > greater): greater = len(str2)

        return greater  

    def lesserLength(self, str1, str2):
        lesser = len(str1)
        
        if (len(str2) < lesser): lesser = len(str2)

        return lesser
        
    def order(self,obj1,obj2):
        #Limpia las cadenas.
        obj1 = obj1.strip()
        obj2 = obj2.strip()
        
        lesser = self.lesserLength(obj1, obj2)

        for i in range(lesser):
            if (self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i])):
                return 1
            elif (self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i])):
                return -1
        
        #0 si las cadenas son iguales, 1 si la primera es mayor y -1 si esta es menor que la segunda.
        if (lesser == self.greaterLength(obj1, obj2)):
            return 0   
        elif (len(obj1) == lesser):
            return -1
        else:
            return 1
    
    def compare(self, name1, name2):
        if (len(name1) > len(name2)):
            return None
        else:
            if (len(name2) > len(name1)):
                return None

        for i in range(self.lesserLength(name1, name2)):
            if (name1[i] == name2[i]):
                #No retorna ningun valor puesto que las cadenas son iguales.
                pass
            else:
                return None

        return name1
