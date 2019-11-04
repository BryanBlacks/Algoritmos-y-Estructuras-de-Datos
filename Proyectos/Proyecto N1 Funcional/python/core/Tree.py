from core.LinkedList import *


class Tree:
    def __init__(self):
        self.root = None

    # Este método añade un valor a un nuevo nodo del árbol,
    # si no se espeficica quien es el padre del nuevo nodo
    # este sera por defecto el root, en caso de establecer un parent
    # debe ser un nodo del árbol
    def add(self,value,parent=None):
        if not self.root:
            self.root = Node(value)
            return True
        elif not parent:
            return self.root.children.add(value)
        else:
            return parent.children.add(value)

    # Este método retorna un arreglo con los valores de todos los elementos (hijos)
    # de la lista (children) del nodo parent

    def showChilds(self,parent):
        array = []
        current = parent.children.first
        while current:
            array.append(current.value)
            current = current.next
        return array

    # Este método retorna el nodo padre del nodo en el parámetro child

    def getParent(self,child,parent=None):
        if not self.root:
            return False
        if not parent:
            parent = self.root
        temp = parent.children.searchNode(child)
        if temp:
            return parent
        if parent.next:
            temp = self.getParent(child,parent.next)
            if temp:
                return temp
        if parent.children.first:
            temp = self.getParent(child,parent.children.first)
            if temp:
                return temp
        return False

    # Convierte el arbol a archivo TSV
    def treeToFile(self,filename):
        f = open(filename,"w")
        f.write(self.__treeToFileInner(self.root))
        f.close()

    # Método interno y privado para convertir el árbol a TSV

    def __treeToFileInner(self,current,count=0,text=None):
        if not current:
            return ""
        if not text:
            text = Text()
        text.text += "%s%s%s" % ("\t"*count,current.value,"\n")
        if current.next:
            if current.children.first:
                self.__treeToFileInner(current.children.first,count+1,text)
            self.__treeToFileInner(current.next,count,text)
        elif current.children.first:
            self.__treeToFileInner(current.children.first,count+1,text)
        return text.text

    # Esta función devuelve el nodo con el valor igual al value No DEBE SER USADO SOLO
    # TSVToTree Debe HACERLO

    def getLastTreeNode(self,value,parent=None):
        candidate = None
        if not parent:
            parent = self.root
        if parent.value == value:
            candidate = parent
        temp = parent.children.getNode(value)
        if temp:        
            candidate = temp
        if parent.children.first:
            temp = self.getLastTreeNode(value,parent.children.first)
            if temp:
                candidate = temp
        if parent.next:
            temp = self.getLastTreeNode(value,parent.next)
            if temp:
                candidate = temp
        if candidate:
            if candidate.children.first:
                temp = self.getLastTreeNode(value,candidate.children.first)
                if temp:
                    candidate = temp
        return candidate                    







# Método estático que convierte un archivo .tsv apropiado en un árbol


def TSVToTree(filename):
    f = open(filename,"r")
    content = f.read()
    content = content.split("\n")
    tree = Tree()
    tree.add(content[0].lstrip("\t"))
    for i in range(0,len(content)-1):
        if not content[i][-1] == "/":
            continue
        if content[i+1].count("\t") <= content[i].count("\t"):
            continue
        parent = tree.getLastTreeNode(content[i].lstrip("\t"))
        for j in range(i+1,len(content)):
            if content[i].count("\t") == content[j].count("\t") -1:
                tree.add(content[j].lstrip("\t"),parent)
            elif content[i].count("\t") >= content[j].count("\t"):
                break
    return tree