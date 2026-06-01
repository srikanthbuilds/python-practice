number = int(input("Entr your number : "))
sum_of_digits = 0
while number>0:
    sum_of_digits += number%10
    number//=10
print(f"The sum of digits is : {sum_of_digits}")
