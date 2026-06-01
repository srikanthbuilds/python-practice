print("--- LEAP YEAR checking programme ---")
year = int(input("Enter your year to check : "))

if (year%4 ==0 and year%100 != 0) or year%400 ==0:
    print(f"{year} is a LEAP year!")
else:
    print(f"{year} is NOT a LEAP year!")