rows = int(input("Enter how many rows you want : "))
columns = int(input("Enter how many columns you want :"))
symbol = input("Enter your symbol : ")
for x in range(rows):
    for y in range(columns):
        print(symbol,end ="")
    print()
