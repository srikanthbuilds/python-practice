name = str(input("Hey, could you please enter your name : "))
age =  int(input("How many years old are you            : "))
if age >=18:
    print(f"Hi {name}, nice to meet you!\nBy the way, you are eligible to vote!")
else:
    print(f"Hi {name}, nice to meet you!\nBy the way, you are NOT eligible to vote!")