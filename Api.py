import requests
# Requête pour obtenir la dernière position de la station ISS depuis L'API OpenNotify
# On ajoute après l'adresse de l'API un point d'accès 
# ou endpoint qui donne accès à des informations (ici iss-now.json --› latitude et longitude de la station)
# les request sont de quatres types GET POST PUT Delete
response = requests.get ("http://api.open-notify.org/iss-now.json") 
#status_code est un objet de la biblio
status_cod = response.status_code
print(status_cod)

# retourne plus d'information du request
Json = response.content
print(Json)

#dumps -- prend en entree un objet Python et retourne une chaine de caracteres comme str
import json
sports = ["tennis","foot","trisathlon"]
ste = str(sports)
sports_string = json.dumps(sports)
print(sports_string)
print(type(ste))
print(type(sports_string))
print(type(sports))

#loads prend en entree une chaine de caracteres JSON et retourne un objet Python
sports2 = json.loads(sports_string)
print(type(sports2))

#EX transformer la dict et str ou/et en dict
sports_number = {
"Football": 1962241,
"Tennis": 1039337,
"Equitation": 663194,
"Basketball": 641367
}

print("exercice")
test = json.dumps(sports_number)
print(type(test))
test = json.loads(test)
print(type(test))



#obtenir un objet Python sous pour convertir en JSON
parametres = {'lat':48.87, 'lon':2.33}
response = requests.get ("http://api.open-notify.org/iss-now.json", params=parametres) 
json_data = response.json()
print(type(json_data))
print(json_data)

#dans le dict recuper une la premiere valeur d'un tableau
first_response = json_data['iss_position']["latitude"]
print(first_response)

# Extraction des Meta donneees avec headers
print(response.headers)

content_type = response.headers['Content-Type']
print(content_type)

print(json_data)

repos = requests.get('http://api.open-notify.org/astros.json')
data = repos.json()
print(data)
numbre = data['number']
print(numbre)

# scraping sur Github en API avec une clef tockens
# donner un token
headers = {"Authorisation":"token jj"}
response = requests.get("http://api.github.com/users/huandu", headers = headers)
print(response.json())

#pour une organisation facebook
headers = {"Authorisation":"token h"}
response = requests.get("http://api.github.com/orgs/facebook", headers = headers)
print(response.json())

# Pour Hello-World respot
headers = {"Authorisation":"token dhjds"}
response = requests.get("http://api.github.com/repos/octocat/Hello-World", headers = headers)
print(response.json())

# pagination fait de recuperer sur un repot une page choisi
# params = {"per_page":50, "page":1}
# response = requests.get("https://api.gethub.com/users/rakeshukla53/starred",  headers=headers, params=params)
# print(response.json())

#request POST
payload = {"name":"api-scraping"}
response = requests.post("https://api.github.com/user/repos", json=payload, headers = headers)
status = response.status_code
print(status)

#PATCH PUT
payload = {"name": "api","description": "Super formation!"}
response = requests.patch ("https://api.github.com/Youssefboulahia1999/repos/api-scraping", json=payload, headers=headers)
status = response.status_code
print (status)

# DELETE
# response = requests. delete("https://api.github.com/repos/codelikerod/api",
# headers=headers)
# status = response.status_code
# print(status)

