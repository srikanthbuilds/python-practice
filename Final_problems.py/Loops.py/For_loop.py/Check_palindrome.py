number = int(input("Enter your number : "))
number1= number
reversed_num = 0
for i in range(len(str(number))):
    last_digit = number%10
    reversed_num = (reversed_num*10)+last_digit
    number //= 10
if number1 == reversed_num:
    print(f"Given number {number1} is a PALINDROME number.")
else:
    print(f"Given number {number1} is NOT a PALINDROME number.")