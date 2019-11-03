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
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True
        return False

    def addInPosition(self, value, position):
        count = 0
        if position == 0:
            queue = self.first
            self.first = Node(value)
            self.first.next = queue

            return True
        else:
            if position > 0:
                current = self.first
                before = self.first
                while current.next:
                    current = current.next
                    count = count +1
                    if count == position:
                        before.next = Node(value)
                        before.next.next = current
                        return True
                    before = before.next
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

    def getFirst(self):
        return self.first

    def getLast(self):
        last = self.first
        while last.next:
            last = last.next
        return last

    def printLL(self):
        current = self.first
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

