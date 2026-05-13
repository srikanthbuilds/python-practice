import os

file_path = "C:\\Users\\Owner\\OneDrive\\Desktop\\output.txt"

with open(file_path,"r") as file:
    content = file.read()
    print(content)