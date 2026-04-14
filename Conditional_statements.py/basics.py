# if : checks the condition is true or false ?
# -> if the condition is true it execute the code
# -> if the condition is false it will goes to next condition like elif Or else condition !!


# elif : if the 'if' condition is false , it will goes into elif condition!
# -> if 'elif' condition is also false , it will goes into 'else' condition!

# else : if both the conditions , 'if' & 'elif' were false , it will goes into 'else' condition!


# age program to demonstrate condtional statements !

age = int(input("Enter your age : "))

if age>=60:
    print("You are a senior member , you are signed up!")
elif age>=18:
    print("You are signed up!")
else:
    print("You must be 18+ to sign up!")