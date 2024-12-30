# Projet Python : Exercices Divers

Ce projet contient plusieurs exercices Python qui couvrent différents concepts, tels que les jeux de mots, la manipulation de données JSON, l'écriture de fichiers CSV, ainsi que l'interaction avec des APIs externes.

## Exercice 1 : Jeu de mots

Le joueur doit deviner un mot lettre par lettre. Il a un nombre limité de chances avant que le jeu ne soit terminé. Des erreurs dans les lettres non présentes dans le mot feront perdre des chances. Ce jeu permet de pratiquer la gestion des entrées utilisateur et la logique conditionnelle.

### Fonctionnalités :
- Deviner un mot en plusieurs tentatives.
- Un nombre limité d'essais avant de perdre.
- Perdre des chances lorsque des lettres incorrectes sont proposées.

---

## Exercice 2 : Manipulation des produits JSON

Cet exercice montre comment récupérer des données JSON à partir d'une API externe, les transformer et les imprimer au format base64. Il inclut également la génération de mots de passe sécurisés et d'UUID pour chaque produit.

### Fonctionnalités :
- Récupérer des données JSON depuis une API.
- Convertir et imprimer les données en base64.
- Générer des mots de passe sécurisés et des UUID uniques pour chaque produit.

---

## Exercice 3 : Écriture dans un fichier CSV

Les données des produits récupérées sont écrites dans un fichier CSV local. Cela permet de pratiquer l'utilisation des fichiers CSV pour stocker des données structurées.

### Fonctionnalités :
- Récupérer des données.
- Sauvegarder ces données dans un fichier CSV local.

---

## Installation

### Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir Python 3 installé. Vous aurez également besoin des bibliothèques suivantes :

- `requests` pour interagir avec l'API JSON.
- `uuid`, `random`, `string`, `hashlib` pour la génération de mots de passe et de hachages.
- `pathlib` pour la gestion des chemins de fichiers.
- `csv` pour la gestion des fichiers CSV.

Vous pouvez installer ces bibliothèques via pip si elles ne sont pas déjà installées :
```
pip install requests
```


## Api.py exemple d'API - API Requests et Manipulation de JSON

Ce projet montre comment interagir avec différentes APIs publiques en Python, y compris la récupération de données JSON depuis une API externe et leur manipulation.

Authentification avec l'API Reddit

Ce projet montre comment interagir avec l'API Reddit pour récupérer les posts populaires dans le subreddit Python. Il inclut également la récupération des commentaires associés et l'extraction du post et du commentaire les plus populaires. L'authentification est effectuée en utilisant OAuth2 via un token d'accès.

Fonctionnalités :
Authentification OAuth2.
Récupérer les posts populaires dans un subreddit.
Extraire les commentaires associés aux posts populaires.


## Lsb.py Stéganographie avec Python

Ce projet utilise la stéganographie pour cacher un message secret dans une image en manipulant les bits de poids faible (LSB) des composantes RGB de chaque pixel. Vous pouvez ensuite récupérer ce message à partir de l'image.

Prérequis :
Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

Python (version 3.x recommandée)
Pillow (bibliothèque pour la manipulation d'images en Python)
Installez Pillow via pip :
``` pip install pillow```

Commandes pour exécuter le code :
Pour cacher un message dans une image :
```` python lsb.py write <chemin_vers_l_image_en_entree> <message_secret_a_ecrire>````

Pour lire un message caché dans une image :
``` python lsb.py read <chemin_vers_l_image_en_entree>```

## Scraping.py Web Scraping avec BeautifulSoup et Requests

Ce projet Python utilise les bibliothèques requests et BeautifulSoup pour récupérer et analyser le contenu d'une page web. Il permet d'extraire des informations comme les titres, les paragraphes, les éléments avec des identifiants ou des classes spécifiques, et d'autres contenus HTML.

Prérequis :
Avant de commencer, assurez-vous que vous avez installé les dépendances suivantes :

Python 3.x
requests : Pour envoyer des requêtes HTTP.
BeautifulSoup (via bs4) : Pour analyser le contenu HTML.
Installez les dépendances à l'aide de pip : 
``` pip install requests beautifulsoup4```

Contribution


