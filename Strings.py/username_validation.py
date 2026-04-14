user_name = str(input("Enter your name :"))
if len(user_name) > 12:
    print("username cannot contains more than 12 characters!") 
elif not  user_name.find(" ") <= -1:
    print("username does not contains space!")
elif not user_name.isalpha() :

    print("Username cannot contains digits!") 
else :
    print(f"Hello, welcome {user_name}")