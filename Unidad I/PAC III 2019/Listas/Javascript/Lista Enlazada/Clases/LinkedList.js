function LinkedList(){
    this.first = null;
    this.push = LinkedListPush;
    this.pop = LinkedListPop;
    this.print = LinkedListPrint;
    //this.length = LinkedListLength;
    //this.search = LinkedListSearch;
    
}
    
    function LinkedListPush(value,pos){
        if(!this.first){
            this.first = new Node(value);
            return true;
        }else{
            if(pos == null){
                current = this.first;
                while(current.next){
                    current = current.next;
                }
                current.next = new Node (value);
                return true;
            }else{
                if(pos>-1){
                    if(pos==0){
                        current = this.first;
                        this.first = new Node(value);
                        this.first.next = current;
                        return true;
                    }else{
                        c=1;
                        prev = this.first;
                        last = prev.next;
                        while(last){
                            if(c==pos){
                                prev.next = new Node(value);
                                prev.next.next = last;
                                return true;
                            }
                            prev = last;
                            last = last.next;
                            c++;
                        }
                        return false;
                    }
                }
            }

        }
    }
    
    function LinkedListPop(n=0){

        if (this.first){
            
            if(n>-1){

                if(n==0){
                    current = this.first;
                    this.first = current.next;
                    return current.value;

                }else{
                    count = 1;
                    prev = this.first;
                    last = prev.next;
                    while(last){
                        if(count == n){
                            prev.next = last.next;
                            return last.value;
                        }
                        prev = last;
                        last = last.next;
                        count++;
                    }
                    return false;
                }

            }else{
                return false;
            } 

        }else{
            return false;
        }
        
    }

    function LinkedListPrint(){
        list="";
        if(!this.first)
            return false;
        else{
            current = this.first;
            while(current){
                list = `${list}${current.value} --> `;
                current = current.next;
            }
            list = `${list}null`;
            return list; 
        }

        
    }