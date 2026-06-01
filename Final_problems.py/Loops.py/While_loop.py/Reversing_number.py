number = int(input("Enter your number to reverse it : "))
reversed_no = 0
i = 1
while number > 0:
    last_digit = number %10
    reversed_no = (reversed_no*10) + last_digit
    number//=10
print(f"Reversed number : {reversed_no}")

