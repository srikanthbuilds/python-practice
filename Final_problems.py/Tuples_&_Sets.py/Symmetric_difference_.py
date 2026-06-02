user_set1 = set()
user_set2 = set()
symmetric_elements_set = set()
while True:
    elements = input("Enter elements in 1st set (0 to quite): ")
    if elements == "0":
        break
    else:
        user_set1.add(elements)
while True:
    elements = input("Enter elements in 2nd set (0 to quite): ")
    if elements == "0":
        break
    else:
        user_set2.add(elements)
print(f"Set 1 : {user_set1}")
print(f"Set 2 : {user_set2}")
for elements in user_set1:
    if elements not in user_set2:
        symmetric_elements_set.add(elements)
for elements in user_set2:
    if elements not in user_set1:
        symmetric_elements_set.add(elements)
print(f"Symmetric/unique elements, elements set : {symmetric_elements_set}")