# Assignment five - guessing game 1-100 that calculates average guesses - Travis Hurley - dec-14-22

import random
average = 0                                  # creates average and total to be used in get_guess
total = 0


def get_number():
    '''
    this function generates random number
    :return: random integer in int form
    '''
    number = random.randint(1, 100)
    return number


def get_guess(average, total, number):
    '''
    Runs the guessing game three times while stating higher, lower, or correct in response to the guess.
    Outputs the amount of guesses per game and average over all three games
    :param average: amount of guesses per game used to add to the total for later average (int)
    :param total: total amount of guesses for all three games (int)
    :param number: the random integer (int)
    :return: does not return anything
    '''
    test = ""
    for x in range(3):                      # Runs the game three times
        number = get_number()                        # gets Random number for game
        while True:                         # Creates a loop until they guess the correct number
            guess = int(input("What is your guess? > "))  # Prompts the user for the guess
            if guess < number:              # makes if statement for if the guess is less than the number
                average += 1                # adds one to the average guesses
                print("Higher! ")           # outputs higher - then restarts the loop to prompt user to guess again
            elif guess > number:            # Makes elif statement if the guess is higher than the number
                average += 1
                print("Lower! ")            # outputs lower - then restarts the loop to prompt user to guess again
            elif guess == number:           # makes elif statement if the guess is the number
                average += 1
                total += average            # Adds the amount of guesses for previous game to the total
                print("Yes! That is it! It took you "+str(average)+" guesses to get the number.")
                print(" ")                  # makes a space, so you can visually see the break in games
                average = 0
                break                       # ends the loop for correct number
    comb = total/3                          # finds average total per game - I don't know why it is called comb
    new = round(comb, 2)                    # rounds it to the second decimal
    print("Your average per game was " + str(new) + " guesses.")


def main():
    '''
    prompts user into the game
    assigns number to random integer
    runs game
    thanks player for playiing
    :return:
    '''
    number = get_number()                   # assigns number to the random number int
    print("Welcome to my guessing game! Try and guess my number between 1-100.")
    print(" ")                              # space for visual looks
    get_guess(average, total, number)
    print("Thank your for playing!")


main()
