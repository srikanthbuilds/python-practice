num = 6
a = 6 
b = 7
age = 17
temp = 30
user_roll = "Admin"

# print("Positive" if num>0 else "Negative")
# result = "even" if num %2==0 else "odd"
# maxnum = a if a>b else b
# print(maxnum)
# minnum = a if a<b else b
# print(minnum)
# status = "Adult"if age >= 18 else "Child"
# temp = "Hot" if temp >= 30 else "Cold"
access = "You can have Full access! " if user_roll == "Admin" else "Limited access" 
print(access)

# Id verification programme 

id = int(input("Enter your Id number :"))
name =str(input("Enter your name :"))
result = "Verified" if id == 208 and name == "srikanth" else "Not verified !!"
print(result)

