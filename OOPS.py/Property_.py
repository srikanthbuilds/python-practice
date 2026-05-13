"""

@property = Decorator used to define property (it can be accessed like an 'attribute')
            Benifit : Add additional logic when read , write and delete attributes.
            Gives you getter , setter and deleter methods.


"""

class Rectangle :
    def __init__(self,width,height):
        self._width = width        # '_width' & '_height' are private attributes.
        self._height = height 


    @property    # this '@property' is must be mentioned.
    def width(self):
        return f"{self._width} cm's"
    @property
    def height(self):
        return f"{self._height} cm's"
    


    @width.setter

    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter

    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")




    @width.deleter

    def width(self):
        del self._width
        print("Width is deleted.")

    @height.deleter

    def height(self):
        del self._height
        print("Height is deleted.")
        


rectangle1 = Rectangle(7,9)

print(rectangle1._width)
print(rectangle1._height)   

rectangle1.width = 2           # setter
rectangle1.height = 2

print(rectangle1.width)
print(rectangle1.height)       # getter

del rectangle1.width
del rectangle1.height          # deleter


        