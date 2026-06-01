print("----- Multiplication table programmes -----")
number = int(input("Enter which table do you want : "))
print(f"Here is your {number} Table : ")
i = 1
while i <= 10:
    print(f"{number} X {i} = {number*i}")
    i +=1
print()