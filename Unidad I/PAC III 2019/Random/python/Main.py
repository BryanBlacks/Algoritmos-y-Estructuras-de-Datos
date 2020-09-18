from Paragraph import*
from Random import*

paragraph = Paragraph()
rand = Randomx()

tam = rand.generator(5,2)
text = []

for i in range(tam):
    text.append(paragraph.create())

print("\n\n".join(text))


#escribir en html con python
"""
text = "%s%s%s" % ("<p>", "</p><p>".join(text),"</p>")

html = "%s%s%s%s%s" % ("<script>\n","text = '",text,"';\ndocument.write(text);\n","</script>")

f = open("main.html","w")
f.write(html)
f.close()
"""