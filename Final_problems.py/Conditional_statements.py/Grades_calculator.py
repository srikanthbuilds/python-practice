first_sub = float(input("Enter your 1st subject marks : "))
secound_sub = float(input("Enter your 2nd subject marks : "))
third_sub = float(input("Enter your 3th subject marks : "))
fourth_sub = float(input("Enter your 4th subject marks : ")) 
fifth_sub = float(input("Enter your 5th subject marks : ")) 
sixth_sub = float(input("Enter your 6th subject marks : "))
total = first_sub + secound_sub +third_sub+fourth_sub+fifth_sub+sixth_sub
cgpa = total//6

if first_sub < 28  or secound_sub<28 or third_sub<28 or fourth_sub<28 or fifth_sub<28 or sixth_sub<28:
    print("Result       : FAILED")
elif cgpa >= 90:
    print("Result       : PASSED")
    print(f"Total marks :{total:.1f} / 600")
    print("Grade        : A")
    print(f"Percentage          : {cgpa:.1f}%")
elif cgpa >= 80:
    print("Result       : PASSED")
    print(f"Total marks :{total:.1f} / 600")
    print("Grade        : B")
    print(f"Percentage        : {cgpa:.1f}%")
elif cgpa >= 70:
    print("Result       : PASSED")
    print(f"Total marks :{total:.1f} / 600")
    print("Grade        : C")
    print(f"Percentage        : {cgpa:.1f}%")
elif cgpa >= 60:
    print("Result       : PASSED")
    print(f"Total marks :{total:.1f} / 600")
    print("Grade        : D")
    print(f"Percentage        : {cgpa:.1f}%")
elif cgpa >= 40:
    print("Result       : PASSED")
    print(f"Total marks :{total:.1f} / 600")
    print("Grade        : E")
    print(f"Percentage        : {cgpa:.1f}%")
else:
    print("Result       : PASSED")
    print(f"Total marks :{total:.1f} / 600")
    print("Grade        : E")
    print(f"Percentage        : {cgpa:.1f}%")

    