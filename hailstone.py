
def sequence(number):
    step = 0
    while True:
        if number%2 == 1:
           number = (number*3)+1
           print(number)
        elif number%2 == 0:
            number = number/2
            print(number)
        step+=1
        if number == 1:
            break
        print(step)
def main():
    sequence(13)
main()