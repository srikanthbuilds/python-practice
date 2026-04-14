print("----- Rock - Paper - Scissor - GAME -----")
import random
options = ("rock","paper","scissor")
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter (Rock,Paper,Scissor): ").lower()

    print(f"player :{player}")
    print(f"computer :{computer}")
    if player == "rock" and computer == "scissor":
        print("You win !!")  

    elif player == "paper" and computer == "rock":
        print("You win !!")
    
    elif player == "scissor" and computer == "paper":
        print("You win !!")

    elif player == computer :
        print("Tie !!")
        
    else:
        print("You lose !!")
    
    if not input("Play again (y/n): ").lower() ==  "y":
        running = False
print("Thanks for playing :)")



    # user = input("Enter (Rock,Paper,Scissor): ").lower()
    # if user not in options:
    #     user = input("Enter (Rock,Paper,Scissor): ").lower()
    # else:

    