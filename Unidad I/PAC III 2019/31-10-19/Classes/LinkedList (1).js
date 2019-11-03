function LinkedList(){
    this.first = null;
    this.push = LinkedListPush;
    this.pop = LinkedListPop;
    this.print = LinkedListPrint;
    this.lenght = LinkedListLenght;
    //this.combine = LinkedListCombine;
    //this.order = LinkedListOrder;
}

    function LinkedListPush(value){
        if(!this.first){
            this.first = new Node(value);
            return true;
        }else{
           current = this.first;
           while(current.next){
               current = current.next;
           }
           current.next = new Node(value);
           return true;
        }
    }
    
    function LinkedListPop(pos = 0){
        if(pos>-1){
            if (pos == 0 && this.first){
                    current = this.first;
                    this.first = this.first.next;
                    return current;
                }
            }else if (this.first ){
                count = 1;
                prevLast = this.first;
                last = this.first.next;
                while(last){
                    if(count == pos){
                        prevLast.next = last.next; //Aquí se borra el last
                        return last;
                    }
                    prevLast = last;
                    last = last.next;
                    count++;
            
                }
                return false;
            
        }else{
            return false;
        }
    }

    function LinkedListPrint(){
        lista = "";
        current = this.first;
        while(current){
            lista += current.value.brand;
            lista += "-->";
            current = current.next;
        }
        lista += "null";
        return lista;
        
    }

    function LinkedListLenght(){
        if(!this.first){
            return 0;
        }else{
            count = 1;
            current = this.first;
            while(current.next){
                current = current.next;
                count++;
            }
            return count;
        }
    }
