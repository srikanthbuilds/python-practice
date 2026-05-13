import random

def spin_row():
    symbols = ["🍉", "🍋", "🍒", "🥝", "⭐"]
    return [random.choice(symbols)for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "⭐":
            return bet * 10
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🥝":
            return bet * 3
        elif row[0] == "🍒":
            return bet * 2
    return 0

def main():
    print("--------------------------------------")
    print("     Welcome to slot machine game     ")
    print("--------------------------------------")

    print("Symbols : 🍉 🍋 🍒 🥝 ⭐")


    balance = 100
    print(f"Current balance : ${balance}")


    while balance > 0:
        bet = input("Place your bet amount ? : $")
        if not bet.isdigit():
            print("Inavild entry!")
            continue
        bet = int(bet)

        if bet <= 0:
            print(f"Bet amount must be greater than 0")
            continue
        elif bet > balance:
            print("Insufficient funds")
            continue
        balance -= bet
        print("Spinning...")
        print("-------------")
        row = spin_row()
        print_row(row)
        print("-------------")
        payout_amount = payout(row,bet)
        balance += payout_amount
        if payout_amount > 0:
            print(f"You won {payout_amount}")
            print(f"Current balance : ${balance}")


        else :
            print("Sorry you lost this round!")
            print(f"Current balance : ${balance}")
        
        play_again = input("Wanna play again ? (Y/N): ").upper()
        if play_again != "Y":
            print("Good bye!")
            break
        else:
            continue  
    print("------------------20----------------------")
    print(f"Game over , your balance is ${balance}")
    print("----------------------------------------")
main()
