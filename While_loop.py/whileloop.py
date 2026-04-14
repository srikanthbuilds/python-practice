#  While loop : it executes some code until a conditon is true.

user_name = input("Enter your name : ")

while user_name == "" or user_name == " ":
    print("You did not enter your name!")
    user_name = input("Enter your name :")
print(f"Hello, Welcome {user_name}!")