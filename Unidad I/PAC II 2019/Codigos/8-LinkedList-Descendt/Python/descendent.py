#-*- coding:utf8 -*-
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, value):
        if not self.first:
            self.first = Node(value)
            return True
        else:
            if self.first.value <= value:
                stack = self.first
                self.first = Node(value)
                self.first.next = stack

            else:
                prev = self.first
                current = prev.next
                while current:
                    if current.value <= value:
                        prev.next = Node(value)
                        prev.next.next = current
                        return True
                    prev = current
                    current = prev.next
                prev.next = Node(value)
                return True
        return False

    def delete(self, value):
        prev = None
        current = self.first
        if self.first is None:
            return False
        else:
            while (current.value != value and current.next is not None):
                prev = current
                current = current.next
            if(current.value == value):
                if current == self.first:
                    if current.next is None:
                        self.first = None
                    else:
                        self.first = current.next
                else:
                    if current.next is None:
                        prev.next = None
                    else:
                        prev.next = current.next
            else:
                return False

    def printLL(self):
        current = self.first
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

newlist = LinkedList()
newlist.add(4)
newlist.add(5)
newlist.add(8)
newlist.add(2)
newlist.add(3)
newlist.add(14)
newlist.add(11)
newlist.add(9)
newlist.delete(3)
newlist.printLL()
                    

        