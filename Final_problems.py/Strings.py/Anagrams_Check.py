word1 = input("Enter your first word : ")
word2 = input("Enter your secound word : ")
if word1 ==  word2 :
    print("Both words have same letters order.")
    if sorted(word1.lower()) == sorted(word2.lower()):
        print("Yes, they are ANAGRAMS!")
    else:
        print("No, they are NOT ANAGRAMS!")
else:
    if sorted(word1.lower()) == sorted(word2.lower()):
        print("Yes, they are ANAGRAMS!")
    else:
        print("No, they are NOT ANAGRAMS!")

# Anagram means, the letters/characters are same in two words, even if the letters are in different order. 