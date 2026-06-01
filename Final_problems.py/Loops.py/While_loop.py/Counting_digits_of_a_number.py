number = int(input("Enter your number : "))
number1 = number
digits_count = 0 
while number >0:
    digits_count += 1
    number //=10
print(f"Given number {number1} has {digits_count} Digits.")