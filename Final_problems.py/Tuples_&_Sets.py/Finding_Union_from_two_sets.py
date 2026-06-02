user_set1 = set()
user_set2 = set()
duplicate_elements_set = set()
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
for element in user_set1:
    if element not in duplicate_elements_set:
        duplicate_elements_set.add(element)
for element in user_set2:
    if element not in duplicate_elements_set:
        duplicate_elements_set.add(element)

print(f"Set 1: {user_set1}")
print(f"Set 2: {user_set2}")
print(f"Union of two set 1 & 2 elements : {duplicate_elements_set}")