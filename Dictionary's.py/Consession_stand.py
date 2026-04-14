#               [--- Consession stand programme ---]

print("---------------------- MENUE ------------------------------")
print()
menue = {
        "pop corn":250,
        "coke":20,
        "eggpuff":35,
        "chickenpuff":35,
        "chocolate":20,
        "samosa":25,
        "soda":20,
        "pizza":220,
        "burger":180,
        "sandwich":150,
}
cart = []
total =0

for key,value in menue.items():
    print(f"{key:15}:{value:.2f}"
    )
print()
print("----------------------------------------------------------")
print()

while True:
    food = input("Enter an item from the above menue (q to quit): ").lower()
    if food == "q":
        break
    elif menue.get(food)==None:
         print(f"{food} is not there in our menue!")
    elif menue.get(food) is not None:
        total += menue.get(food)
        cart.append(food)
print()
print("------------ YOUR ORDER ------------")
print()
for food in cart:
    print(food) 
print()
print(f"Your total is : ${total}")
print()


