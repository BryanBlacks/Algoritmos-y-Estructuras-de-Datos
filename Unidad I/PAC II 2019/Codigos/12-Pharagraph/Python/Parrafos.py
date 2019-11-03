import random

abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#contador = []


class ConstruccionTextosRandom:
    def __init__(self):
        pass
    

     #Metodo para obtener un valor aleatorio.
    def random(self,minimo,maximo):     
        return int(random.random()*(maximo-minimo)+minimo)


    #Metodo para crear palabras random.
    def crearPalabra(self,abecedario,minimo=1,maximo=10):
        numeroPalabras = self.random(minimo,maximo) #Cantidad de caracteres de la palabra
        palabra = []
        #contador.append(numeroPalabras)

        for i in range(numeroPalabras):
            #----Concatenacion de letras para formar la palabra random
            #Dado que la variable "palabra" es un arreglo, se ira adicionando las letras random al arreglo.
            #Ejemp: palabra = ['a','w','f','c']
            palabra.append(abecedario[self.random(minimo,len(abecedario))])

        return "".join(palabra)     #Transforma el arreglo 'palabra' en una cadena mediante la concatenacion(join).
    

    #Metodo para crear oraciones.
    def crearOracion(self,abecedario,minimo=1,maximo=100):
        numeroOraciones = self.random(minimo,maximo)
        oracion = []
        #contador.append(numeroOraciones)

        for i in range(numeroOraciones):
            oracion.append(self.crearPalabra(abecedario))
        return " ".join(oracion)


    #Metodo para crear parrafos.
    def crearParrafo(self,abecedario,minimo=1,maximo=10):
        numeroParrafos = self.random(minimo,maximo)
        parrafo = []
        #contador.append(numeroParrafos)

        for i in range(numeroParrafos):
            parrafo.append(self.crearOracion(abecedario))
        return ". ".join(parrafo)

contenido = ConstruccionTextosRandom()

#--------------P A L A B R A S--------------

#prueba = contenido.crearPalabra(abecedario)
#print (prueba)


#--------------O R A C I O N E S--------------
#prueba2 = contenido.crearOracion(abecedario)
#print (prueba2)  

#--------------P A R R A F O S--------------
prueba3 = contenido.crearParrafo(abecedario)
print (prueba3)

