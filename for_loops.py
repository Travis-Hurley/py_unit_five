#Travis Hurley, Nov-13-22
"""
def count(number, number2):
    for x in range(number, number2):
        return(x)

def main():
    print(count(0,7))
if __name__ == '__main__':
    main()
"""
def count(number1,number2):
    test = ""
    for x in range(number1,1+number2):
        test += str(x)+(" ")
    test2 = ""
    for x in range(number2,number1-1,-1):
        test2 += str(x)+(" ")
    return "Counting up > "+str(test)+ "         " +"Counting down > "+str(test2)
def fake_main():
    print(count(0,6))

"""look at real_count for the HW"""
def real_count(num1,num2):
    if num1>num2:
        real1 = ""
        for x in range(num1,num2-1,-1):
            real1 += str(x)+(" ")
        return real1
    elif num1<num2:
        real2 = ""
        for x in range(num1,num2+1):
            real2 += str(x) + (" ")
        return real2
def main():
    print(real_count(6,0))
main()