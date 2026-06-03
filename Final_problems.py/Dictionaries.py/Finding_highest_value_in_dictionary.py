n = int(input("Enter how many values do you want to enter ? : "))
numbers_dict = dict()
for num in range(n):
    print(f"--- Entering value for value #{num + 1} ---")
    values = f"value {num+1}"
    number =  int(input(f"Enter value {num+1} : "))
    numbers_dict[values] = number
highest_number = list(numbers_dict.values())[0]
highest_value = ""
for keys,value in numbers_dict.items():
    if value >= highest_number:
        highest_number = value
        highest_value = keys
print(f"--- Your 'value:number' dictionary ---")
print(numbers_dict)
print(f"--- Your highest number ---")
print(f"{highest_value} : {highest_number}")


    
