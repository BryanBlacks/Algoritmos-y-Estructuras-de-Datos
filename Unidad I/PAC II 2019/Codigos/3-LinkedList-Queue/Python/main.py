#-*- coding:utf8 -*-
from Queue import *
newList = LinkedList()
newList.add("4")
newList.add("Hola Mundo")
newList.add("2")
newList.addInPosition("8", 0)
newList.addInPosition("3", 2)
newList.printLL()
print("\n")
newList.delete("Hola Mundo")
newList.printLL()
first = newList.getFirst()
last = newList.getLast()

print("El valor del primer nodo es: %s" % first.value);
print("El valor del ultimo nodo es: %s"% last.value);