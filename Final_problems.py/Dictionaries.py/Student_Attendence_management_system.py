Attendence_dates = dict()
while True:
    print("----- Student Attendence Management System -----")
    print("1. Mark attendence on a particular date")
    print("2. View attendence for a particular date")
    print("3. View attendence for a particular student")
    print("4. Exit")
    option = int(input("Enter your optinon : "))
    if option == 1:
        date = (input("Enter date (DD/MM/YY): "))
        if date in Attendence_dates:
            print(f"On {date} You took attendence Already!")
        else:
            Attendence_dates[date] = dict()
            while True:
                name = input("Enter student name: ")
                attendence = input(f"Is {name} present? (P/A) : ")
                if attendence.upper() != "P" and attendence.upper() != "A":
                    print("Invalid input! Please enter 'P' for present or 'A' for absent.")
                    continue
                else:
                    Attendence_dates[date][name] = attendence
                exit_choice = input("Do you wanna add more students? (Y/N) : ")
                if exit_choice.upper() == "Y":
                    continue
                elif exit_choice.upper() == "N":
                    break
            
    elif option == 2:
        date = input("Enter date : ")
        if date in Attendence_dates:
            print(f"--- Attendence on {date} ---")
            for names,attends in Attendence_dates[date][name]:
                print(f"Name : {names} | {attends}")
    