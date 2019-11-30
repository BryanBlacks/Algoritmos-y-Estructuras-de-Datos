from Compare import*

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self,value):
        if not self.first:
            self.first = Node(Vertex(value))
        else:
            current = self.first
            prev = None
            compare = Compare()
            
            while(current):
                if (compare.compare(value, current.value) < 0):
                    if not current.next:
                        current.next = Node(value)
                        return True
                    else:
                        prev = current
                        current = current.next

                elif (compare.compare(value, current.value) == 0):
                    if not prev:
                        self.first.next = current.next
                        self.first = Node(value)
                        return True
                    else:
                        if not current.next:
                            prev.next = Node(value)
                            return True
                        
                        else:
                            prev.next = Node(value)
                            prev.next.next = current.next
                            return True

                else:
                    if not prev: 
                        self.first = Node(value)
                        self.first.next = current
                        return True
                    else:
                        prev.next = Node(value)
                        prev.next.next = current
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
            if current.value == value:
                parent = current.value
                self.first = self.first.next
                return parent
            else:
                while current:
                    if current.value == value:
                        
                        parent = current.value
                        return parent
                    current = current.next
                return False