#-*- coding:utf-8 -*-
from Algorithms import (SelectionSort, InsertionSort,  QuickSort, BubbleSort)
from Performance import (TestPerformance, ExecutionTime, ArrayGenerator)

test = TestPerformance()
arrayGenerator = ArrayGenerator()
array = arrayGenerator.generate(100)
result = []


bubbleSort = BubbleSort()
selectionSort = SelectionSort()
insertionSort = InsertionSort()
quickSort = QuickSort()

"""
Para Imprimir el arreglo aleatorio y el arreglo ordenado
--------------------------------------------------------
finalArray = bubbleSort.sort(array)
result.append(finalArray)
print("-"*40)
print("BubbleSort")
print("-"*40)
print(array)
print(finalArray)
"""

finalArray = test.test(lambda: bubbleSort.sort(array[:]))
array, time = finalArray
print("-"*40)
print("BubbleSort")
print("-"*40)
print("%s \nEl tiempo es %s milisegundos" % (array,time))

finalArray = test.test(lambda: selectionSort.sort(array[:]))
array, time = finalArray
print("-"*40)
print("SelectionSort")
print("-"*40)
print("%s \nEl tiempo es %s milisegundos" % (array,time))

finalArray = test.test(lambda: insertionSort.sort(array[:]))
array, time = finalArray
print("-"*40)
print("InsertionSort")
print("-"*40)
print("%s \nEl tiempo es %s milisegundos" % (array,time))

#qarray = [i for i in range(100,0,-1)]
array = arrayGenerator.generate(100)
print("---> %s" % array[:])
finalArray = test.test(lambda: quickSort.sort(array[:]))
array, time = finalArray
print("-"*40)
print("QuickSort")
print("-"*40)
print("%s \nEl tiempo es %s milisegundos" % (array,time))