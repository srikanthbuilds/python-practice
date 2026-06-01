user_list1 = []
user_list2 = []
common_numbers_list =[]
running = True
while running == True:
    elements = int(input("Enter your number to add in 1st list (00 To Quite adding) : "))
    if elements == 00:
        break
    else:
        user_list1.append(elements)
while running == True:
    elements = int(input("Enter your number to add in 2nd list (00 To Quite adding) : "))
    if elements == 00:
        break
    else:
        user_list2.append(elements)
print(f"Your 1st original list : {user_list1}")
print(f"Your 2nd original list : {user_list2}")
for numbers in user_list1 and user_list2:
    if numbers in user_list1 and user_list2:
        common_numbers_list.append(numbers)
print(f"Your common numbers from both list's : {common_numbers_list}")

