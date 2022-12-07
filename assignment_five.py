# Assignment five - guessing - Travis Hurley - dec-7-22

import random
average = 0
def get_guess(average):
    test = ""
    for x in range(3):
        number = random.randint(1, 2)
        while True:
            guess = int(input("What is your guess? > "))
            if guess<number:
                average += 1
                print("Higher! "+ str(average))
            elif guess>number:
                average += 1
                print("Lower! " + str(average))
            else:
                average += 1
                print("Yes! That is it!")
                print(average)
                break
    comb=average/3
    print("Your average per game was " +str(round((comb,2))) +" guesses.")

def main():
    print("Welcome to my guessing game!")
    get_guess(average)
    print("Thank your for playing!")
