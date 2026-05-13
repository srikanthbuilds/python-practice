"""

Super : A function used in child class to call methods from parent class(super class)
       
        Allows you to extend the functionality of the inherited methods.

"""

class shapes:
    def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled
    def describe(self):
        print(f"It is in {self.colour} colour and {"filled" if self.is_filled == True else "not filled"} ")

class circle(shapes):
    def __init__(self,colour,is_filled,radius):
        super().__init__(colour,is_filled)# calling common attributes using "super()"
        self.radius =  radius 

    # this is overriding...
    def describe(self):
        super().describe()# extending method from parent class
        print(f"It is a circle with area {3.14*self.radius*self.radius}cm ")


class square(shapes):
    def __init__(self,colour,is_filled,width):
        super().__init__(colour,is_filled)# calling common attributes using "super()"
        self.width =width

    # this is overriding...
    def describe(self):
        super().describe()# extending method from parent class
        print(f"It is a square with area {self.width*self.width}cm ")

    
class triangle(shapes):
    def __init__(self,colour,is_filled,width,height):
        super().__init__(colour,is_filled)# calling common attributes using "super()"
        self.width = width
        self.height = height 

    # this is overriding...
    def describe(self):
        super().describe() # extending method from parent class
        print(f"It is a triangle with area {self.width*self.height}cm ")


circle = circle(colour="Red",is_filled = True,radius = 5)
square = square(colour="Yellow",is_filled=False,width=10)
triangle = triangle(colour="Black",is_filled=True,width=5,height=5)


print(circle.colour)    # This colour attribute's are from parent class
print(square.colour)
print(triangle.colour)

print(circle.is_filled)    # This is_filled  attribute's are from parent class
print(square.is_filled)
print(triangle.is_filled)

print(circle.radius)
print(square.width)
print(triangle.height)
print(triangle.width)

# This methods have unique describing's with it's area's.
circle.describe()
square.describe()
triangle.describe()
        
