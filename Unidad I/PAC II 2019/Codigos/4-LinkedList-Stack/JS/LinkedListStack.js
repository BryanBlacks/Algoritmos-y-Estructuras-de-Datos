function Node(value) {

    this.value = value;
    this.next = null;
}
/* 
       Debemos utilizar el nombre correcto de la Class
       LinkedList cambia a Stack(Pilas) o Queue(Colas)
       cuando hacemos uso de Stacks o Queues, el metodo "Add" debe renombrarse y 
       llamarse "push".

       Al hecho de extraer un dato de una Pila o de una Cola se le conoce como "pop". 

       El metodo .add, cambia a .push

*/
function Stack() { //cambia de LinkedList a Stack

    this.first = null;
    this.empty = LinkedListEmpty;
    this.push = LinkedListAdd;
    //cambia de add a push, el push se programara dependiendo
    //de la necesidad de la estructura de datos
}

function LinkedListEmpty() {
    return this.first == null;
}

function LinkedListAdd(obj) {
    if (this.empty()) {
        this.first = new Node(obj);

    } else {
        rest = this.first;
        this.first = new Node(obj);
        this.first.next = rest;
    }
}

function PaperPages(content) {
    this.content = content;
}