# Integration by Bailey Schena
# Program is going to start as a quiz or riddle thing.
# Adding a tally function, will print at the end of each question.

score = 0


def tallyChange(firstInput):
    global score
    score = score + firstInput


def main():
    global score
    replay = 1
    while replay == 1:

        print("Hello! Welcome to my easy quiz")
        # Question One (Multiple Choice)
        print("What is the order of operations?")
        print("1. PEMDAS")
        print("2. PEMSAD")
        print("3. DASMEP")
        print("4. Whats an operation?")
        answer = input("To select an answer, type in the corresponding number, and press enter: ")
        answerNum = int(answer)

        if answerNum == 1:
            print("Good job! The answer is correct!")
            tallyChange(1)
        elif answerNum == 9001:
            secretArea()
        else:
            print("Sorry, the answer is incorrect.")

        print("")
        print("")
        print("")

        # Question Two (Math Problem)
        print("What is 5-2?")
        answer = input("Type the answer, and hit enter: ")

        answerNum = int(answer)

        if answerNum == 3:
            print("Good job! The answer is correct!")
            tallyChange(1)
        else:
            print("Sorry, the answer is incorrect.")

        print("")
        print("")
        print("")

        # Question Three (Math Problem)
        print("What is 3+5?")
        answer = input("Type the answer, and hit enter: ")

        answerNum = int(answer)

        if answerNum == 8:
            print("Good job! The answer is correct!")
            tallyChange(1)
        else:
            print("Sorry, the answer is incorrect.")

        print("")
        print("")
        print("")


        # Question Three (True or false)
        print("The first letter of the word Apple is B.")
        print("1. True")
        print("2. False")
        answer = input("Type the answer, and hit enter: ")

        answerNum = int(answer)

        if answerNum == 2:
            print("Good job! The answer is correct!")
            tallyChange(1)
        else:
            print("Sorry, the answer is incorrect.")

        print("")
        print("")
        print("")

        print("Thank you for playing!")

        print("Your total correct was: ", score)

        print("Would you like to play again? 1 for yes, 2 for no")
        replay = int(input())
        score = 0

        print("")
        print("")
        print("")


def secretArea():
    print("Nice find")


main()
