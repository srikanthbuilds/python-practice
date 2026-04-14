operator = str(input("Enter an operator (+, -, *, /) : "))
n1 = float(input("Enter your first number : "))
n2 = float(input("Enter your secound number : "))

if operator == "+":
    print(round(n1+n2,3))
elif operator == "-":
    print(round(n1-n2,3))
elif operator == "*":
    print(round(n1*n2,3))
elif operator == "/":
    print(round(n1/n2,3))
elif operator == "":
    print("You did not type in any operator, try again! ")
else:
    print(f"{operator} is not a valid operator!")
    print("It should be an (+, -, *, /) , Try again!")
 