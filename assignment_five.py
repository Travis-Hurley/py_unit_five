# Assignment five - guessing - Travis Hurley - dec-7-22

import random
average = 0
def get_guess(average):
    test = ""
    for x in range(3):
        number = random.randint(1, 5)
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

def main():
    print("Welcome to my guessing game!")
    get_guess(average)
    all = average/3
    print("Your average guess per game was "+str(all))
main()