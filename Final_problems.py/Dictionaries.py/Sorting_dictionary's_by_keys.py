n = int(input("Enter how many elements do you want to enter ? : "))
Dictionary = dict()
for num in range(n):
    print(f"--- Entering value for value #{num + 1} ---")
    Keys = input(f"Enter key (number/alphabet): ")
    Values =  input(f"Enter value {num+1} : ")
    Dictionary[Keys] = Values
print(f"-- Sorted keys ---")
print(sorted(Dictionary.keys()))