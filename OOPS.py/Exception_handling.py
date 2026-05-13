"""

Exception : An event which inturupts the flow of execution!

"""

try :
    number = int(input("Enter your number : "))
    number2 = int(input("Enter your dividing number :"))
    r= number/number2
    print(F"Result : {r}")
except ZeroDivisionError:
    print("You cannot divide with zero IDIOT!")
except ValueError:
    print("Enter only number's please")
except NameError:
    print(r)
finally:
    print("exited!")