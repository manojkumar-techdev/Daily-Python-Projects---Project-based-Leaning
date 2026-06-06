# Python project - Number Guessing Game

# This statement imports Python's built-in random module, which provides functions for generating random numbers and making random selections
import random


# Function creates random number from 1 - 100
def getRandomNumber():
    return random.randrange(1, 1001)

def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "Cold"
    elif number == guess:
        return "Right"
    else:
        return "Hot"

def runGuess():
    secretNumber = getRandomNumber()
    # Update the code below
    while True:
        user_guess = int(input("Enter a number between 1 and 100: "))
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it Right!")
            break
            
        else:
            print(hint)

# Call the function to run the complete project code            
runGuess()