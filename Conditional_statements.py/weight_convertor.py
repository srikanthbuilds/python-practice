
# weight convertor programme 
print("--- Weight conversion programme ---")
weight = float(input("Enter your weight : "))
unit = input("Kilograms Or Pounds (K Or L) : ")
if unit == "K":
    unit = "Lbs"
    print(f"Your weight is : {round(weight*2.205,1)} {unit} ")
elif unit == "L":
    unit = "Kgs"
    print(f"Your weight is : {round(weight/2.205,1)} {unit} ")
else:
    print(f"{unit} is invalid unit !!") 