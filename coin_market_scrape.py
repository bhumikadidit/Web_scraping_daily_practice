from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4] #prints only name and price
    fixed_name = name.p.string
    fixed_price = price.span.string

    prices[fixed_name] = fixed_price

print(prices)


# for tr in trs[10:]:
#     name,price = tr.contents[2:4] #pritns only name and price
#     fixed_name = name.span.string
#     fixed_price = price.span.string
#     prices[fixed_name] = fixed_price

# print(prices)




