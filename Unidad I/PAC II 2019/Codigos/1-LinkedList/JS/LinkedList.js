function Node(name, student) {
    this.name = name;
    this.student = student;
    this.next = null;
}

function LinkedList(Node) {
    this.first = Node;
}

function Student(name, accountNumber) {
    this.name = name;
    this.accountNumber = accountNumber;
    this.average = 100;
}

Juan = new Student("Juan", "2010293");
Node = new Node(0, Juan);
List = new LinkedList(Node);