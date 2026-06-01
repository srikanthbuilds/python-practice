number = int(input("Enter your number : "))
reversed_num = 0
last_digit = 0
for i in range(len(str(number))):
    last_digit = number%10 # gets the last digit & adds to num.
    reversed_num = (reversed_num*10)+last_digit
    number //= 10    # removes the last digit.

print(f"Reversed number : {reversed_num}")