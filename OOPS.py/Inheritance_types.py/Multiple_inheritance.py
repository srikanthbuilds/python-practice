"""

Multiple inheritance : a child class inherits more than 1 parent class is called as multiple inheritance. 
                       C(A,B)

Multilevel inheritance : a child class inherits a parent class and parent class inherits a grand parent class.
                        C(B) -> B(A) -> A

"""



# Multiple inheritance EXAMPLE :

class prey:
    def flee():
        print(f"This animal is fleeing...")
class predator:
    def hunt():
        print(f"This animal is hunting...")

class rabbit(prey):
    pass

class hawk(predator):
    pass
class fish(prey,predator): # inherits more than one parent class!
    pass

rabbit.flee()
# rabbit.hunt() this rabbit as no method hunt.
hawk.hunt()
# hawk.flee() this hawk as no method flee.


#  this fish has both flee and hunt methods.
fish.flee()
fish.hunt()