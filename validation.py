def get_input():
    while True:
        number=int(input("Enter a number between 1 and 10 > "))
        if 10>=number>=1:
            break
    return number


def main():
    print(get_input())


if __name__ == '__main__':
    main()
