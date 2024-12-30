import requests
from pathlib import Path
from typing import List

class MyCsvWriter:
    def __init__(self,path:Path, columns_name: List[str],delimiter: str = ';'):
        self.path = path
        self.columns_name = columns_name
        self.delimiter = delimiter
        self.file = open(path,'w')

    def __enter__(self):
#ciblé le fiche et l'ouvrire en write
        self.file = open(self.path, 'w')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
# ferme le fichier 
        if self.file:
            self.file.close()
    def escape_value(self,value: str) -> str:
        if ',' in value or '"' in value:
            return f'"{value.replace("\"","\"\"")}"'
        else:
            return value

    
    def write_my_headers(self) -> None:
        headers = self.delimiter.join(
            self.escape_value(column) for column in self.columns_name)
        self.file.write(headers + "\n")

    def write_my_rows(self, rows: List[dict])-> None:
        for i in rows:
            i_rows = self.delimiter.join(
                self.escape_value(str(i.get(column, ''))) for column in self.columns_name)
            self.file.write(i_rows +'\n')

    def close_file(self) -> None:
        self.file.close()

r = requests.get("https://dummyjson.com/products")
rows = r.json()["products"]
file_path = Path.home().joinpath("Downloads", "Youssef_boulahia.csv")
with MyCsvWriter(file_path, columns_name=list(rows[0])) as writer:
    writer.write_my_headers()
    writer.write_my_rows(rows)
    writer.close_file()

