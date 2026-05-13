
# temperature convertor programme !

unit = str(input("Is your temperature is in Celsius Or Fahrenheit (C / F): "))
temp = float(input("Enter your temperature : "))

if unit == "F":
    unit = "C"
    print(f"The temperature in Celsius is : {round((temp-32)*(5/9))} {unit}")
elif unit == "C":
    unit = "F"
    print(f"The temperature in Fahrenheit is : {round((temp*(9/5))+32)} {unit}")
else :
    print(f"{unit} is invalid unit !!")