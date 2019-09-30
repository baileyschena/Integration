#Inegration by Bailey Schena
#Program is going to start as a quiz or riddle thing.
#Adding a tally function, will print at the end of each question.
numCorrect = 0
print("Hello! Welcome to my easy quiz")
#Question One (Multiple Choice)
print("What is the order of operations?")
print("1. PEMDAS")
print("2. PEMSAD")
print("3. DASMEP")
print("4. Whats an operation?")
answer = input("To select an answer, type in the corresponding number, and press enter: ")
answernum = int(answer)
print(answernum)
if(answernum == 1):
    print("Good job! The answer is correct!")
    numCorrect = numCorrect + 1
else:
    print("Sorry, the answer is incorrect.")
print(numCorrect)
#Question Two (Math Problem)
print("What is 5-2?")
answer = input("Type the answer, and hit enter: ")

answernum = int(answer)
print(answernum)
if(answernum == 3):
    print("Good job! The answer is correct!")
    numCorrect = numCorrect + 1
else:
    print("Sorry, the answer is incorrect.")
print(numCorrect)

#Question Three (Math Problem)
print("What is 3+5?")
answer = input("Type the answer, and hit enter: ")

answernum = int(answer)
print(answernum)
if(answernum == 8):
    print("Good job! The answer is correct!")
    numCorrect = numCorrect + 1
else:
    print("Sorry, the answer is incorrect.")
print(numCorrect)

#Question Three (True or false)
print("The first letter of the word Apple is B.")
answer = input("Type the answer, and hit enter: ")
print("1. True")
print("2. False")

answernum = int(answer)
print(answernum)
if(answernum == 2):
    print("Good job! The answer is correct!")
    numCorrect = numCorrect + 1
else:
    print("Sorry, the answer is incorrect.")
print(numCorrect)
    
print("Thank you for playing!")
print("Your total correct was: ", numCorrect)

