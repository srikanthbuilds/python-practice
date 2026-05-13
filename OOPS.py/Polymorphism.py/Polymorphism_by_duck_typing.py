"""

"Duck typing" = an object must have necessary attributes / methods.


"""
class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Car:
    alive = False # This matches parent attribute 'alive'.
    def speak(self): # first it is in Horn(self) method, then, it should meet the necessary methods and attributes so that it can implement Duck typing, so its again edited too speak(self) to match.
        print("Honk!")

animals = [Dog(),Cat(),Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
    

