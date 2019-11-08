#-*- coding:utf8 -*-
from Nucleo.Lista.Node import *

class LinkedList:
    def __init__(self):
        self.first = None
    

    def push(self, value ):
        if (not self.first):
            self.first = Node(value)
            return True
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True

        return False

    def printQueue(self):
        current = self.first
        while(current.next):
            print(current.value.name)
            current = current.next
        print(current.value.name)

    def pop(self,poss):
        if (not self.first):
            return False
        else:
            if (pos >-1):
                if(pos==0):
                    current = self.first
                    self.first = current.next
                    return True
                else:
                    count = 1
                    prev = self.first
                    last = prev.next
                    while(last):
                        if(count == pos):
                            prev.next = last.next
                            return True
                        prev = last
                        last = last.next
                        count = count+1
            else:
                return False

    def search(self,pos=0):
        if(pos==0):
            return self.first.value
        else:
            count=1
            prev = self.first
            last = prev.next
            while(last):
                if(pos == count):
                    return last.value             
                last = last.next
                count= count+1
            
            return False


    def length(self):
        if(not self.first):
            return 0
        else:
            len = 1
            current = self.first
            while(current.next):
                len = len+1
                current = current.next
            return len


    def generateTable(self):
        count = 1
        current = self.first
        name, cost, desc = "Nombre","Costo","Descripción"
        table=[]
        row=[]
        j,w,q = 0,0,0

        table.append("%s%s%s%s%s%s"%("-"*120,"\n","\t"*6,"Inventario de Productos","\n","-"*120))

        for k in range(120):
            if k<6:
                if k==0:
                    row.append("N.")
                else:
                    row.append(" ")
            else:
                if k<36:
                    if k==6:
                        row.append("| ")
                    else:
                        tam = len(name)
                        if(j<tam):
                            row.append(name[j])
                            j = j+1
                        else: 
                            row.append(" ")
                else:
                    if k<51:
                        if k==36:
                            row.append("|")
                        else:
                            tam = len(cost)
                            if(w<tam):
                                row.append(cost[w])
                                w = w+1
                            else: 
                                row.append(" ")
                    else:
                        if k<120:
                            if k==51:
                                row.append("| ")
                            else:
                                tam = len(desc)
                                if(q<tam):
                                    row.append(desc[q])
                                    q = q+1
                                else: 
                                    row.append(" ")
        
        table.append("".join(row))
        table.append("-"*120)
        table.append(self.genList())

        return "\n".join(table)



    def genList(self):
        count = 0
        current = self.first
        
        table1=[]

        while(current):
            k,j,w,q,c = 0,0,0,0,0
            cont=[]
            obj = current.value
            for i in range(120):
                if(i<6):
                    if i==0:
                        cont.append(str(count))
                    else: 
                        cont.append(" ")

                else:
                    if(i<36):
                        #j = 0
                        if i==6:
                            cont.append("| ")
                        else: 
                            tam = len(obj.name)
                            if(j<tam):
                                cont.append(obj.name[j])
                                j = j+1
                            else: 
                                cont.append(" ")
                    else:
                        if(i<51):
                            #w = 0
                            if i==36:
                                cont.append("| ")
                            else:
                                if i<40:
                                    tam = len(obj.coin)
                                    if(c<tam):
                                        cont.append(obj.coin[c])
                                        c = c+1
                                else:
                                    tam = len(obj.cost)
                                    if(w<tam):
                                        cont.append(obj.cost[w])
                                        w = w+1
                                    else:
                                        cont.append(" ")
                        else:
                            if(i<120):
                                #q = 0
                                if i==51:
                                    cont.append("| ")
                                else:       
                                    tam = len(obj.description)
                                    if(q<tam):
                                        cont.append(obj.description[q])
                                        q = q+1
                                    else:
                                        cont.append(" ")

            txt = "".join(cont)
            table1.append(txt)
            if(current.next):
                table1.append("-"*120)
            
            current = current.next
            count = count+1
        
        return "\n".join(table1)

    