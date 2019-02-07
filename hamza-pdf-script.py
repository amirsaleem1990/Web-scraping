url = "http://www.progressivephonics.com/alphabet/alphabet-books-menu/third-book-set"
import requests
import os
from bs4 import BeautifulSoup
soup = BeautifulSoup(requests.get(url).text, "lxml")
a = soup.find("div", {"class" : "yjsg-leadingarticles"})
for i in list(set([i for i in [i['href'] for i in a.find_all('a', href=True)] if i.endswith(".pdf")])):
	os.system("wget " + i)