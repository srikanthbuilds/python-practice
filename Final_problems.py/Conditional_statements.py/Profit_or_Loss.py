print("----- Profit or Loss checking programme -----")
cost_price = float(input("Enter your cost price : "))
selling_price = float(input("Enter your selling price : "))
profit = selling_price - cost_price 
loss = cost_price - selling_price  
if profit > loss:
    print(f"You got Profit amount : +{profit}")
    print(f"Profit percentage : {(profit/cost_price)*100:.2f} %")
else:
    print(f"You got Loss amount : {profit}")
    print(f"Loss percentage : {(loss/cost_price)*100:.2f} %")

