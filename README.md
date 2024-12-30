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
