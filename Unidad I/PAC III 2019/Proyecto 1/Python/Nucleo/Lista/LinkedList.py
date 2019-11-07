# -*- coding:utf-8 -*-
from Product import *
from Node import *


class LinkedList:
    def __init__(self):
        self.first = None
    
    def push(self, value, pos):
        if (not self.first):
            self.first = Node(value)
            return True
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True

    def pop(self,pos=0):
        if (not self.first):
            return False
        else:
            if (pos >-1):
                if(n==0):
                    current = self.first
                    self.first = current.next
                    return True
                else:
                    count = 1
                    prev = self.first
                    last = prev.next
                    while(last):
                        if(count == pos):
                            prev.next = last.next
                            return True
                        prev = last
                        last = last.next
                        count = count+1
            else:
                return False


    def search(self,pos=0):
        if(pos==0):
            return self.first.value
        else:
            count=1
            prev = self.first
            last = prev.next
            while(last):
                if(pos == count):
                    return last.value             
                last = last.next
                count= count+1
            
            return False


    def length(self):
        if(not self.first):
            return 0
        else:
            lot = 1
            current = self.first
            while(current.next):
                lot = lot+1
                current = current.next
            return lot


    def generateTable(self):
        pass

    