function Node(value) {
    this.value = value;
    this.right = null;
    this.left = null
}

function BST() {
    this.root = null;
    this.add = BSTAdd;
    this.addInner = BSTAddInner;
    this.search = BSTSearch;
    this.searchInner = BSTSearchInner;
    this.minimum = BSTSearchMinimum;
    this.minimumInner = BSTSearchMinimumInner;
    this.maximum = BSTSearchMaximum;
    this.maximumInner = BSTSearchMaximumInner;
    this.printBST = BSTPrintGroup;
}

function BSTAdd(value) {
    return this.addInner(value, this.root);
}

function BSTAddInner(value, current) {

    if (!this.root) {
        this.root = new Node(value);
        return true;
    } else {
        if (current.value == value) {
            current = new Node(value);
            return true;
        } else {
            if (current.value > value) {
                if (!current.left) {
                    return current.left = new Node(value);
                } else {
                    this.addInner(value, current.left);
                    return true;
                }
            } else {
                if (!current.right) {
                    return current.right = new Node(value);
                } else {
                    this.addInner(value, current.right);
                    return true;
                }
            }
        }
    }
}

function BSTSearch(value) {
    return this.searchInner(value, this.root);
}

function BSTSearchInner(value, current) {
    if (current.value == value) {
        return current.value;
    } else {
        if (current.value > value) {
            if (current.left) {
                return this.searchInner(value, current.left);
            } else {
                if (current.value == value) {
                    return current.value;
                } else {
                    return false;
                }
            }
        } else {
            if (current.right) {
                return this.searchInner(value, current.right);
            } else {
                if (current.value == value) {
                    return current.value;
                } else {
                    return false;
                }
            }
        }
    }


    /*if (!this.root) {
        return false;
    } else {
        if (current.value == value) {
            return true
        } else {
            if (current.value > value) {
                if (!current.left) {
                    return false;
                } else {
                    return this.search(value, current.left);
                }
            } else {
                if (!current.right) {
                    return false;
                } else {
                    return this.search(value, current.right);
                }
            }
        }
    }*/
}

function BSTSearchMinimum() {
    return this.minimumInner(this.root)
}

function BSTSearchMinimumInner(current) {
    if (!this.root) {
        return false;
    } else {
        if (!current.left) {
            return current.value;
        } else {
            return this.minimumInner(current.left);
        }
    }
}

function BSTSearchMaximum() {
    return this.maximumInner(this.root);
}

function BSTSearchMaximumInner(current) {
    if (!this.root) {
        return false;
    } else {
        if (!current.right) {
            return current.value;
        } else {
            return this.maximumInner(current.right)
        }
    }
}

function BSTPrintGroup(current = this.root) {
    if (current.left || current.right) {
        console.group(current.value);
        if (current.left) {
            this.printBST(current.left);
        }
        if (current.right) {
            this.printBST(current.right);
        }
        console.groupEnd();
    } else {
        console.log(current.value);
    }
}