'''
 * Bryan Chen
 * 11-11-2025
 * @version 1.0
 * Description: a guessing game python program
'''


import random

def guessing_game():
    #setting my upper and lower bounds. asking the user to pick between 2 numbers chosen at random with upper and lower limits I set.
    lower_bound = random.randint(1, 25)
    upper_bound = random.randint(75, 100)
    #my randomly generated number using the random library
    my_number = random.randint(lower_bound, upper_bound)
    

    #a variable to hold the number of attempts tried by the user
    attempts = 0

    print(f"hi, can you guess my number?\n I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            #gets the user's input
            guess_str = input("enter your guess: ")
            #converts the user's string input into int so I can compare the variables to actual numbers.
            guess = int(guess_str) 
            
            # increment attempt counter, your first guess is already +1 counter. so this is 0+1 attempts before the loops
            attempts += 1
            
            # checks the guess
            if guess < my_number:
                print("your number is too low!")
            elif guess > my_number:
                print("your number is too high!")
            else:
                print(f"wow! you guessed my number which is {my_number}, in {attempts} attempts.")
                break # exit the loop because the guess is correct
        
        except ValueError:
            # handle the cases where the user does not enter a valid number. this does not add to attempts counter
            print("invalid input. please enter a whole number.")

# this calls the function and starts the game
guessing_game()

    