principle = float(input("Enter the principle amount : "))
rate =      float(input("Enter rate of interest     : "))
time =      float(input("Enter time period          : "))

print(f"Your simple interest amount for {time} year time : {principle*rate*time}")
print(f"Total amount to pay with interest : {principle*(1+rate*time)}")

compound = str(input("Do you want to calculate Compound interest also (Y/N) :"))
if compound.upper() == "Y":
    n = int(input("Enter how many times do you want to compound every year ? : "))
    print(f"Total amount with compound interest : {(principle*(1+(rate/n))**(n*time)):.2f}")
else:
    print("Thankyou for visiting, have a great day!")