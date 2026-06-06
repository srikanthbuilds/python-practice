def vowelscount(string):
    count = 0
    string = string.upper()
    vowels = "AEIOU"
    for char in string:
        if char in vowels:
            count +=1
    print(f"Vowels count of word - {string} are : {count}")
vowelscount("srikanth parikibanda")

