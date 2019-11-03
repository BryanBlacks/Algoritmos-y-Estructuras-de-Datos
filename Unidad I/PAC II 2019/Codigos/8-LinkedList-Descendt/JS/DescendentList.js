function Node(value) {
    this.next = null;
    this.value = value;
}

function LinkedList(value) {
    this.first = null;
    this.add = LinkedListAdd;
    this.print = LinkedListPrint;

}

function LinkedListAdd(item) {
    if (!this.first) {
        this.first = new Node(item)
        return true;
    } else {
        if (this.first.value <= item) {
            stack = this.first;
            this.first = new Node(item);
            this.first.next = stack;
        } else {

            prev = this.first;
            current = prev.next;
            while (current) {
                if (current.value <= item) {
                    prev.next = new Node(item);
                    prev.next.next = current;
                    return true;
                }

                prev = current;
                current = prev.next;
            }
            prev.next = new Node(item);
            return true;
        }

    }
    return false;
}

function LinkedListPrint() {
    current = list.first;
    while (current.next) {
        console.log(current.value);
        current = current.next;
    }
    console.log(current.value);
}