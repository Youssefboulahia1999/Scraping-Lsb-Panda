from requests import get

url = ' https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,asc'
response = get(url)
# lien de chaque site : http://www.imdb.com/search/title?release_date=2017&sort=num_votes, debc&page=1
# lien de chaque site : https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,asc
print(response.text[:500])

# import requests

# url = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,asc'

# session = requests.Session()
# session.headers.update({
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# })

# response = session.get(url)

# if response.status_code == 200:
#     print(response.text[:500])
# else:
#     print(f"Erreur {response.status_code}: Accès refusé.")

# from bs4 import BeautifulSoup
# html_soup = BeautifulSoup(response.text, 'html.parser')
# type (html_soup)

# movie_containers = html_soup.find_all('div', class_="lister-item mode-advanced")
# print(type(movie_containers))
# print(len(movie_containers))

# first_movie = movie_containers[0]
# print(first_movie)



#fonction time pour ne pas surcharger le serveur
years_url = [str(1) for i in range(1,5)]

from time import sleep 
from time import time 
from random import randint
from IPython.display import clear_output
#pour afficher les message erreur
from warnings import warn

requests = 0

for a in range(0,5):
    print('booh')
    sleep(randint(1,4))

start_time = time()
for _ in range(5):
    requests += 1
    sleep(randint(1,3))
    elapsed_time = time() - start_time
    print('Request: Frequency: {} requests/s'.format(requests,requests/elapsed_time))
    clear_output(wait = True)
warn('Attention')
print(warn('Attention'))