print("----- 5 & 11 number DIVISIBLITY checking programme -----")
number = float(input("Enter your number to check : "))
if number % 5 == 0 :
    print(f"{number} is only divisible by 5")
elif number % 11 ==0:
    print(f"{number} is only divisible by 11")
elif number % 5 == 0 and number % 11 ==0:
    print(f"{number} is divisible by 5 & 11")
else:
    print(f"{number} is NOT divisible by 5 & 11")




