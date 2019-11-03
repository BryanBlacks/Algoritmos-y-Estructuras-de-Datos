class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None

class Stack:
    def __init__(self):
        self.last = None

    def push(self,value):
        if not self.last:
            self.last = Node(value)
            return True
        else:
            before = self.last
            self.last = Node(value)
            self.last.prev = before
            return True

    def printS(self):
        if not self.last:
            return None
        else:
            current = self.last
            stack = ("%s%s" %("\n",current.value))
            while current.prev:
                current = current.prev
                stack = stack + ("%s%s" %("\n",current.value))
            return stack

    def pop(self):
        if not self.last:
            return None
        else:
            if not self.last.prev:
                temp = self.last
                self.last = None
                return temp.value
            else:
                current = self.last
                self.last = current.prev
                return current.value
        return None