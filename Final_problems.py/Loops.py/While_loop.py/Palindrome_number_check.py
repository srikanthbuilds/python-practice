number = int(input("Enter your number : "))
reversed_num = 0
number1 = number 
while number >0:
    last_digit = number%10
    reversed_num = (reversed_num*10)+last_digit
    number //= 10

if number1 == reversed_num:
    print(f"Given {number1} is a PALINDROME number.")
else:
    print(f"Given number {number1} is NOT a PALINDROME number.")