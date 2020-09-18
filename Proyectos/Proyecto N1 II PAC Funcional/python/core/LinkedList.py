import copy

# Clase que es usada en el árbol para convertirlo a .tsv
class Text:
    def __init__(self):
        self.text = ""

class Node:
    def __init__(self, value):
        self.value = str(value)
        self.next = None
        self.children = LinkedList()


class LinkedList:
    def __init__(self):
        self.first = None

    # Esta función añade un nodo de manera ordenada Pdt. Es un método privado
    # no considere necesario usarlo afuera de esta clase

    def __addNode(self,value):
        value = copy.copy(value)
        value.next = None
        if not self.first:
            self.first = value
            return True

        current = self.first
        prev = self.first
        compare = self.__compare(current, value)
        if compare == -1:
            self.first = value
            self.first.next = current
            return True

        elif compare == 0:
            return False

        else:
            while current.next:
                compare = self.__compare(current, value)
                if compare == -1:
                    prev.next = value
                    prev.next.next = current
                    return True

                elif compare == 0:
                    return False

                prev = current
                current = current.next

            compare = self.__compare(current, value)
            if compare == -1:
                prev.next = value
                prev.next.next = current
                return True

            elif compare == 1:
                current.next = value
                return True

            else:
                return False


    # Esta función crea un nodo con el value igual a value, este es agregado de manera ordenada

    def add(self, value):
        if isinstance(value,Node):
            return self.__addNode(value)
        return self.__addNode(Node(str(value)))

    # Esta función imprime en pantalla todos los nodos

    def showInconsole(self):
        current = self.first
        while current:
            print(current.value)
            current = current.next

    # Retorna el primer nodo con valor igual al parámetro value

    def getNode(self, value):
        current = self.first
        while current:
            if current.value == value:
                return current
            current = current.next
        return False

    # Función booleana que retorna true si un nodo con ese valor se encuentra en la lista

    def searchValue(self,value):
        current = self.first
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # Función booleana que retorna true si el nodo parametro se encuntra en la lista

    def searchNode(self,node):
        current = self.first
        while current:
            if current == node:
                return True
            current = current.next
        return False

    # Elimina el primer nodo que tenga como valor el parámetro value
    def delete(self,value):
        current = self.first
        previous = self.first
        if current.value == value:
            self.first = current.next
            return True
        else:
            current = current.next
            while current:
                if current.value == value:
                    previous.next = previous.next.next
                    return True
                else:
                    current = current.next
                    previous = previous.next
        return False

    # Este método retorna -1 si el valor del nodo current es menor que el valor de el nuevo nodo
    # Pdt. Es un método privado no considere necesario usarlo afuera de esta clase

    def __compare(self,current, New):
        alphabet = " !#$%&'()/+,-.0123456789:;=@AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz[]^_`}{~"
        if isinstance(current, Node):
            valueCurrent = str(current.value)
        else:
            valueCurrent = str(current)

        if isinstance(New, Node):
            valueNew = str(New.value)
        else:
            valueNew = str(New)

        if len(valueCurrent) < len(valueNew):
            for i in range(len(valueCurrent)):
                if alphabet.index(valueCurrent[i]) < alphabet.index(valueNew[i]):
                    return 1
                elif alphabet.index(valueCurrent[i]) > alphabet.index(valueNew[i]):
                    return -1

            return 1

        if len(valueNew) < len(valueCurrent):
            for i in range(len(valueNew)):
                if alphabet.index(valueNew[i]) < alphabet.index(valueCurrent[i]):
                    return -1
                elif alphabet.index(valueNew[i]) > alphabet.index(valueCurrent[i]):
                    return 1

            return -1

        if len(valueCurrent) == len(valueNew):
            for i in range(len(valueNew)):
                if alphabet.index(valueCurrent[i]) < alphabet.index(valueNew[i]):
                    return 1

                elif alphabet.index(valueNew[i]) < alphabet.index(valueCurrent[i]):
                    return -1

            return 0


