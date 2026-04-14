principle = 0
rate = 0
time = 0 
while True:
    principle = float(input("Enter your principle amount : "))

    if principle < 0 :
        print("Principle amount must be greater than 0 !!")
    else :
        break

while True:
    rate = float(input("Enter your interest rate : "))

    if rate < 0 :
        print("Interest rate must be greater than 0 !!")
    else :
        break

while True:
    time = float(input("Enter your time : "))

    if time < 0 :
        print("Time must be greater than 0 !!")
    else :
        break

total = principle * pow((1+rate/100),time)
print(f"Balance after {time} years : ${total:,.2f}")

