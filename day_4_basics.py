from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
# print(tbody.prettify())
#Tree Navigation
trs = tbody.contents 

# #tree siblings
print(trs)  # contents, children
print(trs[0].next_sibling)  # next_sibling
print(trs[1].previous_sibling) #previous_sibling
print(list(trs[0].next_siblings)) #print list of rows after 1st

#Tree parents and Descendants
print(trs[0].parent) #parent
print(trs[0].parent.name) #parent_name
print(trs[0].descendants) #gives everything that comes after or inside this tag
print(list(trs[0].descendants)) #list of all descendants
print(trs[0].children) #gives tags that are inside of that tag