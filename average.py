divide=0
total=0
x=0
while True:
    x = input("Would you like to add a number or quit(q)? > ")
    if x == "q":
        break
    divide += 1
    total += int(x)
y = total/divide
print("The average is "+str(y))