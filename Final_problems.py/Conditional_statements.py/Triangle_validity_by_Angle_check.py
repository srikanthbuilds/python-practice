print("----- Triangle validity checking programme by angle -----")
side_1 = int(input("Enter your 1st side angle : "))
side_2 = int(input("Enter your 2nd side angle : "))
side_3 = int(input("Enter your 3rd side angle : "))
if side_1 + side_2 + side_3 == 180:
    print()
    print("Accepted as a Triangle.")
    print()
else:
    print()
    print("NOT Accepted as a Triangle.")
    print()
