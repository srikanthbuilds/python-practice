number = int(input("Enter your number : "))
count = 0
for i in range(len(str(number))):
    count+=1
print(f"Given number {number} has {count} Digits." )
