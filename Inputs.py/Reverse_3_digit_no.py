number = int(input("Enter a 3-digit number : "))
# 321
digit1 = number%10
digit2 = (number//10)%10
digit3 = number // 100

# 123
reversed_number = digit1*100+digit2*10+digit3
print("Reversed number        :",reversed_number)