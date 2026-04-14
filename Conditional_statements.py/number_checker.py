number = int(input("Enter a number: "))
if number > 0 :
    print(f"{number} is a positive number!")
elif number < 0:
    print(f"{number} is a negative number!")    
else:
    print(f"{number} is zero!") 



if number%2 == 0 :
        print(f"{number} is a even number")
else :
        print(f"{number} is a odd number")
        



if number % 3 ==0 and number % 5 ==0 :
    print(f"{number} is divisible by 3 and 5")
elif number % 3 ==0:
    print(f"{number} is divisible by only 3")
elif number % 5 ==0 :
    print(f"{number} is divisible by only 5")
else :    
    print(f"{number} is not divisible by 3 or 5")
