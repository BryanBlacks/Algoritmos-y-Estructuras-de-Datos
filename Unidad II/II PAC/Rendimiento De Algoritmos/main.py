#-*- coding:utf-8 -*-
from Algorithms import (SelectionSort, InsertionSort,  QuickSort, BubbleSort)
from Performance import (TestPerformance, ExecutionTime, ArrayGenerator)

execution = ExecutionTime()
test = TestPerformance()
arrayGenerator = ArrayGenerator()
array = arrayGenerator.generate(10000)
result = []

bubbleSort = BubbleSort()
insertionSort = InsertionSort()
selectionSort = SelectionSort()
quickSort = QuickSort()

bubble = test.test(
    bubbleSort,
    execution, 
    array[:]
)
result.append(bubble)

insert = test.test(
    insertionSort,
    execution, 
    array[:]
)
result.append(insert)

select = test.test(
    selectionSort,
    execution, 
    array[:]
)
result.append(select)

quick = test.test(
    quickSort,
    execution, 
    array[:]
)
result.append(quick)

print("-"*110)
print("\t%s\t\t|\t\t%s\t\t|\t\t\t%s" % ("Nombre", "Tamaño", "Tiempo"))
print("-"*110)

for name, size, time in result:
    print("\t%s\t\t|\t\t%s\t\t|\t\t\t%s" % (name, size, time))
print("-"*110)