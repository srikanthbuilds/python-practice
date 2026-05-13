total_lights = {"light_1": True, "light_2": True, "light_3": True, "light_4": True, "light_5": True}

def ON_lights():
    print("--- Turned ON lights ---")
    for light, status in total_lights.items():
        if status:
            print(f"{light}: {status}")

def OFF_lights():
    print("--- Turned OFF lights ---")
    for light, status in total_lights.items():
        if not status:
            print(f"{light}: {status}")

def totallights():
    print("--- Total lights ---")
    for light in total_lights:
        print(light)

def Turn_on_lights():
    light_name = input("Enter your light name to turn ON: ")
    if light_name in total_lights:
        total_lights[light_name] = True
        print(f"{light_name} Turned ON.")
    else:
        print(f"{light_name} is not in your home.")

def Turn_off_lights():
    light_name = input("Enter your light name to turn OFF: ")
    if light_name in total_lights:
        total_lights[light_name] = False
        print(f"{light_name} Turned OFF.")
    else:
        print(f"{light_name} is not in your home.")

home = True
while home:
    print("\n----- LIGHTING SYSTEM -----")
    print("1. Show total lights")
    print("2. Show ON lights")
    print("3. Show OFF lights")
    print("4. Turn ON a light")
    print("5. Turn OFF a light")
    print("6. Exit")

    option = int(input("Enter an option (1-6): "))

    if option < 1 or option > 6:
        print("Invalid option!")
    elif option == 1:
        totallights()
    elif option == 2:
        ON_lights()
    elif option == 3:
        OFF_lights()
    elif option == 4:
        Turn_on_lights()
    elif option == 5:
        Turn_off_lights()
    elif option == 6:
        print("Goodbye!")
        home = False



