import requests

#le requests peut aussi extrair des page web
response = requests.get('https://youssefboulahia1999.github.io/projet2/')
content = response.content
# print(content)

#utilise la librairie beaurifulsoup du pack bs4 pour recuperer un element
from bs4 import BeautifulSoup
#le parser recupere tous le code
parser = BeautifulSoup(content,"html.parser")
#body prend le body du code html
body = parser.body

# recuperer le p de chaque body
p = body.p
#sous le .text il recuper le paragraphe avec la balise <p>
print(p.text)

#dans le head on recupere le title
head = parser.head
title = head.title
print(title.text)

parser = BeautifulSoup(content, 'html.parser')

#obtenir tous les elements de la balise body c'est une liste
body = parser.find_all("body")

# Tous les elements de la balise <p>
p = body[0].find_all("p")

print(p[0].text)

headr = parser.find_all('head')
titler =headr[0].find_all('title')
print(titler.text)

#on recupere l'id firt du paragraphe p
firt_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

second_paragraph = parser.find_all("p", id="second")[0]
print(second_paragraph.text)

#Pour le class
first_class = parser.find_all("p",class_="class1")[0]
print(first_class.text)

# Sélectionner tous les élements de la classe first-item
first items = parser.select(".first-item")
print(first_items[0].text)

first class2 text = parser.select(".class2")[0].text
print(first class2 text)

second text = parser.select("#second")[0].text
print (second text)


# Trouver Le nombre de fautes de Chelsea
offences = parser.select("#fautes")[0]
chelsea offences = offences.select ("td")[11]
chelsea_offences_count = chelsea_offences.text

print(chelsea offences count)

psg_pass_count = parser.select("#passes")[0].select ("td") [2].text
print(psg_pass_count)