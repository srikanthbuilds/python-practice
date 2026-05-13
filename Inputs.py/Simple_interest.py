principle_amount = int(input("Enter your principle amount : "))
rate = int(input("Enter your rate of interest : "))
time = int(input("Enter your time :"))

simple_interest = (principle_amount * rate * time)/100

print("Your simple interest : ",simple_interest)