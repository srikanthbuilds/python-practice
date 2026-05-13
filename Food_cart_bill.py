foods=[]
prices=[]
total = 0
while True:
    food = str(input("Enter your food to buy (q to quit): "))
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter price of a {food} :$"))
        prices.append(price)

print("----- Shopping cart Bill -----")
for food in foods:
    print(food, end = ", ")
for price in prices:
    total += price
print(f"Your total is : ${total:.2f}")
print("----- Thankyou for Visiting ----- :)")

    





