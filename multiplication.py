#Travis Hurley - nov/13/22 - HW
def multi(num1):
    test = ""
    for x in range(1,13):
        test += str(x*num1)+ (" ")
    return(test)
def main():
    print(multi(7))
main()