1exercice.py. **Jeu de mots :** 
   - Le joueur doit deviner un mot lettre par lettre.
   - Il a un nombre limité de chances avant que le jeu ne soit terminé.
   - Des erreurs dans les lettres non présentes dans le mot font perdre des chances.
   
2exercice.py. **Manipulation des produits JSON :**
   - Récupère des données JSON à partir d'une API externe.
   - Transforme et imprime les données au format base64.
   - Génére des mots de passe sécurisés et des UUID pour chaque produit.
   
3exercice.py. **Écriture dans un fichier CSV :**
   - Les données des produits récupérés sont écrites dans un fichier CSV local.

## Installation

### Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir Python 3 installé. Vous aurez également besoin des bibliothèques suivantes :
- `requests` pour interagir avec l'API JSON.
- `uuid`, `random`, `string`, `hashlib` pour la génération de mots de passe et de hachages.
- `pathlib` pour la gestion des chemins de fichiers.
- `csv` pour la gestion des fichiers CSV.

Vous pouvez installer ces bibliothèques via pip si elles ne sont pas déjà installées :

```bash
pip install requests




#Api.py **API Requests and JSON Handling in Python**

Ce projet démontre l'utilisation de la bibliothèque Python `requests` pour interagir avec différentes APIs publiques, ainsi que la manipulation de données JSON. Vous y trouverez des exemples de requêtes HTTP pour récupérer des informations sur la Station Spatiale Internationale (ISS), interagir avec l'API GitHub et effectuer diverses opérations sur des données JSON.

**# Auth_reddit.py Reddit API Authentication and Data Extraction**

Ce projet montre comment interagir avec l'API Reddit pour récupérer des posts populaires dans le subreddit Python, récupérer des commentaires associés, et extraire le post et le commentaire les plus populaires. L'authentification est effectuée en utilisant OAuth2 via un token d'accès.

## Table des Matières

- [Installation](#installation)
- [Authentification Reddit API](#authentification-reddit-api)
- [Récupérer les posts populaires](#récupérer-les-posts-populaires)
- [Récupérer les commentaires populaires](#récupérer-les-commentaires-populaires)
- [Dépendances](#dépendances)
- [Contribution](#contribution)






# Stéganographie avec Python

Ce projet permet de cacher un message secret dans une image en utilisant la technique de la stéganographie par les bits de poids faible (LSB) des composantes RGB de chaque pixel. Le message peut être récupéré à partir de l'image une fois qu'il a été caché.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

- **Python** (version 3.x recommandée)
- **Pillow** (bibliothèque d'image Python)

Vous pouvez installer Pillow via pip :

```bash
pip install pillow

python lsb.py write chemin vers l'image en entree> <message secret a ecrire
python lsb.py read chemin vers limage en entre
