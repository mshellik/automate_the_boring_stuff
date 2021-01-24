#This script is used for try/except block

def divideBy(num):

    try:
        return (42/num)
    except ZeroDivisionError:
        print("you are trying to divide a number by zero")

print(divideBy(2))
print(divideBy(12))
print(divideBy(0))
print(divideBy(1))
