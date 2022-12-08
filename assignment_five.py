# Assignment five - guessing - Travis Hurley - dec-7-22

import random
average = 0
total=0

def get_number():
    number = random.randint(1, 2)
    return number
def get_guess(average,total,number):
    test = ""
    for x in range(3):
        get_number()
        while True:
            guess = int(input("What is your guess? > "))
            if guess<number:
                average += 1
                print("Higher! ")
            elif guess>number:
                average += 1
                print("Lower! ")
            else:
                average += 1
                average -= abs(total)
                abs(average)
                total+=average
                print("this is total "+str(total))
                print("Yes! That is it! It took you "+str(average)+" guesses to get the number.")
                break
    print("This is total "+str(total))
    comb=total/3
    new=round(comb,2)
    print("Your average per game was " +str(new) +" guesses.")


def main():
    number=get_number()
    print("Welcome to my guessing game! Try and guess my number between 1-100.")
    get_guess(average,total,number)
    print("Thank your for playing!")
main()
