
"""

class methods = Allows operations related to class itself!

"""

class student:
    count = 0 
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa
    
    @classmethod
    def get_count(cls): # instead of using "self" parameter , we use "cls" parameter.
        return f"Total number of students : {cls.count}"
    
    @classmethod 
    def get_avg_gpa(cls): # instead of using "self" parameter , we use "cls" parameter.
        if cls.total_gpa == 0:
            return 0
        else :
            return f"Average gpa : {(cls.total_gpa / cls.count):.2f}"
    
student1 = student("Srikanth",9.3)
student2 = student("patrick",8.3)
student3 = student("dom",7.3)
student4 = student("vel",6.3)

print(student.get_count())     
                                     # We need to call it with class name
print(student.get_avg_gpa())

