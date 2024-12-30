while True:
    mots = input("donne une mots : ")
    if mots.isalpha() and " " not in mots:
        break
    else: 
        print("donne un mots sans chiffre et espace")

def mot_en_tableau(mot):
    tableau_de_lettres = list(mot)
    return tableau_de_lettres

# Exemple d'utilisation
tableau_resultant = mot_en_tableau(mots)
print("Tableau de lettres :", tableau_resultant)
nombre = len(tableau_resultant)
print(nombre)

trouvée = ""
chance = 5
tableau_vrai = []
tableau_faux = []
train = []
tableau_trouve = []
while len(tableau_trouve) < nombre:
    tableau_trouve.append("_")
print(tableau_trouve)
print(tableau_faux)

while trouvée != tableau_resultant or chance == 0:
    print(f"donne un mots a {nombre} lettre")
    lettre = input("donne une lettre : ")
    if lettre.isalpha() and len(lettre) == 1:
        if lettre in tableau_trouve:
            print("cette lettre est deja dans le mot")
            continue
        if lettre in tableau_resultant:
            for i in range(len(tableau_resultant)):
                if tableau_resultant[i] == lettre:
                    tableau_trouve[i] = lettre
            print(tableau_trouve)
            print("ok")
            tableau_vrai.append(lettre)    
            print(tableau_vrai)
            if tableau_trouve == tableau_resultant:
                print("super tu gagne")
                break
        else:
            print(f"non la lettre {lettre} n'est pas dans le mots")
            chance -= 1
            if chance == 4:
                train.insert(0,"/...\\")
            if chance == 3:
                train.insert(0,"!...x..!")
            if chance == 2:
                train.insert(0,"(.....)")
            if chance == 1:
                train.insert(0,"[.....]")
            if chance == 0:
                train.append("le train c'est cracher")
                print(train) 
                break
            tableau_faux.append(lettre)   
            print(train) 
            print(tableau_faux)
            print(f"il te reste {chance} chance")
    else:
        print(f"Non {lettre} n'est pas une lettre")