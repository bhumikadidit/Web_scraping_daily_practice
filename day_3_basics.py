from bs4 import BeautifulSoup
import re

with open ("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
#print multiple tags 
tags1 = doc.find_all(["p", "div", "li"])
print(tags1)

#find attribute
tags2 = doc.find_all(["option"], string = "Undergraduate", value ="undergraduate")
print(tags2)

#find class
tags3 = doc.find_all(class_="btn-item")
print(tags3)

#find regular exression model
tags = doc.find_all(string = re.compile("\$.*") )
for tag in tags:
    print(tag.strip())

#find limit
tags4 = doc.find_all(string = re.compile("\$.*"), limit=1)
for tag in tags4:
    print(tag.strip())

#save modifications in the html file]
new_tag = doc.find_all("imput", type ="text" )
for tag in new_tag:
    tag["placeholder"] = "I changed you"

with open("changed.html", "w") as file:
    file.write(str(doc))