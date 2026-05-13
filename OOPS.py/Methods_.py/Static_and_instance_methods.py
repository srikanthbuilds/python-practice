"""
Static method = A method that belongs to a class rather than any object from that class (objects).
                Usually used for general utility's.

Instance methods = Best for operations on instances of the class (objects).
Static methods   = Best for utility functions that do not need access to the class data. 


"""


class Employee:
    def __init__(self,name,position):
        self.name = name 
        self.position = position
    
    # This is a instance method.
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod   # This is a static method.
    def is_valid(position):
        positions = ["manager","cashier","cook"]
        return position in positions
    
Employee1 = Employee("mukesh","cashier")
Employee2 = Employee("vijay malya","cook")
Employee3 = Employee("sundar pichai","manager")



print(Employee.is_valid("manager")) # for to access static method , you need to call it with it's class name.


print(Employee1.get_info()) # For instance method access you need to call it with a object.
print(Employee2.get_info())
print(Employee3.get_info())


    

