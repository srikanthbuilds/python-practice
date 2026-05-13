import os
txt_data = "I like pizza & sandwiches!"
txt_employees = ["srikanth","suman","patrick","bob"]

file_path = "C:\\Users\\Owner\\OneDrive\\Desktop\\output.txt"
try:
    with open(file_path,"w") as file:
        for employee in txt_employees:
           file.write("\n"+employee)
        print(f"'{file_path}' file is created! ")

except FileExistsError:
  print(f"That file ' {file_path} ' already exists")