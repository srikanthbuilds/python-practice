student_marks = dict()
n = int(input("Enter how many students do you want to enter : "))
for student in range(n):
    print(f"--- Entering details for student #{student+1} ---")
    name = input("Enter student name : ")
    marks = int(input(f"Enter marks for {name} : "))
    student_marks[name] = marks
print("--- Final student marks Dictionary ---")
print(student_marks)
print(f"--- Formated student Record ---")
for key,values in student_marks.items():
    print(f"Student : {key} | marks : {values}")

