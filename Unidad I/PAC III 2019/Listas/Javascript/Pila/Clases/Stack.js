
function Stack(){
    this.first = null;
    this.last = null;
    this.push = StackPush;
    this.add = StackAdd;
    this.pop = StackPop;
    this.print = StackPrint;
}

    function StackPush(value){
        
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

    function StackAdd(value){
        if(!this.last){
            this.last = new Node(value);
        }else{
            current = this.last;
            this.last = new Node(value);
            this.last.next = current;
            return true;
        }
        return false;
    }

    function StackPop(){
        if(!this.first){
            return false;
        }else{
            if(!this.first.next){
                current = this.first;
                this.first = null;
                return current;
            }else{
                prev = this.first;
                last = prev.next;
                while(last.nex){
                    prev = last;
                    last= last.next;
                }
                prev.next = null;
                return last
            }
        }
    }

    function StackPrint(){
        list="";
        if(!this.first)
            return false;
        else{
            current = this.first;
            while(current){
                list = `${list}${current.value.val} --> `;
                current = current.next;
            }
            list = `${list}null`;
            return list; 
        }

        
    }