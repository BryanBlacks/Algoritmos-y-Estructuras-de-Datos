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
            if current.value == value:
                parent = current.value
                self.first = self.first.next
                return parent
            else:
                while current:
                    if current.value == value:
                        # Se debe guardar y devolver el elemento que se borrar
                        parent = current.value
                        return parent
                    current = current.next
                return False
    

class DeletedElement:
    def __init__(self,parent,deletedNode):
        self.parent = parent
        self.deletedNode = deletedNode

class Tree:
    def __init__(self):
        self.root = Node("c:\\\\")
        self.trash = LinkedList()
    
    def add(self, value, current=None):
        if not current:
            current = self.root
            print ("El nodo %s se agregará como hijo de la raíz" % value)
            return current.children.add(value)
        else:
            #Validar Tipo De Dato para saber que current es un Nodo
            if isinstance(current,Node):
                print("El nodo %s  se agregará como hijo de %s" %(value,current.value))
                return current.children.add(value)
            else:
                print("El nodo padre %s No se encontró en el árbol, %s se agregará en la raíz"%(current,value))
                return self.root.children.add(value)
    
    def search(self, value, current = None):
        #Validar Tipo De Dato para saber que current es un Nodo
        if not current or not isinstance(current,Node):
            current = self.root
            return current.children.search(value)

        else:
            if current.children.search(value):
                #print("El nodo padre %s se ha encontrado en el árbol"%(current.value))
                return current.children.search(value)
            else:
                print("El nodo padre %s no se encuentra en la lista"%(current))
                return False


    def remove(self,value,current=None):
        if not current:
            print("El nodo %s se eliminará del nodo raíz %s" % (value,current.value))
            current = self.root
        #Validar Tipo De Dato para saber que current es un Nodo
        if isinstance(current,Node):
            print("Se eliminará el nodo %s del nodo padre %s"%(value,current))
            return trash.add(DeletedElement(current,current.children.pop(value)))
        else:
            print("El nodo padre %s No se encontró en el árbol, %s se agregará en la raíz"%(current,value))
            return self.root.children.add(value)



tree= Tree()
tree.add(4)
tree.add("A")
tree.add("J")
tree.add("hola",tree.search(4))
tree.add("Hola2",tree.search("hola",tree.search(4)))
tree.add("Adios",tree.search("A"))
tree.add("Prueba",tree.search("Adios",tree.search("A")))

#tree.remove("hola",4)
