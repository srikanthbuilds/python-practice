import json

file_path = "C:\\Users\\Owner\\OneDrive\\Desktop\\output.json"
with open(file_path,"r") as file:
    content = json.load(file)
    print(content)
    print(content["name"])
    print(content["age"])
    print(content["salary"])
