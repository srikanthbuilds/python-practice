sentence = input("Enter your sentence : ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"From your sentence, the longest word is : '{longest_word}'")