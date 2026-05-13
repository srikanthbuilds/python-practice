"""

POLYMORPHISM : It is a greek word , poly - 'many' and morphe - 'more'.
               Have many from's or faces.

               
               TWO ways to achieve polymorphism :

                1. Inheritance = an object could be treated of the same type as a parent class.
                2. "Duck typing" = an object must have necessary attributes/methods.

"""

class Shape:
    def __init__(self):
        pass
class circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius**2
class square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2
    
class triangle(Shape):
    def __init__(self,base ,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height*0.5
    
class pizza(circle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius)


shapes = [circle(2),square(2),triangle(2,2),pizza("onion",15)]
for shape in shapes:
    print(f"{shape.area()} cm")
