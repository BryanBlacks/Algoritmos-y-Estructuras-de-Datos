# -*- coding:utf8 -*-

class Node:
    
    def __init__(self,value,date,parent):
        self.value = value
        self.date = date
        self.parent = parent
        self.next = None