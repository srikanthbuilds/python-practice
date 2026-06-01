import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
# print(chars)
# print(f"keys : {keys}")

# ENCRYPT
print("----- Welcome to message encryption program -----")

original_text = input("Enter your message to encrypt : ")
cipher_text = " "


for letter in original_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print()
print(f"Original message  : {original_text}")
print(f"Encrypted message :{cipher_text}")
print()



# DECRYPT


cipher_text = input("Enter your message to DE-encrypt : ")
original_text1 = " "


for letter in cipher_text:
    index = keys.index(letter)
    original_text1 += chars[index]

print()
print(f"De-Encrypted message :{original_text1}")
print()