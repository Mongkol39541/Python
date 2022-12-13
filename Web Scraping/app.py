import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.xn--h3ct1aayhy3eted5k.com/"
data = requests.get(url)
data = BeautifulSoup(data.text, "html.parser")
title = data.find_all("a", {"class" : "text_body_yellow01"})
number = data.find_all("td", {"class" : "text_body_yellow01", "width" : "21%"})

dict_phone = {"Phone" : [], "Price" : []}

for loop in range(len(title)):
    try:
        phone = title[loop].text.split()[0]
        price = number[loop].text.split()[0]
        dict_phone["Phone"].append(phone)
        dict_phone["Price"].append(price)
    except:
        pass

dict_phone = pd.DataFrame(dict_phone)
print(dict_phone)