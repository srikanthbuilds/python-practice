# JSON file : it has a dictionary of key-value pairs!

import json
employee ={
   "name" :"srikanth",
   "age":20,
   "salary":"1cr"
   
}


file_path = "C:\\Users\\Owner\\OneDrive\\Desktop\\output.json"
try:
    with open(file_path,"w") as file:
        json.dump(employee,file,indent=4)
        print(f"Json '{file_path}' file is created! ")

except FileExistsError:
  print(f"That file ' {file_path} ' already exists")