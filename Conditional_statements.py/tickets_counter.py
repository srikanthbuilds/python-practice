# ticket counter programme !!
# first show the original ticket price!
# 1. take users age
# 2. based on user age , divide tickets prices accordingly
# 3. may add some discounts!

print("Welcome to 'Avatar' movie ticket counter!")
print("Ticket price starts from $100 dollar's")
age = int(input("Enter your age to get discount on your ticket price : "))
p = 100
if age >= 18 and age <= 25:
    p -= 20 
    print("dude!, you got a student discount of 20% off")
    print(f"Ticket price: ${p}")
    print("Enjoy the show & have fun!")
elif age >=10 and age <18:
    p -= 50
    print("hey kid!, you got a child discount of 50% off")
    print(f"Ticket price: ${p}")
    print("Enjoy the show & have fun!")
elif age >25 and age <=59 :
    print("dude!, you got no discount!")
    print(f"Ticket price: ${p}")
    print("Enjoy the show & have fun!")
else :
    p -= 10
    print("hey man!,you got a discount of 10% off")
    print(f"Ticket price: ${p}")
    print("Enjoy the show & have fun!")




     