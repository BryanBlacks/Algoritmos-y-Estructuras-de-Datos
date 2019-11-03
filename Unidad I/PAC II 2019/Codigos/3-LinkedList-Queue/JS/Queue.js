function Node(value) {
    this.value = value;
    this.next = null; //es a lo que apunta al nodo
}

function LinkedList() {
    this.first = null;
    this.add = LinkedListAdd;
    this.print = LinkedListPrint;
    this.addInPosition = LinkedListAddInPosition;
    this.getLast = LinkedListGetLast;
    this.getFirst = LinkedListGetFirst;
    this.delete = LinkedListDelete;
}

function LinkedListAdd(value) {
    //si no existe uno primero lo agrega
    if (!this.first) {
        this.first = new Node(value);
    } //cuando ya existe un primero buscar el ultimo
    //Y agregar el nuevo nodo despues
    else {
        current = this.first;
        while (current.next) {
            current = current.next;
        }
        current.next = new Node(value);
    }
}

function LinkedListDelete(value) {
    prev = null;
    current = this.first;
    if (this.first == null) {
        return false;
    } else {
        while (current.value != value && current.next != null) {
            prev = current;
            current = current.next;
        }

        if (current.value == value) {
            if (current == self.first) {
                if (current.next == null) {
                    this.first = null;
                } else {
                    this.first = current.next;
                }
            } else {
                if (current.next == null) {
                    prev.next = null;
                } else {
                    prev.next = current.next;
                }

            }

        }

    }

}

function LinkedListPrint() {
    current = this.first;
    while (current.next) {
        console.log(current.value);
        current = current.next;
    }
    console.log(current.value);
}

function LinkedListAddInPosition(value, n) {
    count = 0;

    //agrega en el inicio el value 
    if (n == 0) {
        queue = this.first;
        this.first = new Node(value);
        this.first.next = queue;

        return true;
    } else if (n > 0) { //agrega despues del inicio el value
        current = this.first;
        while (current.next) {
            centinela = current; //se necesita guardar la posicion donde se "corta"
            current = current.next;
            count++;
            if (count == n) {

                queue = current;
                current = new Node(value);
                current.next = queue;
                centinela.next = current; //Se usa el centinela para obtener la posicion cortada
                return true;
            }
        }
    }

    return false;
}

function LinkedListGetFirst() {

    return this.first;
}

function LinkedListGetLast() {
    last = this.first;
    while (last.next) {
        last = last.next;
    }
    return last;
}

/*
list = new LinkedList();
list.add("1");
list.add("Hola Mundo");
list.add(2);

 //Lista: "1","2","Hola Mundo","2"
list.addInPosition("6",0);  

console.log("El valor del primer nodo es: ", list.getFirst().value);
console.log("El valor del ultimo nodo es: ", list.getLast().value);



list.print();
//Lista: "1","2","Hola Mundo","2"
list.addInPosition("6", 2);
list.print();*/