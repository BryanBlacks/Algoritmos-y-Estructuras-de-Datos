# -*- coding:utf8 -*-

from LinkedList import LinkedList

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.children = LinkedList()