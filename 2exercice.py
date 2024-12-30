#terminal ruff format exercice.player
#ruff --select E,F,I,N,UP,B,C4,SIM,PTH,ISC,ARG

import csv
import hashlib
import random
import secrets
import string
import uuid
from datetime import datetime
from pathlib import Path
from base64 import b64encode
import requests
import json

def get_json():
    response = requests.get("https://dummyjson.com/products")
    product = response.json().get("products",[])
    return product

def date_base64():
    return_product = get_json()
    for fot in return_product:
        fot["processed_at"] = datetime.now().isoformat()
        fot["base64_json_data"]=b64encode(json.dumps(fot).encode("utf-8")).decode("utf-8")
        print(json.dumps(fot, indent=2))

def password_uuid():
    return_product = get_json()
    for fot in return_product:
        you_uuid = uuid.uuid4()
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(8))
        password_unsafe = ''.join(random.choice(characters) for _ in range(8))
        print(f"Mots de pass : {password} \nSafe : {password_unsafe} \nUuid : {you_uuid}")

def img_md5():
    return_img_md5 = get_json()
    for fot in return_img_md5:
        tab_img = fot.get("images", [])
        resultat = " -- ".join(tab_img)
        image_md5 = hashlib.md5(resultat.encode()).hexdigest
        print(f"Image md5 : {image_md5}")
filee = get_json


def deposit():
    filee = get_json()
    p = Path(r"C:\Users\Youssef\Downloads\MY_FILE_Youssef_Boulahia.csv")
    def write_csv(data, filename: str) -> None:
        headers = data[0].keys() if data else []
        with Path.open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter = ";")
            writer.writeheader()
            writer.writerows(data)
    write_csv(filee, p)

products_data = get_json()
date_base64()
password_uuid()
img_md5()
deposit()

 