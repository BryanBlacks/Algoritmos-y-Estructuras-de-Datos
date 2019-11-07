# -*- coding:utf-8 -*-
from Node import *


class ABB_1:
    def __init__(self):
        self.root = None

    def add(self,value):
        return self.addInner(value,self.root)

    def addInner(self,value,current):
        if(not self.root):
            self.root = Node(value)
            return True
        else:
            if(value.cost > current.value.cost):
                if (current.right):
                    current = current.right
                    return self.addInner(value, current)
                else:
                    current.right = Node(value)
                    return True
            else:
                if(value.cost < current.value.cost):
                    if (current.left):
                        current = current.left
                        return self.addInner(value, current)
                    
                    else:
                        current.left = Node(value)
                        return True
                """
                else:
                    if(value.cost == current.value.cost):
                        pass
                """
