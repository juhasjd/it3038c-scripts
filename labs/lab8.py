import requests, re
from bs4 import BeautifulSoup

data  = requests.get("https://www.adidas.com/us/x-speedportal.1-fg/FZ6289.html").content 
soup = BeautifulSoup(data, 'html.parser') 
span = soup.find("h1", {"class":"name___120FN"}) 
title = span.text
span = soup.find("span", {"class":"product-price___2Mip5"}) 
price = span.text
print("Item %s has price %s" % (title, price))