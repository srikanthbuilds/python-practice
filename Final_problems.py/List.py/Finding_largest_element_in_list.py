running = True 
user_list = []
largest_number =0
while running == True:
    elements =  int(input("Enter your number in list (00 To Quite):"))
    if elements == 00:
        break
    else:
        user_list.append(elements)
print(f"Your original list : {user_list}")
for number in user_list:
    if number > largest_number:
        largest_number = number
print(f"Your largest number : {largest_number}")

