# Assignment five - guessing - Travis Hurley - dec-7-22

import random
average = 0 #creates average and total to be used in get_guess
total=0

def get_number(): #Generates random number
    number = random.randint(1, 20)
    return number
def get_guess(average,total,number): #runs the guessing game
    test = ""
    for x in range(3): # Runs the game three times
        get_number() # gets Random number for game
        while True: # Creates a loop unil they guess the correct number
            guess = int(input("What is your guess? > ")) #Prompts the user for the guess
            if guess<number:
                average += 1
                print("Higher! ")
            elif guess>number:
                average += 1
                print("Lower! ")
            elif guess==number:
                average += 1
                total += average
                print("Yes! That is it! It took you "+str(average)+" guesses to get the number.")
                print(" ")
                average=0
                break # ends the loop for correct number
    comb=total/3
    new=round(comb,2)
    print("Your average per game was " +str(new) +" guesses.")

def main():
    number=get_number()
    print("Welcome to my guessing game! Try and guess my number between 1-100.")
    print(" ")
    get_guess(average,total,number)
    print("Thank your for playing!")
main()