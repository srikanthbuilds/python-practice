user_list = []
positive_numbers = []
negative_numbers = []
positive_numbers_count = 0
negative_numbers_count = 0

while True :
    elements = int(input("Enter your number to add in list (00 to Quite Adding) : "))
    if elements == 0:
        break
    else:
        user_list.append(elements)
print(f"Your Original list : {user_list}")
for number in user_list:
    if number >= 0:
        
        positive_numbers.append(number)
        positive_numbers_count += 1
    else:
        negative_numbers.append(number)
        negative_numbers_count += 1
print(f"Positive numbers from your list : {positive_numbers}")
print(f"Negative numbers from your list  : {negative_numbers}")
print(f"Your Total number of Positive numbers  : {positive_numbers_count}")
print(f"Your Total number of Negative numbers : {negative_numbers_count}")