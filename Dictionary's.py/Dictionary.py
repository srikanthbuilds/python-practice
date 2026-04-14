# ---------------------- DICTIONARY'S ----------------------------
#  Definition : a collection of {key:value} pairs.
#               ordered and changeable.
#               No duplicates.

students_marks = {"Srikanth" : 99,
                  "Ramu" : 65,
                  "Suresh": 90,
                  "Ramesh" : 76,
                  "Alice": 75,
                  "Peter park" : 40}
# print(len(students_marks))

# print(students_marks.keys())

# print(students_marks.values())

# print(students_marks.items())

# print(students_marks.get("Peter park")) // it will returns the value of a key.



# if students_marks.get("Srikanth"):
#     print("Student exists !!")
# else:
#     print("Student NOT exists !!")



# for key,value in students_marks.items():
#     print(f"{key:10}:{value}")



# students_marks.update({"Srikanth": 100})
# print(students_marks)

# students_marks.pop("Peter park") # it removes a key:value pair.

# students_marks.popitem() # it removes latest key:value pair.
# print(students_marks.popitem()) # it will prints (or) returns latest key:value pair.
students_marks.clear()
print(students_marks)