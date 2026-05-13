principle_amount = float(input("Enter your principle amount : "))
rate = float(input("Enter your rate of interest : "))
time = float(input("Enter your time :"))

amount = principle_amount * (1+ rate/100)**time
compound_interest = amount - principle_amount


print(f"Your compound interest : {compound_interest : .2f} ")