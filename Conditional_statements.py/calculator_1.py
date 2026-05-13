operator = str(input("Enter an operator (+, -, *, /) : "))
if operator not in ["+","-","/","%"]:
    print("Invalid operator, you have to choose in [+,-,/,%]")
else:
    n1 = float(input("Enter your first number : "))
    n2 = float(input("Enter your secound number : "))

    if operator == "+":
        print("Your answer : ",round(n1+n2,3))
    elif operator == "-":
        print("Your answer : ",round(n1-n2,3))
    elif operator == "*":
        print("Your answer : ",round(n1*n2,3))
    elif operator == "/":
        print("Your answer : ",round(n1/n2,3))
    elif operator == "":
        print("You did not type in any operator, try again! ")
 