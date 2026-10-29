import json
from pathlib import Path
file_path = Path("E:/SE/produc.json")
products=[]

def load():
    global products
    if file_path.exists():
        try:
             with open(file_path, "r", encoding="utf-8") as file:
                products = json.load(file)
        except(json.JSONDecodeError,OSError):
            products=[]
    else:
        products=[]

def save():
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)

