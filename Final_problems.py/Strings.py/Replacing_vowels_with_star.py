string = input("Enter your string : ")
new_text =""
for char in string :
    if char in "aeiouAEIOU":
        new_text += "*"
    else:
        new_text += char
print(f"After replacing vowels with '*' : {new_text}")