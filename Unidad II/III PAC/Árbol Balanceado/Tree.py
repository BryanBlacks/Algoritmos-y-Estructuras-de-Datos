#-*- coding:utf8 -*- 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.children = LinkedList()

class DeletedElement:
    def __init__(self,parent,deletedNode):
        self.parent = parent
        self.deletedNode = deletedNode

"""
----------------------------Balanceo-----------------------------
*Simbolos --> Numeros --> Letras Minusculas --> Letras Mayusculas

Se hace un metodo que compare el current.value
    Si es -1 el parametro 1 es menor que el parametro 2
    Si es 0 parametro 1 y parametro 2 son iguales
    Si es 1 el parametro 1 es mayor que parametro 2

"""
class Compare:
    def __init__(self):
        self.alphabet = " !#$%&/()=?¡'¿[]-:;,.+*´_0123456789abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ"

    def greaterLength(self,str1, str2):
        greater = len(str1)
        if(len(str2) > greater): greater = len(str2)
        return greater  

    def lesserLength(self,str1, str2):
        lesser = len(str1)
        if(len(str2) < lesser): lesser = len(str2)
        return lesser
        
    def compare(self,obj1,obj2):
        if(isinstance(obj1,Node)):
            obj1 = (str(obj1.value)).strip()
        if(isinstance(obj2,Node)):
            obj2 = (str(obj2.value)).strip()

        if(isinstance(obj1,int)):
            obj1 = (str(obj1)).strip()
        if(isinstance(obj2,int)):
            obj2 = (str(obj2)).strip()

        obj1 = obj1.strip()
        obj2 = obj2.strip()
        
        lesser = self.lesserLength(obj1,obj2)

        for i in range(lesser):
            if self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i]):
                return 1
            elif self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i]):
                return -1
                
        if (lesser == self.greaterLength(obj1,obj2)):
            return 0   
        elif len(obj1) == lesser:
            return -1
        else:
            return 1

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self,value):
        if not self.first:
            self.first = Node(value)
        else:
            current = self.first
            prev = None
            compare = Compare()
            
            while(current):
            #Si el valor del actual es menor al valor del que deseo agregar
                if (compare.compare(value, current.value) < 0):
                    if not current.next:
                    #Si no hay siguiente del actual y se debe de seguir avanzando,
                      #el nuevo nodo se agrega al final de la lista.
                        current.next = Node(value)
                        return True
                    else:
                        #Si tiene siguiente se sigue avanzando en la lista
                        prev = current
                        current = current.next

            #Si el valor del actual es el mismo al que deseo agregar, reemplazo el nodo
                elif (compare.compare(value, current.value) == 0):
                    if not prev:
                        #Si no tiene previo, esto indica que el nodo a reemplazar es el primero de la lista
                        self.first.next = current.next
                        self.first = Node(value)
                        return True
                    else:
                        #Si el atual no tiene siguiente no hay necesidad de enlazar un nulo al nuevo nodo, ya lo tiene
                        if not current.next:
                            prev.next = Node(value)
                            return True
                        
                        #Si no se reemplaza normalmente
                        else:
                            prev.next = Node(value)
                            prev.next.next = current.next
                            return True

                #Si el actual es mayor al que se desea agregar
                else:
                    #Si no tiene previo, el nuevo será el primero en la lista
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
                        # Se debe guardar y devolver el elemento que se borrar
                        parent = current.value
                        return parent
                    current = current.next
                return False

    def PrintLL(self):    
        current = self.first
        trail = " "
        while (current.next):
            trail += str(current.value) 
            trail += " --> "
            current = current.next
"""
------------------------------------------Árbol Generico------------------------------------------
* Árbol que tiene n nodos que tienen por hijos una lista enlazada balanceada haciendo uso del
    compare que ordena los nodos al agregarlos al árbol.
"""
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
tree.add(4,5)

#tree.remove("hola",4)
