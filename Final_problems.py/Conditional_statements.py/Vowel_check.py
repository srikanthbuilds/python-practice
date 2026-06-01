print("---  Vowel or Consonent checking programe ---")
string = str(input("Enter a Character to check : "))

if (string == "a"or string == "e"or string == "i"or string == "o"or string == "u") or (string == "A"or string == "E"or string == "I"or string == "O"or string == "U"):
    print(f"{string} is a VOWEL.")
else:
    print(f"{string} is a CONSONANT.")