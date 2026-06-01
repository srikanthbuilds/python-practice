number = int(input("Enter your number : "))
num = 0
for i in range(len(str(number))):
    num += number%10 # gets the last digit & adds to num.
    number //= 10    # removes the last digit.

print(f"The sum of digits is : {num}")