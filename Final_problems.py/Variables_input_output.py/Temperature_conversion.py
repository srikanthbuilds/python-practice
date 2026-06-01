temp = float(input("Enter your temperature : "))
unit = str(input("Enter you temperaure unit (F/C) : "))

if unit.upper() == "F":
    unit = "C"
    print(f"{temp}F is converted to Celsius is {round((temp-32)*(5/9))}{unit}")
elif unit.upper() == "C":
    unit = "F"
    print(f"{temp}C is converted to Fharenhiet is {round((temp*(9/5))+32)}{unit}")
else:
    print("Invalid unit!")
