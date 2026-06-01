number = float(input("Enter first number : "))
number2 = float(input("Enter secound number : "))
number3 = float(input("Enter third number : "))
if number < number2 and number < number3:
    print(f"{number} is the smallest number.")
elif number2 < number3 and number2 < number:
    print(f"{number2} is the smallest number.")
elif number3 < number and number3 < number2:
    print(f"{number3} is the smallest number.")
else:
    print("ALL are EQUAL.")
