user_set1 = set()
duplicate_elements_set = set()
while True:
    elements = input("Enter elements for set (0 to quite): ")
    if elements == "0":
        break
    else:
        user_set1.add(elements)
print(f"Set   : {user_set1}")
