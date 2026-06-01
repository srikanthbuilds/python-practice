string = input("Enter your string : ")
duplicates = []
for char in string:
    if char == " ":
        pass
    elif string.count(char) >1 and char not in duplicates:
        duplicates.append(char)
print(f"Duplicate character's from your string -'{string}'  : {duplicates}")
