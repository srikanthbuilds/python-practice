# CSV : comma separated value's.
import csv

employees = [["name","age","grade"],
             ["srikanth",20,"A"],
             ["patrick",19,"C"],
             ["sandy",23,"D"],
             ["peter park",18,"B"]]


file_path = "C:\\Users\\Owner\\OneDrive\\Desktop\\output.csv"
try:
    with open(file_path,"w",newline= "") as file:
        writer = csv.writer(file)
        for row in employees:
           writer.writerow(row)
        print(f"CSV '{file_path}' file is created! ")

except FileExistsError:
  print(f"That file ' {file_path} ' already exists")