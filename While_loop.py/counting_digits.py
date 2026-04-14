n = int(input("Enter your numbers to count digits : "))
n1 = n
i = 1
count=0
while i<=n:
    n = n/10
    count += 1 
print(f"Your number {n1} contains -> {count} digits")
1