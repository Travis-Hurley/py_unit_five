def get_sum(number):
    sum=0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            sum += (x)
    print(sum)
get_sum(10)

