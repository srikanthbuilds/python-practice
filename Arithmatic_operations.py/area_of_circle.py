import math
# formula to find area of a circle is : pi*r*r

radius = float(input("Enter radius of your circle : "))
area = math.pi*math.pow(radius,2)
print(f"The are of your circle is : {round(area,2)} cm's")