user_list1 = []
user_list2 = []
result = []
while  True:
    elements = int(input("Enter number for 1st list (0 to quite) : "))
    if elements == 0:
        break
    else:
        user_list1.append(elements)
while True:
    elements = int(input("Enter number for 2nd list (0 to quite) : "))
    if elements == 0:
        break
    else:
        user_list2.append(elements)
print(f"List 1 : {user_list1}")
print(f"List 2 : {user_list2}")
if len(user_list1) != len(user_list2):
    print("Both lists should have same length, Try again!")

else:
    for numbers_in_list_1 in range(len(user_list1)):
        for numbers_in_list_2 in range(len(user_list2)):
            if numbers_in_list_1 == numbers_in_list_2:
                Total = user_list1[numbers_in_list_1] + user_list2[numbers_in_list_2]
                result.append(Total)

print(f"Added list : {result}")

