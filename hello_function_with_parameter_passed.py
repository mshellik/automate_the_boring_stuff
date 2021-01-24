#This is to call the hello function with parameters.
#parameters are the values passed to a variable defined in function
#print function returns None vaule.. which is nothing .. and nothing is not printed.
#the result is always the side effect of print function.. which is stdio/print screen..
#(Not sure.what to do when the print output has to be redirected to anyother device)


def hello(name):
    print('Hello ' + name)
    print('All the best to your coding practice')


hello('Bob')
hello('Alice')
