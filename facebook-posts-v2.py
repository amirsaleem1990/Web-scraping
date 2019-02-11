file = "Noman Khalid-2.html"
f = open(file, "r")
r = f.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(r, "html.parser")
a = soup.find("div", {"id" : "timeline_story_container_683995890"})
mm = []
for i in a:
    try:
        mm.append(i.find("span", class_="_4arz").get_text())
    except:
        pass

final = []
for i in mm:
    if i.isnumeric():
        final.append(int(i))
    else:
        temp = i.split()
        ab = [int(i) for i in temp if i.isnumeric()]
        if ab:
            final.append(i.count(",")+1 + ab[0])
        else:
            final.append(1)

with open('total_likes.txt', "w") as file:
    file.write("\n".join([str(i) for i in final]))
