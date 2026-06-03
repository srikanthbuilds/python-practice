n = int(input("How many 'key:value' you want to enter : "))
print(f"You are entering 'key:value' pairs : ")
Dictionary = dict()
for i in range(n):
    print(f"For pair {i+1}")
    keys = input("Enter key : ")
    values = input("Enter value : ")
    Dictionary[keys] = values
print(f"Original dictionary : {Dictionary}")
print(f"Sorted values : {sorted(Dictionary.values())}")
