running = True 
user_list = []
first_largest_number =0
secound_largest_number =0
while running == True :
    elements = int(input("Enter your number to add in list (00 To Quite Adding): "))
    if elements ==00:
        break
    else:
        user_list.append(elements)
for number in user_list:
    if number > first_largest_number:
        secound_largest_number = first_largest_number
        first_largest_number = number
print(f"Your Original list: {user_list}")
print(f"Your Secound largest number : {secound_largest_number}")
print(f"Your First largest number : {first_largest_number}")


