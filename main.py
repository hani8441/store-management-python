from storage import load
from storage import save
from productsofmarket import add
from productsofmarket import show
from productsofmarket import search
from productsofmarket import edit
from productsofmarket import delete
from productsofmarket import calculate
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
            exit()
        else:
            print("invalid")
    except ValueError:
        print("enter number")
