import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as cs



## this is the video link >>> (https://www.youtube.com/watch?v=XQgXKtPSzUI&t=1620s)

url = requests.get('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card')
soup = BeautifulSoup(url.content,"html.parser")
items = soup.find_all(class_= "item-container")

filename = {"products.csv"}
f = open(filename, "w")
headers = "brand, title, price\n"
f.write(headers)

brand = [item.find(class_= "item-branding").img["title"] for item in items]
title = [item.find(class_="item-title").get_text() for item in items]
price = [item.find(class_="price-current").strong.get_text() for item in items]

f.write(brand + "," + title + "," + price + "\n")
f.close()