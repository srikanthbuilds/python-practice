"""
class variable : 1. shared amoung all instances of a class.
                 2. Defined outside the constructor.
                 3. Allows you to share data amoung all objects that you created from that class. 

                 



"""

class Student:

    class_year = 2028 # THIS IS A " CLASS " VARIABLE.

    no_of_students =0
    def __init__(self,name,age):

        self.name= name # THIS IS A " INSTANCE " VARIABLE.
        self.age = age
        Student.no_of_students += 1

student1 = Student("Srikanth",20)
student2 = Student("Spogebob",21)
student3 = Student("Peter park",19)
student4 = Student("Agust",18)


print(f"My class year {Student.class_year} graduating students are total {Student.no_of_students} memebers")
print(f"{student1.name},he is {student1.age} years old" )
print(f"{student2.name},he is {student2.age} years old")
print(f"{student3.name},he is {student3.age} years old")
print(f"{student4.name},he is {student4.age} years old")

