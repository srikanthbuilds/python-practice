import math

# formula for to find hypotnes of a right angle triangle : c = sqrt of a^2 + b^2
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotnes of your right angle triangle, is  C : {round(c,2)}")