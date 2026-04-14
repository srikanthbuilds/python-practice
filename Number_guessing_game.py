#  Number guessing game !!

import random

lowest_num = 1
highest_num = 100
gueses = 0
is_running =True

answer = random.randint(lowest_num,highest_num)

print()
print("--------------- Python - Number Guessing Game --------------")
print(f"Select an number between {lowest_num} to {highest_num} ")
while is_running:
    guess = input("Enter your guess : ")
    if guess.isdigit():
        guess = int(guess)
        gueses +=1
        if guess < lowest_num or guess > highest_num  :
            print("Out of range!")
        elif guess > answer:
            print("Too High, try again!")
            print()

        elif guess < answer:
            print("Too Low, try again!")
            print()
        else:
            print()
            print("Correct !!")
            print(f"The answer was {answer}")
            print(f"You guessed in {gueses} attempts!")
            print()
            is_running = False
    else:
        print("Invaild Guess!")
        print("Please Enter your guess again")

        
    