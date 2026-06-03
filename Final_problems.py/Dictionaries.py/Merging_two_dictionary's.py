n1 = int(input("Enter how many values do you want for dict 1 ? : "))
numbers_dict1 = dict()
for num in range(n1):
    print(f"--- Entering in dictionary - 1 for  value #{num + 1} ---")
    values = f"d1 v{num+1}"
    number =  int(input(f"Enter value {num+1} : "))
    numbers_dict1[values] = number
n2 = int(input("Enter how many values do you want for dict 1 ? : "))
numbers_dict2 = dict()
for num in range(n2):
    print(f"--- Entering in dictionary - 2 for value #{num + 1} ---")
    values = f"d2 v{num+1}"
    number =  int(input(f"Enter value {num+1} : "))
    numbers_dict2[values] = number
merging_dictionary = dict()
for key, val in numbers_dict1.items():
    merging_dictionary[key] = val
for key,val in numbers_dict2.items():
    merging_dictionary[key] = val
print(f"--- Dictionary's ---")
print(f"Dictionary 1: {numbers_dict1}")
print(f"Dictionary 2: {numbers_dict2}")
print(f"Merged Dictionary: {merging_dictionary}")