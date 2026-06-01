first_no = int(input("Enter your first number : "))
operator = str(input("Enter your operator (+, -, %, /, *, **) : "))
secound_no = int(input("Enter your secound number : "))
if operator == "+":
    print("Answer : ",first_no+secound_no)
elif operator == "-":
    print("Answer : ",first_no-secound_no)
elif operator == "%":
    print("Answer : ",first_no%secound_no)
elif operator == "/":
    print("Answer : ",first_no/secound_no)
elif operator == "*":
    print("Answer : ",first_no*secound_no)
elif operator == "**":
    print("Answer : ",first_no**secound_no)
else:
    print("Invalid operator.")