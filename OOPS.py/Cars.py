class Car:  # a class named "Car".

    def __init__(self,year,model,colour,for_sale):
        self.year= year
        self.model = model
        self.colour = colour
        self.for_sale = for_sale


#    This is a method : which runs a block of code.
    def drive(self):
        print(f"You are driving {self.colour} {self.model}")

#    This is a method : which runs a block of code.
    def parking(self):

        print(f"You are parking {self.colour} {self.model}")

#    This is a method : which runs a block of code.
    def describe(self):
        print(f"It is a {self.year} {self.colour} {self.model} and its for_sale : {self.for_sale} ")
