import requests
from bs4 import BeautifulSoup

# Récupérer le contenu de la page web
response = requests.get('https://youssefboulahia1999.github.io/projet2/')
content = response.content

# Utiliser BeautifulSoup pour analyser le contenu HTML
parser = BeautifulSoup(content, "html.parser")

# Récupérer le contenu du premier paragraphe <p>
body = parser.body
p = body.p
print(p.text)

# Récupérer le titre dans la balise <title> dans <head>
head = parser.head
title = head.title
print(title.text)

# Trouver tous les éléments <body>
body_elements = parser.find_all("body")

# Trouver tous les éléments <p> dans <body>
p_elements = body_elements[0].find_all("p")
print(p_elements[0].text)

# Récupérer le titre de la page depuis <head>
headr = parser.find_all('head')
titler = headr[0].find_all('title')
print(titler[0].text)

# Récupérer le premier paragraphe avec l'id "first"
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

# Récupérer le second paragraphe avec l'id "second"
second_paragraph = parser.find_all("p", id="second")[0]
print(second_paragraph.text)

# Récupérer le premier paragraphe avec la classe "class1"
first_class = parser.find_all("p", class_="class1")[0]
print(first_class.text)

# Sélectionner tous les éléments de la classe "first-item"
first_items = parser.select(".first-item")
print(first_items[0].text)

# Sélectionner le texte de la première balise avec la classe "class2"
first_class2_text = parser.select(".class2")[0].text
print(first_class2_text)

# Sélectionner le texte du paragraphe avec l'id "second"
second_text = parser.select("#second")[0].text
print(second_text)

# Trouver le nombre de fautes de Chelsea
offences = parser.select("#fautes")[0]
chelsea_offences = offences.select("td")[11]
chelsea_offences_count = chelsea_offences.text
print(chelsea_offences_count)

# Trouver le nombre de passes de PSG
psg_pass_count = parser.select("#passes")[0].select("td")[2].text
print(psg_pass_count)
