import random
class Recursive:
    def __init__(self):
        pass
    
    #Metodo para factorial recursivo.
    def factorial(self,n):
        if(n<2):
            return 1
        
        else:
            return n*self.factorial(n-1)

    #Metodo para fibonacci recursivo.
    def fibonacci(self,n):
        if(n==0 or n==1):
            return n

        #print ("El valor de %s es %s" %('n', n ))
        #print ("El valor de %s es %s" %('n-2', n-2 )) 
        #print ("El valor de %s es %s" %('n-1', n-1 ))
        #print ('------------------------------------')    
        temp = self.fibonacci(n-2) + self.fibonacci(n-1)
        return temp

    #Metodo para generar un valor random.
    def randomInt2(self,min=0,max=10):
        r = random.random()
        return int(r*(max-min)+min)



#======================= M A I N =======================
recursividad = Recursive()                  #Nuevo objeto tipo Recursive().
NumRandom = recursividad.randomInt2()       #Numero random generado.


#Entrada de datos
#Guardara el valor ingresado por el usuario.
print ('------M E N U------\n')
respuesta = int(input("1. Factorial \n2. Fibonacci \nEscriba el numero de la operacion a realizar: "))
print ('\n')
modo = int(input('1.Manual \n2.Automatico \nDatos de manera... '))
print('')


#Condiciones dependiendo de lo que el usuario a elegido.
#Condicion para factorial.
if (respuesta==1):

    #Condicion si los datos se ingresan de manera manual.
    if(modo==1):
        NumFact = int(input('Ingrese un numero: '))
        print ("El factorial de %s es %s" %(NumFact, recursividad.factorial(NumFact)))
    
    #Condicion si los el valor es automatico.
    elif(modo==2):
        print ("El factorial de %s es %s" %(NumRandom, recursividad.factorial(NumRandom)))

    else:
        print('Valor erroneo')



#Condicion para fibonacci
elif(respuesta==2):

    #Condicion si los datos se ingresan de manera manual.
    if(modo==1):    
        NumFib = int(input('Ingrese un numero: '))
        print ("El fibonacci de %s es %s" %(NumFib, recursividad.fibonacci(NumFib)))

    #Condicion si los datos se ingresan de manera automatica.
    elif(modo==2):
        print ("El factorial de %s es %s" %(NumRandom, recursividad.factorial(NumRandom)))    

else:
    print('Dato de entrada no valido!')