
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Directory:
    def __init__(self, value):
        self.type = "D"
        self.name = value
        self.children = LinkedList()
        
class File:
    def __init__(self, value):
        self.type = "F"
        self.name = value

"""
    El método addList guarda los nodos en una lista enlazada(hijos de una carpeta), iniciando en la
    carpeta raíz(root) y al mismo tiempo los ordena en prioridad de Carpeta, luego Archivos que a 
    su vez son ordenados por nombre
"""


class LinkedList:

    def __init__(self):
        self.first = None

    def addList(self, newNode, prev = None, current = None):
         

        if(not self.first):
            self.first = newNode
            return True

        if(not prev):
            prev = self.first

        if( newNode.value.type == 'D'):
                if( prev.value.type == 'D'):
                    
                    if( self.order(newNode.value.name,prev.value.name) > 0 ):
                        if(prev is self.first):
                            self.first = newNode
                            newNode.next = prev
                            return True
                        else:
                            current.next = newNode
                            newNode.next = prev
                            return True

                    else:
                        current = prev
                        prev = prev.next
                        return self.addList(newNode,prev,current)


                else:
                    if( prev.value.type == 'F'):
                        current.next = newNode
                        newNode.next = prev
                        return True
                    
                    if(prev is None):
                        current.next = newNode
                        return True

        else:
                if(prev.value.type == 'F'):

                    if( self.order(newNode.value.name,prev.value.name) > 0 ):
                        if(prev is self.first):
                            self.first = newNode
                            newNode.next = prev
                            return True
                        else:
                            current.next = newNode
                            newNode.next = prev
                            return True

                    else:
                        if(prev):
                            current = prev
                            prev = prev.next
                            return self.addList(newNode,prev,current)


                


                else:
                    while(not(prev is None) and prev.value.type == 'D' ):
                        current = prev
                        prev = prev.next

                    if(prev is None):
                        current.next = newNode
                    
                    else:
                        return self.addList(newNode,prev,current)

    #Método que compará la cadena mayor entre dos cadenas de caracteres(nombres)   
    def order(self,name1,name2,i=0):

        al = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        if( al.index(name1[i]) > al.index(name2[i]) ):
            return 1

        else:
            if( al.index(name1[i]) == al.index(name2[i]) ):
                i=i+1
                return self.order(name1,name2,i)

            else:
                if( al.index(name1[i]) < al.index(name2[i]) ):
                    return -1

    #Elimina un nodo de una lista sin perder los nodos enlazados al nodo eliminado
    def remove(self, node, anex):

        
        if(anex.value.name == node):
            self.first = anex.next

        prev = anex
        anex = anex.next
        
        while(anex):
            if(anex.value.name == node):
                prev.next = anex.next

            else:
                prev = anex
                anex = anex.next
                

        



                            

