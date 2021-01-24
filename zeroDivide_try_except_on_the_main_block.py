def divideBy(num):
    return (42/num)


try:
    print(divideBy(2))
    print(divideBy(12))
    print(divideBy(0))
    print(divideBy(1))
except ZeroDivisionError:
    print('You are trying to divide by ZERO which is not right')
