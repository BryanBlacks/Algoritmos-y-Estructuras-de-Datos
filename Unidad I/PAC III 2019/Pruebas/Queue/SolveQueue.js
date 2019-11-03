function Node(value) {
    this.value = value;
    this.next = null;
}

function Queue() {
    this.first = null;
    this.add = QueueAdd;
    //this.print = QueuePrint;
    this.search = QueueSearch;
}

function QueueAdd(value) {
    if (!this.first) {
        this.first = new Node(value);
        return true;
    } else {
        current = this.first;
        while (current.next) {
            current = current.next;
        }
        current.next = new Node(value);
        return true;
    }
}

function QueueSearch(value) {
    if (this.first.value == value) {
        return this.first.value;
    } else {
        current = this.first;
        while (current.next) {
            if (current.value == value) {
                return current.value;
            } else {
                current = current.next;
            }
        }
        if (current.value == value) {
            return current.value;
        } else {
            return null;
        }
    }
}