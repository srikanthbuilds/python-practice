"""

Multi-level inheritance : a child class inherits a parent class and parent class inherits a grand parent class.
                        C(B) -> B(A) -> A

"""

# Multi-level inheritance EXAMPLE :

class Animal:
    def __init__(self,name):
        self.name = name 

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")

class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing...")
class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting...")

class rabbit(prey):
    pass

class hawk(predator):
    pass
class fish(prey,predator):
    pass

Rabbit = rabbit("Mike") 
Hawk = hawk("Tony") 
Fish = fish("Nemo") 

Rabbit.eat()
Rabbit.sleep()
Rabbit.flee()

Hawk.eat()
Hawk.sleep()
Hawk.hunt()

Fish.eat()
Fish.sleep()
Fish.flee()
Fish.hunt()