from Compare import*
from LinkedList import*

class Tree:

    def __init__(self,):
        #Creación de root como Carpeta Principal
        self.root = Node(Directory("/.")) 
        
    def thisRoot(self):
        return self.root
   
    def add(self, name, _type, reference=None):
        #Sí lo que se quiere agregar es una carpeta se crea un nodo tipo carpeta
        if(_type == 'D'):       
            #name= "%s%s"%(name,"/")
            newNode=Node(Directory(name))

        #Sí lo que se quiere agregar es un archivo se crea un nodo tipo archivo 
        else:
            if(_type == 'F'):
                newNode=Node(File(name))

        #Sí no hay un nodo de referencia(Carpeta) se guardará como hijo del directorio principal(raíz)
        if(not reference):
            parentNode=self.root
            parentNode.value.children.addList(newNode)

        #Sí hay un nodo de referncia(carpeta) se guardará como hijo de dicha carpeta
        else:
            parent = self.search(reference)
            parent.value.children.addList(newNode)


    
    #Método para buscar un nodo basado en su nombre
    def search(self, value,current=None):

        comp = Compare()

        if(not current):
            current=self.root

        if(current.next):
            if(comp.compare_(current.value.name,value)):
                return current
            
            else:
                if(current.value.type == 'D'):
                    if (current.value.children.first):
                        if (self.search(value, current.value.children.first)):
                            current = current.value.children.first
                            return self.search(value, current)
                        
                        else:
                            current = current.next
                            return self.search(value, current)

                    else:
                        current = current.next
                        return self.search(value, current)
                else:
                    current = current.next
                    return self.search(value,current)



        else:
            if(comp.compare_(current.value.name,value)):
                return current
            
            else:                

                if(current.value.type == 'D'):
                    if(current.value.children.first):
                        if(self.search(value,current.value.children.first)):
                            current = current.value.children.first
                            return self.search(value, current)
                        
                        else:
                            return None

                    else:
                        return None
                else:
                    return None

    #Eliminar nodo del árbol
    def delete(self, nameNode, parent=None):
        
        if(not parent):
            current = self.root
            current.value.children.remove(nameNode, current.value.children.first)

        else:
            current = parent
            current.value.children.remove(node, current.value.children.first)

    #Para guardar el árbol en un archivo txt con tabulado
    def save(self,tt="",tree=None,tab=""):

        """
            Se inicia el recorrido desde la raíz imprimiendo el nombre del nodo que ocupe la
            variable tree, luego se recorren los hijos y seguira concatenando los nombres con
            su respectivo tabulado(en profundidad) finalizando con una cadena de texto que 
            representará al árbol con tabulado
        """

        if(not tree):
            tree = self.root
    
        if(tree.value.type == 'D'):
            tt1= "%s%s%s/%s"%(tt,tab, tree.value.name,"\n")
        else:
            tt1= "%s%s%s%s"%(tt,tab, tree.value.name,"\n")
        if(tree.value.type == 'D'):
            current= tree.value.children.first
        else:
            current = None
        while(current is not None):
            ttx= self.save(tt1,current, "%s%s"%(tab,"\t"))

            while(current.next is not None):
                current = current.next
                tt2= self.save(ttx,current,"%s%s"%(tab,"\t"))
                if(tt2):
                    ttx = tt2
                if(not current.next):
                    return tt2
            if(not current.next):
                return ttx   
        


        return tt1

    #Guardar en un arreglo el nombre de los nodos hijos de una carpeta y retorna el arreglo
    def array(self, tree=None):

        

        if(tree is None):
            tree = self.root
            son=[]
        else:
            if(tree.value.name == '/.'):
                son = []
            else:
                son = [".",".."]

        child= tree.value.children
        if(child.first):

            current = child.first
            while(current):
                son.append(current.value.name)
                current = current.next

        else:
            return son

        return son
    #Funcion para leer el texto plano y pasarlo al arbol
    def fromPlainText(self):
            f = open("PRUEBA.txt","r")
            lines = f.readlines()
            l = len(lines)

            
            #print(lines)
            for i in range(l):
                line = lines[i]
                li = len(line)
                n = line.count("\t", 0, li)
                if(n == 0):
                    root = self.root.value.name
                else:
                    if(n == 1):
                        parent = root
                        pa = parent.replace('\n', '')
                        current = lines[i]
                        cu = current.replace('\t', '')
                        cur = cu.replace('\n', '')
                        d = cur.count("/", 0, len(cur))
                        if(d == 1):  
                            Current = cur.replace('/', '')
                            self.add(Current, "D", pa)
                        else: 
                            self.add(cur, "F", pa)
                    else:
                        if(n == 2):
                            parent = cur
                            pa = parent.replace('\t', '')
                            par = pa.replace('\n', '')
                            Parent = par.replace('/', '')
                            new = lines[i]
                            N = new.replace('\t', '')
                            ne = N.replace('\n', '')
                            dd = ne.count("/", 0, len(ne))
                            if(dd == 1):  
                                New = ne.replace('/', '')
                                self.add(New, "D", Parent)
                            else: 
                                self.add(ne, "F", Parent)
                        else:
                            if(n > 2):
                                #Si el anterior tiene un tab menos, el anterior es el padre
                                tabs = lines[i-1].count("\t", 0, len(lines[i-1]))
                                tab = lines[i].count("\t", 0, len(lines[i]))
                                if(tabs < tab):
                                    parent = lines[i-1]
                                else:
                                    parent = ne
                                pa = parent.replace('\t', '')
                                par = pa.replace('\n', '')
                                Parent = par.replace('/','')
                                new = lines[i]
                                N = new.replace('\t', '')
                                ne = N.replace('\n', '')
                                ddd = ne.count("/", 0, len(ne))
                                if(ddd == 1):  
                                #self.add(pa, "D")
                                    New = ne.replace('/', '')
                                    self.add(New, "D", Parent)
                                    
                                else: 
                                    self.add(ne, "F", Parent)
            f.close() 

    
class DoubleLinked:

    def __init__(self, k):
        self.first = k

    def linked(self, node, current= None):

        if(not current):
            current = self.first
        
        while(current.next):
            current = current.next
        
        current.next = node
        anex = current.next
        anex.prev = current 
    
    def search1(self,node,current = None):

        com = Compare()

        if(not current):
            current = self.first
        
        if(current.next):
            if(com.compare_(current.value.name,node)):
                return current
            
            else:
                current = current.next
                return self.search1(node,current)

        else:
            if(com.compare_(current.value.name,node)):
                return current
    
    def nodePrev(self,node):
        return node.prev

    def dele(self, node=None):

        if(not node):
            node= self.first
        
        while(node.next):
            node = node.next
        
        current= self.nodePrev(node)
        current.next = None






"""
    tree = Tree()
    tree.add("Hola", "D")
    tree.add("Hola1", "D", "Hola")
    tree.add("File1", "F", "Hola")
"""