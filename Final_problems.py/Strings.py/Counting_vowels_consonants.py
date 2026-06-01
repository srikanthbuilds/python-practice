word = input("Enter your word : ")
vowels_count = 0
consonants_count=0
for char in word:
    if char.upper() == "A":
        vowels_count += 1
    elif char.upper() == "E":
        vowels_count += 1 
    elif char.upper() == "I":
        vowels_count += 1 
    elif char.upper() == "O":
        vowels_count += 1 
    elif char.upper() == "U":
        vowels_count += 1 
    else:
        if char.upper() == " ": 
            pass
        else:
            consonants_count+=1
            
print(f"Vowels count     : {vowels_count}")
print(f"Consonants count : {consonants_count}")
print(f"Total letters : {vowels_count + consonants_count}")

