"""
L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon.
"""

from requests import *
from bs4 import *

r = get("https://www.gov.uk/search/news-and-communications")
soup = BeautifulSoup(r.content, "html.parser")

titres = soup.find_all("a", class_="gem-c-document-list__item-title")

ttitres = []
for titres in titres:
    ttitres.append(titres.string)

print(ttitres)