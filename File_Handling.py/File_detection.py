import os
file_path = "C:\\Users\\parik_6r4phsv\\OneDrive\\Desktop\\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' is found!")
    if os.path.isfile(file_path):
        print("it is a file")
    elif os.path.isdir(file_path):
        print("it is not a file !")
else :
    print("Not exists!")