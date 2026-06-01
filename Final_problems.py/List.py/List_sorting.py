user_list = []
while True:
    elements = int(input("Enter your number to add in list (00 To Quite adding): "))
    if elements == 00:
        break
    else:
        user_list.append(elements)
user_list.sort()
print(f"Your Original list : {user_list}")
print(f"Sorted list : {user_list}")
