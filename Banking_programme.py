

def show_balance(balance):
    print("------------------------------")
    print(f"Your balance amount is ${balance:.2f}")
    print("------------------------------")
def deposit():
    money = float(input("Enter your amount to be deposited : "))
    if money <=0:
        print("------------------------------")
        print("Can't be Zero to deposit. ")
        print("------------------------------")
        return 0
    else:
        print("------------------------------")
        print(f"${money} has successfully deposited.")
        print("------------------------------")
        return money
def withdraw(balance):
    money = float(input("Enter your amount to withdraw : "))
    if money <=0:
        print("------------------------------")
        print("Can't withdraw less than and equal to Zero.")
        print("------------------------------")
        return 0
    elif money > balance :
        print("------------------------------")
        print("Insufficient bank balance.")
        print("------------------------------")
        return 0
    else:
        print("------------------------------")
        print(f"${money:.2f} has been successfully withdrawed !!")
        print("------------------------------")
        return money


def main():
    balance = 0
    is_running = True
    while is_running:
        print("------------------------------")
        print("      Banking programme       ")
        print("------------------------------")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
            print("------------------------------")
            print("Thankyou, Have a nice day!")
            print("------------------------------")
        else :
            print("------------------------------")
            print("Invaild choice !!")
            print("------------------------------")

if __name__ == '__main__':
    main()