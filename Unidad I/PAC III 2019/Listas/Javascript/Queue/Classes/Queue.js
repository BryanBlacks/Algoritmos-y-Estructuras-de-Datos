function Queue(){
    this.first = null;
    this.add = QueueAdd;
    this.pop = QueuePop;
    this.print = QueuePrint;   
}

    function QueueAdd(value){
        if (!this.first){
            this.first = new Node(value);
            return true;     
        }
        else{
            current = this.first;
            while (current.next){
                current = current.next;
            }
            current.next = new Node(value);
            return true;
        }
    }

    function QueuePop(){
        current = this.first;
        this.first = current.next;
        return current.value;
    }

    function QueuePrint(){
        lista = "";
        current = this.first;
        while(current){
            lista += current.value;
            lista += "-->";
            current = current.next;
        }
        lista += "null";
        return lista;
        
    }
/*
    function QueueAdd(value){
        if (!this.first){
            this.first = value;
            return true;     
        }
        else{
            current = this.first;
            while (current.next){
                current = current.next;
            }
            current.next = value;
            return true;
        }
    }

    function QueuePop(){
        if (!this.first){
            return null;
        }
        else{
            current = this.first;
            this.first = current.next;
            if(current){
                return current.value;
            }
            else{
                current = null;
            }

        }
    }

    function QueuePrint(){
        lista = "";
        current = this.first;
        while(current){
            lista += current.value;
            lista += "-->";
            current = current.next;
        }
        return lista;
        
    }
*/