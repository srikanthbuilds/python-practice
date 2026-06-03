PhooneBook = dict()
while True:
    print("--- PhoneBook ---")
    print("1.Add")
    print("2.Update")
    print("3.Delete")
    print("4.view")
    print("5.Exit")
    option = int(input("Enter an option to perform operation : "))
    if option == 1:
        name = input("Enter name : ")
        number = int(input("Enter number : "))
        if name not in  PhooneBook:
            PhooneBook[name] = number
            print("Added!")
        else:
            print("Already Existed contact!")
    elif option == 2:
        old_name = input("Enter old name : ")
        if old_name not in PhooneBook:
            print("Not exists!")
        else:
            new_name = input("Enter new name : ")
            PhooneBook[new_name] = number
            if new_name != name:
                PhooneBook.pop(name)
            o1 = input("Do you wanna update number (Y/N): ")
            if o1 == "Y":
                new_number = int(input("Enter new number : "))
                PhooneBook[new_name] = new_number
                print("Updated number successfully!")
    elif option == 3:
        name = input("Enter name to delete : ")
        if name not in PhooneBook:
            print("Not Exists!")
        else:
            PhooneBook.pop(name)
            print("Deleted!")
    elif option == 4:
        print("Saved contacts: ")
        for name,numbers in PhooneBook.items():
            print(f"{name} : {numbers}")
    elif option == 5:
        print("GoodBye!")
        break        
    else:
        print("Invalid option! Please try again.")




