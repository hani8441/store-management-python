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


def add():
   
    name = input("name: ").strip()

    if not name:
        print("invalid")
        return

    try:
        price = int(input("price: "))
        count = int(input("count: "))

        if price <= 0 or count <= 0:
            print("Price and count must be greater than zero.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    product = {
        "name": name,
        "price": price,
        "count": count
    }

    products.append(product)
    save()
    print("Product added successfully.")

    
def show():
    if not products:
        print("No products found.")
        return

    for product in products:
        print(
            "Name:", product["name"],
            "Price:", product["price"],
            "Count:", product["count"]
        )

def search():
    name=input("name").strip().lower()
    for product in products:
        if product["name"].lower()==name:
            print(product)
            return
    else:
            print("it isnt")
            return

def edit():
    name=input("name:").strip().lower()
    for product in products:
        if product["name"].lower()==name:
            try:
                price=int(input("newprice:"))
                count=int(input("newcount:"))
                if price <= 0 or count<= 0:
                    print("Price and count must be greater than zero.")
                    return

            except ValueError:
                print("Please enter valid numbers.")
                return

            product["price"] = price
            product["count"] = count

            save()
            print("Product updated successfully.")
            return

    else:
        print("it isnt")
        return
    

def delete():
    name=input("name:").strip().lower()
    for i in products:
        if i["name"].lower()==name:
            products.remove(i)
            save()
            print("success")
            return
    else:
        print("it isnt")
        return
def calculate():
    total=0
    for i in products:
        total += i["price"] * i["count"]

    print("Total inventory value:", total)


load()   
select=True
while select==True:
    print("1.add")
    print("2.show")
    print("3.search")
    print("4.edit")
    print("5.delete")
    print("6.calculate")
    print("7.exit")
    try:
        num=int(input("num:"))
        if num==1:
            add()
        elif num==2:
            show()
        elif num==3:
            search()
        elif num==4:
            edit()
        elif num==5:
            delete()
        elif num==6:
            calculate()
        elif num==7:
            break
        else:
            print("invalid")
    except ValueError:
        print("enter number")
