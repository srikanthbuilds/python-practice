# ------------------ QUIZ GAME ------------------------------------
questions = ("How many bones are there in human body ?",
            "A leap year contains how many days ?",
            "Which gas is most abundant gas in earth's atmosphere ?",
            "which animal lays largest egg ?",
            "How many letters contains in alphabets ?")
options = (("A. 207","B. 208","C. 209","D. 206"),
           ("A. 365","B. 366","C. 367","D. 368"),
           ("A. Oxygen","B. Carbon-dioxide","C. Hydrogen","D. Nitrogen"),
           ("A. Whale","B. Ostrich","C. Eagle","D. Chicken"),
           ("A. 26","B. 27","C. 20","D. 24"))
answers = ("D","B","D","B","A")
gueses = []
score = 0
question_no = 0


print("------------------- QUIZ GAME --------------------------")
for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[question_no]:
        print(option)

#  input options from user
    guess = input("Enter (A,B,C,D) : ").upper()
    gueses.append(guess)
    if guess == answers[question_no]:
        print("CORRECT !!")
        score +=1
    else:
        print("INCORRECT !!")
        print(f"{answers[question_no]} is Correct!")
    question_no += 1
#  result / score 

print("_____________________________________________")
print()
print("                  RESULTS                    ")
print("_____________________________________________")
print()
print("Your answers     : ",end ="")
for guess in gueses:
    print(guess,end =" ")
print()
print("Original answers : ",end ="")
for answer in answers:
    print(answer,end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is    : {score}%")
print()


