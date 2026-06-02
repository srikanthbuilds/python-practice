sentence = input("Enter your sentence : ")
words = sentence.split()
seen_words = set()
duplicate_words =set()
for word in words:
    if word in seen_words:
        duplicate_words.add(word)
    else:
        seen_words.add(word)
unique_words = seen_words-duplicate_words
print(f"Unique words : {unique_words}")
