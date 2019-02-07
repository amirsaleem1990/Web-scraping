import requests
from bs4 import BeautifulSoup
import os

def scrap(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find("div", { "class" : "col-md-10 col-md-offset-1" }).findAll("div")[1:]    
    soup = BeautifulSoup(html)
    links_only = [a['href'] for a in soup.find_all('a', href=True)]
    books_links_only = [i for i in links_only if str(i).endswith(".pdf")]
    return books_links_only

all_links = []
main_url = "https://freekidsbooks.org/reading-level/children/"

for i in range(2,12):
    temp_url = main_url + "page/{}/".format(i)
    all_links += scrap(temp_url)
with open('urls.txt', 'w') as file:
    file.write('\n'.join(all_links))
os.system("xargs -n 1 curl -O < urls.txt")