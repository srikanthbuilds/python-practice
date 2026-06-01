string = input("Enter your string : ")
string1 = ""
print("Here's your string with uppercase : ")
for char in string:
    char = char.capitalize()
    print(char,end="")