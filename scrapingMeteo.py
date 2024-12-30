import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup (page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
today = forecast_items[0]
print (today.prettify())

period = today.find(class_="period-name") .get_text()
short_desc = today.find(class_ ="short-desc").get_text()
# temp = today.find(class_="temp").get_text()

print(period)
print (short_desc)
# print(temp)

img = today.find("img")
source = img['src'] # img est un dict

print(source)

#Tous les elements 
period_tags = seven_day.select(" .tombstone-container .period-name")
# On parcourt tous les éléments de period tags et pour chaque élément on applique la méthode get text ()
# On obtient une liste
periods = [pt.get_text () for pt in period_tags]
print(periods)



# Utilise select() de BeautifulSoup pour sélectionner tous les éléments HTML qui 
# ont la classe .short-desc à l'intérieur d'un conteneur avec la classe .tombstone-container.
# Cela retourne une liste d'éléments HTML correspondant aux descriptions courtes.
# [sd.get_text() for sd in ...]
# Parcourt chaque élément HTML (sd) retourné par select.
# Utilise la méthode get_text() pour extraire uniquement le texte à l'intérieur de chaque élément HTML.
short_descs = [sd.get_text() for sd in seven_day.select (".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select (" .tombstone-container .temp")]
descs = [img['title'] for img in seven_day.select(".tombstone-container img") if img.has_attr('title')]

print(short_descs)
print(temps)
print(descs)



short_descs.remove('High Surf Advisory')


print(len(periods))
print(len(short_descs))
print(len(temps))
print(len(descs))



import pandas as pd
weather = pd.DataFrame({ 
    # "period": periods,
    "short_desc": short_desc,
    "temps": temps,
    "descs": descs
})
print(weather)


