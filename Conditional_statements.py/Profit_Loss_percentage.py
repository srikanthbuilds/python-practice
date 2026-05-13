cp = int(input("Enter cost price : "))
sp = int(input("Enter selling price : "))
if sp > cp:
    profit = sp - cp
    profit_percentage = (profit/cp)*100
    print("Profit amount      : ",profit)
    print(f"Profit percentage : {profit_percentage:.2f}%")
elif cp > sp:
    loss = cp - sp
    loss_percentage = (loss/cp)*100
    print("Loss amount      : ",loss)
    print(f"Loss percentage : {loss_percentage:.2f}%")

else:
    print("No profit , No loss")