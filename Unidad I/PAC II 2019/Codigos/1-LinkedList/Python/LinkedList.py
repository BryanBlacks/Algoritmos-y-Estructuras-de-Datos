#-*- coding.utf8 -*-
class Node: 
    def __init__(self, name, student):
        self.name = name
        self.student = student
        self.next = None

class LinkedList:
    def __init__(self, Node):
        self.first = Node

class Student:
    def __init__(self, name, accountNumber):
        self.name = name
        self.accountNumber = accountNumber
        self.average = "100"

Juan = Student("Juan", "20193012")
node = Node(0, Juan)
listS = LinkedList(node)

print("la variable lista es: %s" % listS)
print("la variable nodo es: %s" % node)
print("la variable estudiante es: %s" % Juan)