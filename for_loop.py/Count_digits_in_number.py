count = 0
number = int(input("Enter your number to count digits : "))
for n in range(number+1):
    count += 1

print(f"Number of digits in {number} number is {count} digit's including zero.")