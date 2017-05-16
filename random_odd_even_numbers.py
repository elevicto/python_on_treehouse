import random
def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2
start = 5
while start:
    num = random.randint(1, 99)
    if even_odd(num) == True:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
    start -= 1
