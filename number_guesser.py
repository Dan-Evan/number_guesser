#**********************************************************************************
# Name of author: Daniel Evans
# Date Created: August 11, 2021
# Description: This program will have the user enter the to range 
#              and them guess which number was selected.
# Credit: Made this base code by following along with YouTuber 'Tech with Tim' 
#         and made my own editions
#
#**********************************************************************************

import random # The random module with the randomizing function I need

# Welcome to Daniel's Number Guessing Game!
print("Welcome to Daniel's Number Guessing Game!")

# This ask the user for a number to determine the range for the number
# number they are gonna guess.
top_of_range = input("Type a number: ")

# We are first checking if the input is an digit with the if statement
# and if it is convert it to a integer and then checks if it is a whole
# number. If not it quit and tell them to type a number greater than zero next time.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()# quits the program where it is.
else:
    print("Please type a number next time.")
    quit()

#generates a random number and stores it in the variable ramdom_number using the
# number they were first asked for as the top of teh range.
random_number = random.randint(0, top_of_range)
guesses = 0# variable to track the number of guesses

while True:# This will continuously run because it is always true
    guesses += 1# incrementing the guesses to count how many guesses

    # user aked to make a guess
    user_guess = input("Make a guess: ")

    # check if the guess is a digit and converts it to a integer. If
    # not they will asked to type one next time
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue# goes back to the top of loop and repeats/

    # If all is successfull so far it will check if the number is equal 
    # to the guess and if so it will tell that they did and if not it 
    # tells them if they are above or below it number and try again.
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

# Tells th user how many guesses it took to get it correct
print("You got in", guesses, "guesses.")

# END.