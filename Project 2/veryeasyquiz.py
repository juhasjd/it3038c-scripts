#the following code was inspired by...

"""
Description: quiz game
Author: Aman Kharwal
Date: January 3, 2021
URL: https://thecleverprogrammer.com/2021/01/03/create-a-quiz-game-with-python/

"""

#function called checking that ask the user to guess an answer

def checking(guess, answer):
    global total
    guessing = True
    attemptNum = 0

#response given if the answer is correct

    while guessing and attemptNum < 3:
        if guess.lower() == answer.lower():
            print("WOW correct!")
            total = total + 1
            guessing = False

#response given if the answer is incorrect

        else:
            if attemptNum < 2:
                guess = input("lol sorry that's incorrect, guess again.")
            attemptNum = attemptNum + 1

#response given if answer is incorrect after 2nd attempt

    if attemptNum == 3:
        print("wrong again... the right answer is ",answer )

#total starts at 0 and increases by one for each correct answer    

total = 0
print("Answer the next 4 questions.")
quest1 = input("What does 1+1 equal? ")
checking(quest1, "2")
quest2 = input("How many states does the USA have? ")
checking(quest2, "50")
quest3 = input("What are the first three digits of Pi? ")
checking(quest3, "3.14")
quest4 = input("How many continents are there? ")
checking(quest4, "7")

#prints your score out of the max score possible

print("Your Score is "+ str(total) + "/4, play again soon!")