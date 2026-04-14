rows = int(input("enter how many rows you want ? : "))
columns = int(input("enter how many columns you want ? : "))
symbol = input("enter your symbol : ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end = "")
    print()