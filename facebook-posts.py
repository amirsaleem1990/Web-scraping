# 1- go to facebook and log in
# 2- go to page or group or friend you with to scrap
# 3- save that page by press CTRL+S


import requests
from bs4 import BeautifulSoup
path = "/home/amir/Desktop/Zahid-Mughal.html"
page = BeautifulSoup(open(path), "lxml")
a = page.findAll("p")
for i in a:
    print(i.get_text())