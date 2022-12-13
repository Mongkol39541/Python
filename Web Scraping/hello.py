from bs4 import BeautifulSoup
import requests

destination = requests.get("https://www.it.kmitl.ac.th/th/program/datasci-program/datasci-subjects/")
soup = BeautifulSoup(destination.content, 'html.parser')
data = soup.find_all({"td" : ""})

for txt in data:
    print(txt.text)