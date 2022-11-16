def fibonacci(num):
    a=1
    b=1
    test = ""
    for x in range(num-2):
        c = a + b
        a = b
        b = c
        test += str(c) + (" ")
    return test
def main():
    num=int(input("How many numbers would you like? > "))
    if num==1:
        print(str(1) + " " + fibonacci(num))
    else:
        print(str(1)+(" ")+str(1)+" "+fibonacci(num))
main()