#Authentification de l'api reddit
import requests 
import requests.auth
import json

# HTTPBasicAuth est un class de requests.auth 
# elle permet d'effectuer une authentification HTTP basique 
# avec un nom d'utilisateur et un mot de passe
# elle prend donc deux parametre login et MDP
client_auth = requests.auth.HTTPBasicAuth('CGqHlEiCCA','IAngtzhe7o-79v5nuQ')

#ajout des login reddit en dict
post_data = {"grant_type":"password","username":"login","password":"Pass"}
#Ajout de nom a l'identification API
headers ={"User-agent":'Formation API'}
#generation de token avec les information
response = requests.post("https://www.reddit.com/api/v1/access_token",auth=client_auth, data=post_data, headers=headers)


dict_token = response.json()

# print(response.json())
# token = json.dumps(dict_token["access_token"])
token = dict_token.get("access_token")
# print(token)
# print(response.json())

headers = {"Authorization":f"bearer {token}", "User-agent":"Formation API" }
# On ajoute un parametre pour cibler le dernier jour
params = {"t":"day"}
#requete get avec les parametre 
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)


python_top = response.json()
print(python_top)




# import requests

# # Étape 1 : Définir les paramètres pour la requête GET
# # Ici, on veut récupérer les posts du dernier jour du subreddit 'python'
# params = {"t": "day"}

# # Étape 2 : Faire une requête GET pour récupérer des posts du subreddit Python
# # Cette requête utilise les paramètres et les en-têtes que l'on a définis
# response = requests.get(
#     "https://oauth.reddit.com/r/python/top",  # L'URL de l'API Reddit pour les posts
#     headers=headers,  # En-têtes nécessaires pour s'authentifier
#     params=params     # Paramètres qui spécifient qu'on veut les posts du dernier jour
# )

# # Vérifier si la requête a réussi (code HTTP 200 signifie succès)
# if response.status_code == 200:
#     # Si la requête réussit, récupérer les données en format JSON
#     python_top = response.json()
#     print("✅ Données du subreddit récupérées avec succès.")
#     print(python_top)  # Afficher les données récupérées
# else:
#     # Si la requête échoue, afficher un message d'erreur avec le code d'erreur
#     print(f"❌ Erreur lors de la récupération des posts : {response.status_code}")
#     print(response.json())  # Afficher le détail de l'erreur

# # Étape 3 : Si nécessaire, récupérer un token d'accès (ici, pour récupérer le token)
# # Vérifier si la réponse est correcte (code HTTP 200)
# if response.status_code == 200:
#     # Récupérer la réponse JSON et extraire le token
#     dict_token = response.json()
#     token = dict_token.get("access_token")  # Obtenir le token d'accès depuis la réponse
#     print("✅ Token récupéré avec succès.")
# else:
#     # Si la récupération du token échoue, afficher l'erreur
#     print(f"❌ Erreur lors de la récupération du token : {response.status_code}")
#     print(response.json())  # Afficher le détail de l'erreur
#     exit()  # Quitter le programme si une erreur survient





#recuperer l'id du reddit le plus populaire
python_top_articles = python_top['data']['children']
most_upvoted = ""
most_upvotes = 0

for article in python_top_articles:
    ar = article['data']
#ups sont les vote les plus populaire
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]
print(most_upvotes)
print(most_upvoted)

#reccuperer tous les commentaires du poste
reponse = requests.get("https://oauth.reddit.com/r/python/comments/1hmlsys", headers=headers)
comments = reponse.json()
print(comments)

#reccuperer le commentaire le plus populaire
comments_list = comments [1]['data']['children']
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment['data']
    if co["ups"] >= most_upvotes_comment:
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]
print(most_upvoted_comment)
print(most_upvotes_comment)