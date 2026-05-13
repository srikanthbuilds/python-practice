ch = input("Enter a character :  ")

if ch.lower() in ['a','e','i','o','u']:
    print(f"{ch} is a 'Vowel'")
else:
    print(f"{ch} is 'Not a vowel'")