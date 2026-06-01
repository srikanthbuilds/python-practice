running = True
user_list = []
even_number_list = []
odd_number_list = []

even_number_count = 0 
odd_number_count = 0 
while running == True:
    elements = int(input("Enter your number to add in list (00 To Quite adding): "))
    if elements == 00:
        break
    else:
        user_list.append(elements)
for number in user_list:
    if number%2 ==0:
        even_number_count += 1
        even_number_list.append(number)
    else:
        odd_number_count += 1
        odd_number_list.append(number)
print(f"From your list even numbers :{even_number_list}")
print(f"From your list odd numbers :{odd_number_list}")
print(f"Total number of even numbers :{even_number_count}")
print(f"Total number of odd numbers  :{odd_number_count}")


