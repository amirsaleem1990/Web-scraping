# url = "https://urbrainy.com/maths/year-1-age-5-6"
# url = "https://urbrainy.com/maths/early-reception-age-4-5/counting-and-matching"
# pdfs = []
# links = []
# links2 = []
links3 = []
import requests
from bs4 import BeautifulSoup
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "lxml")
# for a in soup.find_all('a', href=True):
#     links.append(a['href'])
# print("Links: ", len(links))
# for i in links:
# 	r = requests.get(url)
# 	soup = BeautifulSoup(r.text, "lxml")
# 	for a in soup.find_all('a', href=True):
# 	    links2.append(a['href'])
# print("Links2", len(links2))
with open("/home/amir/new/links.txt", 'r') as file:
	links2 = file.read().splitlines()
c = 0
for i in links2:
	c += 1
	print(c, round((c/len(links2))*100, 5))
	try:
		r = requests.get(i)
		soup = BeautifulSoup(r.text, "lxml")
		for a in soup.find_all('a', href=True):
		    links3.append(a['href'])
	except:
		pass

# with open('~/links1.txt', 'w') as file:
# 	file.write("\n".join([str(i) for i in links]))

# with open('~/links2.txt', 'w') as file:
# 	file.write("\n".join([str(i) for i in links2]))

with open('~/links3.txt', 'w') as file:
	file.write("\n".join([str(i) for i in links3]))

# with open('a.txt', 'r') as file:
# 	links = file.read().splitlines()
# if "downloadButton" in i:
# 		pdfs.append(i)
# for i in pdfs:
# 	print(i)