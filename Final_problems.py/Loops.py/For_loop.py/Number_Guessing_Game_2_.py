import random
lowest = 1
highest = 100
guess_count = 1
computer_guess = random.randint(lowest,highest)

number = int(input("Enter your number : "))
game = True
while game == True:
    if computer_guess < number:
        print("Too high!")
        number = int(input("Enter your number : "))
        guess_count += 1
    elif computer_guess > number:
        print("Too low")
        number = int(input("Enter your number : "))
        guess_count += 1
    else:
        game = False
        print(f"YOU guessed in {guess_count}th Attempt.")
