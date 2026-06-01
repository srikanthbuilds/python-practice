print("----- Multiplication table programme -----")
number = int(input("Enter which table do you want : "))
print(f"Here is your {number} Table : ")
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")