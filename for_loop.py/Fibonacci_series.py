n = int(input("Enter the number of terms for Fibonacci series : "))
a = 0 
b =1
print("Fibonacci Series:")
for i in range(n):
    print(a)
    c = a+b # 0+1=1,c=1,c=2,3,5,8 
    a = b   #      0 a=1,a=1,2,3,5
    b = c   #      1 b=1,c=2,3,5,8
    
