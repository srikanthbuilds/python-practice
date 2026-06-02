user_set1 = set()
user_set2 = set()
while True:
    elements = input("Enter elements for set 1 (0 to quite) : ")
    if elements =="0":
        break
    else:
        user_set1.add(elements)
while True:
    elements = input("enter elements for set 2 (0 to quite) : ")
    if elements == "0":
        break
    else:
        user_set2.add(elements)
print(f"Set 1 : {user_set1}")
print(f"Set 2 : {user_set2}")

if user_set1 <= user_set2:
    print("Set 1 is subset of Set 2")
else:
    print("Set 2 is Subset of Set 1")
if user_set2 >= user_set1:
    print("Set 2 is Superset of Set 1")
else:
    print("Set 1 is Superset of Set 2")

