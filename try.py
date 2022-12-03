def get_input():
    """
    This function ensures that a user correctly enters a number and not a string in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    while True:
        try:
            userInput = int(input("Please enter a number between 1 and 10: "))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput >= 1 and userInput <= 10:
                return userInput
get_input()