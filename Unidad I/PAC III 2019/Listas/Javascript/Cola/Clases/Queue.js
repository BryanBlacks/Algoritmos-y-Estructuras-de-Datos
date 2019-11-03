
function Queue(){
    this.first = null;
    this.push = QueuePush;
    this.pop = QueuePop;
    this.print = QueuePrint;
}

    function QueuePush(value){
        
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

    function QueuePop(n=0){

        if (this.first){
            
            if(n>-1){

                if(n==0){
                    current = this.first;
                    this.first = current.next;
                    return current.value.val;

                }else{
                    count = 1;
                    prev = this.first;
                    last = prev.next;
                    while(last){
                        if(count == n){
                            prev.next = last.next;
                            return last.value.val;
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

    function QueuePrint(){
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