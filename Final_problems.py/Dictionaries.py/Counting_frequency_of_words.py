words_dict1 = dict()
word_count = 0
print(f"--- Entering words in dictionary---")
while True:
    words = f"word {word_count+1}"
    word =  (input(f"Enter word (0 to quite): "))
    if word == "0":
        break
    else:
        words_dict1[words] = word 
        word_count += 1
print("--- Your words dictionary ---")
print(words_dict1)
print(f"Total words : {word_count}")