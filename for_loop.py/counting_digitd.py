n = int(input("Enter your numbers for to count digits : "))
count = 0
for i in range(1,n+1):
    n = n/10
    count +=1
print(count)
