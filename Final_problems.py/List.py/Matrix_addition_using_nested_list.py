user_list1 = []
user_list2 = []
result = []
while True :
    elements = int(input("Enter number for 1st list (0 To Quite) : "))
    if elements == 0:
        break
    else:
        user_list1.append(elements)
while True :
    elements = int(input("Enter number for 2nd list (0 To Quite) : "))
    if elements == 0:
        break
    else:
        user_list2.append(elements)
print(f"List 1 : {user_list1}")
print(f"List 2 : {user_list2}")
for no_in_list1 in range(len(user_list1)):
    for no_in_list2 in range(len(user_list2)):
        if no_in_list1 == no_in_list2:
            total = user_list1[no_in_list1] + user_list2[no_in_list2]
            result.append(total)
print(f"Result : {result}")
            



