number = int(input("Enter a number : "))
Prime_numbers_count = 0
for i in range(1,number+1):
    if i == 2:
        print(i)
    if i%2 !=0 and i%i == 0:
        print(i)
        Prime_numbers_count += 1
print(f"Total prime numbers from 1 to {number}  = {Prime_numbers_count}")
