function Stack() {
    this.last = null;
    this.push = StackPush;
    this.print = StackPrint;
    this.pop = StackPop;
}

function StackPush(value) {
    if (!this.last) {
        this.last = new Node(value);
        return true;
    } else {
        prev = this.last;
        this.last = new Node(value);
        this.last.prev = prev;
        return true;
    }
}

function StackPrint() {
    stack = "\n";
    current = this.last;
    while (current) {
        stack += current.value.taste;
        stack += "\n";
        current = current.prev;
    }
    return stack;
}

function StackPop() {
    if (!this.last) {
        return false;
    } else {
        if (!this.last.prev) {
            temp = this.last;
            this.last = null;
            return temp.value.taste;
        } else {
            current = this.last;
            this.last = current.prev;
            return current.value.taste;
        }
    }
    return false;
}