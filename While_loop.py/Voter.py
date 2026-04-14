age =0
while True:
    age = int(input("Enter your age :"))
    if age <= 0:
        print(f"Your age cannot be 0 or negative value")
    elif age <18:
        print(f"You are {age} years old, you are NOT eligible to vote!")
        break
    
    elif age>=18:
        print(f"You are {age} years old, you are eligible to vote!")
        break
        
