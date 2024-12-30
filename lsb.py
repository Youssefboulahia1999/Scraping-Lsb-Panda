import sys
from PIL import Image

def hide_message(image_path: str, message: str) -> None:
    img = Image.open(image_path)
    pixels = img.load()
    message += '\0'  # Ajouter un caractère de fin de texte

    index = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = pixels[x, y]

            # Cacher les bits du message dans les bits de poids faible de chaque composante RGB
            if index < len(message):
                ascii_code = ord(message[index])
                pixels[x, y] = (r & 0b11111110 | (ascii_code & 0b10000000) >> 7,
                                g & 0b11111110 | (ascii_code & 0b01000000) >> 6,
                                b & 0b11111100 | (ascii_code & 0b00111111))
                index += 1
            else:
                img.save("image_with_secret_message.png")
                return

# def retrieve_message(image_path: str) -> str:
#     img = Image.open(image_path)
#     pixels = img.load()

#     message = ""
#     ascii_code = 0
#     index = 0

#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             r, g, b = pixels[x, y]

#             # Récupérer les bits du message depuis les bits de poids faible de chaque composante RGB
#             ascii_code = (ascii_code << 1) | (r & 1)
#             ascii_code = (ascii_code << 1) | (g & 1)
#             ascii_code = (ascii_code << 2) | (b & 3)

#             index += 1

#             if index % 8 == 0:
#                 if ascii_code == 0:
#                     return message
#                 message += chr(ascii_code)
#                 ascii_code = 0

#     return message

def retrieve_message(image_path: str) -> str:
    img = Image.open(image_path)
    pixels = img.load()

    message = ""
    ascii_code = 0
    index = 0

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = pixels[x, y]

            # Extraire un bit de chaque composante RGB (R, G, B) - un total de 8 bits
            ascii_code = (ascii_code << 1) | (r & 1)  # Extraire le bit du rouge
            ascii_code = (ascii_code << 1) | (g & 1)  # Extraire le bit du vert
            ascii_code = (ascii_code << 1) | (b & 1)  # Extraire le bit du bleu

            index += 1

            # Lorsque nous avons 8 bits (un caractère ASCII complet)
            if index % 8 == 0:
                if ascii_code == 0:  # Si nous avons un caractère de fin (ASCII 0)
                    return message
                # Vérifier que l'ASCII code est dans la plage valide (0 à 127)
                if 0 <= ascii_code <= 127:
                    message += chr(ascii_code)
                else:
                    print(f"Valeur d'ASCII invalide détectée : {ascii_code}")
                    return message
                ascii_code = 0  # Réinitialiser pour le prochain caractère

    return message




if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python lsb.py write <chemin_vers_l'image_en_entree> <message_secret_a_ecrire>")
        print("python lsb.py read <chemin_vers_limage_en_entre>")
        sys.exit(1)

    action = sys.argv[1]
    image_path = sys.argv[2]

    if action == "write":
        message = sys.argv[3]
        hide_message(image_path, message)
        print("Message caché avec succès dans l'image.")
    elif action == "read":
        secret_message = retrieve_message(image_path)
        print("Message caché dans l'image:", secret_message)
    else:
        print("Cette fonctionnalité n'est pas disponible.")
