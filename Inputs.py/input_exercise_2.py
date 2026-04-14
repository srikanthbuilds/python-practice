# shopping cart !!

items = str (input("what item would you like to buy ? : "))
quantity = int(input(f"how many {items}'s are you going to buy ? : "))
price = float(input(f"how much does it costs to buy 1 {items} ? : "))
total = quantity * price
print(f"for {quantity} X {items}'s, your's total cost is : ${total}")
print("THANK YOU for visiting :)")