json = {}

def fromPlainText(self):
            f = open("PRUEBA.txt","r")
            lines = f.readlines()
            l = len(lines)

            
            #print(lines)
            for i in range(l):
                line = lines[i]
                li = len(line)
                n = line.count("\t", 0, li)
                if(n == 0):
                    
                    json = {"%s" % line : []}
                else:
                    if(n == 1):
                        parent = root
                        pa = parent.replace('\n', '')
                        current = lines[i]
                        cu = current.replace('\t', '')
                        cur = cu.replace('\n', '')
                        d = cur.count("/", 0, len(cur))
                        if(d == 1):  
                            Current = cur.replace('/', '')
                            self.add(Current, "D", pa)
                        else: 
                            self.add(cur, "F", pa)
                    else:
                        if(n == 2):
                            parent = cur
                            pa = parent.replace('\t', '')
                            par = pa.replace('\n', '')
                            Parent = par.replace('/', '')
                            new = lines[i]
                            N = new.replace('\t', '')
                            ne = N.replace('\n', '')
                            dd = ne.count("/", 0, len(ne))
                            if(dd == 1):  
                                New = ne.replace('/', '')
                                self.add(New, "D", Parent)
                            else: 
                                self.add(ne, "F", Parent)
                        
            f.close() 
