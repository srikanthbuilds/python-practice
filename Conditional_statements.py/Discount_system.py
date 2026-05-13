amount = int(input("Enter  your billing amount : "))

if amount >= 5000:
    discount = amount *0.20
elif amount >= 3000:
    discount = amount *0.10
else :
    discount = 0

print(f"Discount amount : {discount}")
total_amount  = amount -discount
print("Total amount : ",total_amount) 