"""
INHERITANCE : Acquiring properties ( attributes & methods ) from one class (parent class) to another class(child class).
              
              Helps with code reuseability & extensibility

"""

class Animal:
    def __init__(self,name):
        self.name = name 
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")

class dog(Animal):
    def speak(self):
        print(f"{self.name} speaks like : WORRFF...")
class cat(Animal):
    def speak(self):
        print(f"{self.name} speaks like : MEOWWW...")
class mouse(Animal):
    def speak(self):
        print(f"{self.name} speaks like : SQUEZZE...")

Dog = dog("Mike")
print(Dog.name)
print(Dog.is_alive)

Dog.eat()
Dog.sleep()

Cat = cat("scoby")
print(Cat.name)
print(Cat.is_alive)
Cat.eat()
Cat.sleep()

Mouse = mouse("rat")
print(Mouse.name)
print(Mouse.is_alive)
Mouse.eat()
Mouse.sleep()

Dog.speak()
Cat.speak()
Mouse.speak()

