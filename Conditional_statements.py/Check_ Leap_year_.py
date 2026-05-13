year = int(input("Enter your year to check : "))

if (year%4==0 and year%100!=0) or year % 400 == 0:
    print(f"{year} is a Leap year!")
else:
    print(f"{year} is Not a leap year.")
    