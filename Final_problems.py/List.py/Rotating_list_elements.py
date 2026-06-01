user_list = []
while True:
    elements = input("Enter elements to add in list (0 To Quite) : ")
    if elements == "0":
        break
    else:
        user_list.append(elements)
# print(f"Original list : {user_list}")
# user_list.reverse()
# print(f"Reversed list : {user_list}")
index = len(user_list)
for i in range(len(user_list),0):
    i -= 1

    print(i)

    

