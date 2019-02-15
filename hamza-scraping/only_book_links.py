with open("second-stage-links.txt", "r") as file:
    links = file.read().splitlines()
import requests
from bs4 import BeautifulSoup
d = "resource-title"
book_links = []
c = 0
for i in links[850:]:
	c = c + 1
	print("Ho gay: ", c, "\tLinks_ok: ", len(book_links), "\t %:", round((c) / (len(links))*100, 5))
	try:
		b = BeautifulSoup(requests.get(i).text, "lxml")
		if d in str(b):
			book_links.append(i)
			with open('only_pdf_books_links.txt', 'a') as f:
				f.write(i + "\n")
	except:
		pass
try:
	with open("only_book_links.txt", "w") as file:
		file.write("\n".join([str(i) for i in book_links]))

	import pickle
	with open("only_book_links.pkl", "wb") as file:
		pickle.dump(book_links, file)

except:
	for i in book_links:
		print(i)