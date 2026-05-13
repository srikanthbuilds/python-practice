"""

Decorator = A function that extends the behaviour of another function.
            Without modifying the base function.
            Pass the base function as an argument to the decorator.


            A function that extends the behaviour of a base function.

"""

def add_sprikles(func):
    def wrapper(*args):
        print("* add sprikles")
        func(*args)
    return wrapper

def add_fudge(func):
    def wrapper(*args):
        print("* add fudge")
        func(*args)
    return wrapper

def add_serum(func):
    def wrapper(*args):
        print("* add serum")
        func(*args)
    return wrapper    

def add_bars(func):
    def wrapper(*args):
        print("* add bars")
        func(*args)
    return wrapper

@add_sprikles
@add_fudge
@add_serum
@add_bars
def get_icecream(flavour):
    print(f"Here is your {flavour} ice cream!")

get_icecream("Vanilla")