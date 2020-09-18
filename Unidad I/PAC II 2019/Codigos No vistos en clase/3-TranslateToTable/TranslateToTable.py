#-*- coding:utf8 -*-
class FileToTable:
    def __init__(self, type):
        self.type = type

    def fileToArray(self, filename):
        solution = []
        token = " "

        f = open(filename, "r")
        content = f.read()
        f.close()

        if (self.type is "csv"):
            token = ","

        elif (self.type is "tsv"):
            token = "   "
        
        else:
            print ("E: Terminación de archivo no identificado.")

        rows = content.split("\n")
        
        for row in rows:
            column = row.split(token)
            solution.append(column)

        return solution

    def toTable(self, array):
        table = []
        html = '<table border="1">'
        table.append(html)
        for i in range(len(array)-1):
            html = ('%s<tr>' % ("\t"))
            table.append(html)
            for j in range(len(array[i])):
                if (len(array[i]) == 2 and j ==1):
                    html = ('%s%s<td colspan = "2">%s</td>' %("\t","\t",array[i][j]))
                    table.append(html)
                else:    
                    html = ('%s%s<td>%s</td>' %("\t","\t",array[i][j]))
                    table.append(html)
            html = ('%s</tr>' % ("\t"))
            table.append(html)
        
        html = '</table>'
        table.append(html)
        table = "\n".join(table)
        file = open("table.txt", "w")
        file.write(table)
        file.close()
        return table
        print(table)

    

csv = FileToTable("csv")
tsv = FileToTable("tsv")
content = csv.fileToArray("archivo.csv")
csv.toTable(content)
