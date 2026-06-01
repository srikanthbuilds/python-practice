def weekend(day):
    match day:
        case "sunday"|"saturday":
            return True
        case "monday" |"tuesday"| "wednesday"|"thursday"|"friday":
            return False
        case _:
            print("invalid !!")

print(weekend(input("Enter your day :")))
