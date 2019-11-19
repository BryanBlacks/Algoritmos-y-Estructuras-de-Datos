class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.children = LinkedList()
class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, value):
        if not self.first:
            self.first = Node(value)
            return True
        else:
            current  = self.first
            while current.next:
                current = current.next
            current.next = Node(value)
            return True
        return False

    def search(self,value):
        if not self.first:
            return False
        else:
            current  = self.first
            while current:
                if current.value == value:
                    return current
                current = current.next
            return False
    
    def pop(self,value):
        if not self.first:
            return False
        else:
            current  = self.first
            if current.value == vlue:
                self.first = self.first.next
            else:
                while current:
                    if current.value == value:
                        # Se debe guardar y devolver el elemento que se borrar
                        return current
                    current = current.next
                return False

class Tree:
    def __init__(self):
        self.root = Node("c:\\\\")
        self.trash = LinkedList()
    
    def add(self, value, current=None):
        if not current:
            current = self.root
        #Validar Tipo De Dato para saber que current es un Nodo
        current.children.add(value)
    
    def search(self, value, current = None):
        if not current:
            current = self.root
        #Validar Tipo De Dato para saber que current es un Nodo
        return current.children.search(value)

    def remove(self,value,current=None):
        if not current:
            current = self.root
        #Validar Tipo De Dato para saber que current es un Nodo
        return trash.add(DeletedElement(current,current.children.pop(value))
