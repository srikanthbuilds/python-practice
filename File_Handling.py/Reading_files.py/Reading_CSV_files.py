import csv

file_path = "C:\\Users\\Owner\\OneDrive\\Desktop\\output.csv"
try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
           print(line)
    
    """
    
     for line in content:
           print(line[n]) , n for to print particular column!
    
    """


except FileExistsError:
  print(f"That file ' {file_path} ' already exists")