function Stack() {
    this.first = null;
    this.push = StackPush;
    this.pop = StackPop;
    this.print = StackPrint;
}

function StackPush(value) {
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

function StackPop() {
    if (!this.first) {
        return false;
    } else {
        if (!this.first.next) {
            current = this.first;
            this.first = null;
            return current;
        } else {
            prevLast = this.first;
            last = this.first.next;

            while (last.next) {
                prevLast = last;
                last = last.next;
            }
            prevLast.next = null;
            return last;
        }
    }
}

function StackPrint() {
    lista = "";
    current = this.first;
    while (current) {
        lista += current.value.brand;
        lista += "-->";
        current = current.next;
    }
    lista += "null";
    return lista;

}