user_list1  = []
user_list2  = []
while True:
    elements = int(input("Enter number to add in 1st list (0 To Quite) : "))
    if elements == 0:
        break
    else:
        user_list1.append(elements)
while True:
    elements = int(input("Enter number to add in 2nd list (0 To Quite) : "))
    if elements == 0:
        break
    else:
        user_list2.append(elements)
merged_list = user_list1+ user_list2
print(f"List 1 : {user_list1}")
print(f"List 2 : {user_list2}")
print(f"Merged list : {merged_list}")




        
