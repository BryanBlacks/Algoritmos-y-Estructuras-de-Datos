#-*- coding:utf8 -*-
#Clase nodo
class Node:
    def __init__(self,value):
        self.value = value
        self.rightChild = None
        self.leftChild  = None
    
    #Establece un valor.
    def setValue(self,value):
        self.value=value    
    
    #Obtiene el valor del nodo.
    def getValue(self): 
        return self.value

#Clase BynariSearchTree
class BST():

    def __init__(self):
        self.root = None                        #Variable que guarda la raiz.
    
    def setRoot(self,value):                    #Establece el nodo raiz.
        self.root=Node(value)
    
    def add(self,value):                        #Agrega al BST()
        if self.root is None:                   #En caso que no exista raiz.
            self.setRoot(value)
            
        else:                                   #En caso que ya haya una raiz.
            self.addInner(self.root,value)      #Llamado recursivo.
    
    def addInner(self,currentNodo,value):       #Funcion para agregar 'abajo' de la raiz.
        if currentNodo.value >= value:
            if currentNodo.leftChild is not None:
                self.addInner(currentNodo.leftChild,value)
            else:
                currentNodo.leftChild = Node(value)

        else:
            if currentNodo.rightChild is not None:
                self.addInner(currentNodo.rightChild,value)
            else:
                currentNodo.rightChild = Node(value)

    def search(self,value):                     #Buscar un nodo en BST()
        return self.searchInner(self.root,value)#Llamado recursivo a la busqueda 'bajo' la raiz.

    def searchInner(self,currentNodo,value):    #Funcion de busqueda interna.

        if currentNodo is None:                 #En caso que el root este vacio.
        	return False
        elif currentNodo.value == value:        #Si ya hay un root.
        	return True
        elif currentNodo.value > value:
        	return self.searchInner(currentNodo.leftChild,value)
        else:    
        	return self.searchInner(currentNodo.rightChild,value)    



#------------------- M A I N -------------------
BinaryTree = BST()          #Objeto tipo BST()

BinaryTree.add(1)
BinaryTree.add(2)
BinaryTree.add(3)
BinaryTree.add(6)

print('El valor | %s | existe en el BST ?   ... %s ' %(1,BinaryTree.search(1)))
print('El valor | %s | existe en el BST ?   ... %s ' %(5,BinaryTree.search(5)))
print('El valor | %s | existe en el BST ?   ... %s ' %(4,BinaryTree.search(4)))
