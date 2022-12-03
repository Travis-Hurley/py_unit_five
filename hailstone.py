
def sequence(number):
    step = 0
    while True:
        if number%2 == 1:
           number = (number*3)+1
        elif number%2 == 0:
            number = number/2
        step+=1
        if number == 1:
            break
    return(step)
def main():
    print(sequence(13))
main()