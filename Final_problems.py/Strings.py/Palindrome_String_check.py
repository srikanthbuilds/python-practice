string = input("Enter your word : ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string

if string == reversed_string:
    print(f"Given string - '{string}'  is a PALINDROME string.")
else:
    print(f"Given string - '{string}'  is NOT a PALINDROME string.")
