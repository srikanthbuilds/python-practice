user_list1 = []
user_list2 = []
duplicates_list = []
while True :
    elements = (input("enter nyumber to add in 1st list (0 To Quite): "))
    if elements == "0":
        break
    else:
        user_list1.append(elements)
while True :
    elements = (input("enter nyumber to add in 2nd list (0 To Quite): "))
    if elements == "0":
        break
    else:
        user_list2.append(elements)
for numbers in user_list2 and user_list1:
    if numbers in user_list1 and numbers in user_list2:
        duplicates_list.append(numbers)
print(f"List 1 : {user_list1}")
print(f"List 2 : {user_list2}")
print(f"Duplicates : {duplicates_list}")




