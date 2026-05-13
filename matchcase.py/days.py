def day_of_week(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return True
        case "tuesday":
            return True
        case "wednesday":
            return True
        case "thursday":
            return True
        case "friday":
            return True
        case "saturday":
            return True
        case _:
            print("invalid !!")

print(day_of_week("thursday"))

