# and = it requires both conditions to be true!
# or = it requires any one condition to be true!
# not = it will prints opposite condition!

temp = int(input("Enter your temperature : "))
sunny = str(input("Is sunny outside ?(T/F) : "))
if temp >=28:
    print("Its hot outside")
elif temp >0 and temp <=23 :
    print("Its cold outside!")
elif temp >=24 and temp <=27:
    print("Its moderate temperature outside!")
elif temp == 0 :
    print("You did not type in temperature!")


if sunny == "T":
    if temp >0:
        print("Its sunny outside!")
else:
    if temp >0:
        print("Its cloudy/clear sky outside!")
