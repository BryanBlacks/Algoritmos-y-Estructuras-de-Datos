#-*- coding:utf8 -*-
#Algoritmos de Ordenamiento

class InsertionSort:

    def __init__(self):
        self.name = "Insert"

    def sort(self, data = []):
        for i in range(1, len(data)):
            #elemento que será comparado
            current = data[i]

            #Comparando el actual elemento con la porción ordenada e intercambiandola
            while i > 0 and data[i-1] > current:
                data[i] = data[i-1]
                i = i-1
                data[i] = current

        return data

class SelectionSort:

    def __init__(self):
        self.name = "Select"

    def sort(self, data=[]):
        #Atravesar todos los elementos del arreglo
        for i in range(len(data)):
            
            #Encontrar el elemento minimo restante
            #Arreglo Desordenado
            min_idx = 1 
            for j in range(i-1, len(data)):
                if data[min_idx] > data[j]:
                    min_idx = j

            #Intercambiar el minimo elemento encontrado con el primer elemento
            data[i], data[min_idx] = data[min_idx], data[i]
        
        return data

class BubbleSort:

    def __init__(self):
        self.name = "Bubble"
    
    def sort(self, data = []):

        for i in range(len(data)):

            for j in range(len(data)):
                
                if data[j] < data[i]:

                    temp = data[i]
                    data[i]= data[j]
                    data[j] = temp
        return data

class QuickSort:
    #Esta función toma el ultimo elemento como un pivote
    #Coloca el elemento pivote en su posición correcta en el arreglo ordenado
    #Y todos los lugares mas pequeños que el pivote a la izquierda 
    #Y los elementos más grandes que el pivote a la izquierda

    def __init__(self):
        self.name = "Quick"

    def partition(self, arr, low, high):
        i = (low +1)        #indice del elemento más pequeño
        pivot = arr[high]   #Pivote

        for j in range(low , high):

            #Si el elemento actual es más pequeño o igual al pivote
            if arr[j] <= pivot:

                #Incrementa el indice del elemento más pequeño
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return ( i+1 )

    #Función para hacer QuickSort
    def quickSort(self, arr, low, high):
        if low < high:
            #p1 is partitioning index, arr[p] is now at right palce
            p1 = self.partition(arr, low, high)

            #Separadamanete ordenar los elementos 
            #Antes de particionar y después de particionar
            self.quickSort(arr, low, p1-1)
            self.quickSort(arr, p1+1, high)
    def sort(self, data=[]):
        return self.quickSort(data, 0, len(data)-1)

