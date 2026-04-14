import random
# print(random.randint(1,10))  // it prints a random number between 1 & 10.


cards=[1,2,3,4,5,6,7,8,9,"J","K","Q"]
random.shuffle(cards) #it shuffles the values in cards list , like changing order.
print(cards)

options = ("Rock","Paper","Scisor")
# print(random.choice(options)) // chooses a value from the options tuple.