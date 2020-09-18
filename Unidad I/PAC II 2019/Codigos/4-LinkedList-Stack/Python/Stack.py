class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, value):
        if(not self.first):
            self.first = Node (value)
        else:
            rest = self.first
            self.first = Node(value)
            self.first.next = rest

    def Print(self):
        current = self.first
        while(current.next):
            print(current.value.content)
            current = current.next
        print(current.value.content)
        
class BookPages: 
    def __init__(self, content):
        self.content = content

libro = LinkedList()

libro.add(BookPages("Contenido pagina 1: Portada"))
libro.add(BookPages("Contenido pagina 2: Medio"))
libro.add(BookPages("Esto es pagina 3: Ultima"))
libro.Print()
