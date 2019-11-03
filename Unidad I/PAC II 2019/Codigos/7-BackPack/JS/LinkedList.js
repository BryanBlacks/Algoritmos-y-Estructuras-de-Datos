function Node(value) {
    this.value = value;
    this.next = null;
}

function LinkedList() {
    this.first = null;
    this.empty = LinkedListEmpty;
    this.add = LinkedListAdd;
    this.showContent = LinkedListShowContent;
    this.countContent = LinkedListCountContent;
    this.obtainLast = LinkedListObtainLast;
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

function LinkedListShowContent() {
    if (!this.empty()) {
        current = this.first;
        while (current.next) {
            console.log(current.value);
            current = current.next;
        }
        console.log(current.value);
    }
}

function LinkedListCountContent() {
    if (!this.empty()) {
        count = 1;
        current = this.first;
        while (current.next) {
            count++;
            current = current.next;
        }
        console.log("Se han encontrado: ", count, " elementos")
    }
}

function LinkedListObtainLast() {
    last = this.first;
    while (last.next) {
        last = last.next;
    }
    return last;
}