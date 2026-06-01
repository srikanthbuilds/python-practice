print("----- Billing system with discount conditions programme -----")
print()
print("----- D - Mart -----")
print("Peanut butter : 160 ")
print("Bread         : 100")
print("Banana's      : 200")
print("Apple's       : 400")
print("-------------------")
print("Total amount  : 860")
print("-------------------")
print()
amount = 860
age = int(input("To get Discount, please enter your Age : "))
if age <=18 :
    print("You got a Student discount of 30% ")
    print(f"After discount, Total amount : {amount-228}")
else:
    print("Sorry sir, NO discounts for adults. ")
    print("Total amount  : 860")


    

