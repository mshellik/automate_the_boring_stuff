def spam():
    eggs='spam local'
    print(eggs)

def bacon():
    eggs='bacon local'
    print(eggs) # prints bacon local
    spam()
    print(eggs) # print bacon local


eggs='global'
bacon()
print(eggs) # this will print global value of eggs
