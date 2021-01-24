#This program is to guess a number
import random
print('Guess a number between 1 to 7')

random_number=random.randint(1,7)

print(' Rules of the Game: The user has to guess the number in 6 tries, else he will be disqualified')

for i in range(1,7):
    print('Take a guess')
    guessed_number=int(input())
    
    if guessed_number < random_number:
        print('Your guess is low')

    elif guessed_number > random_number:
            print('Your guess is high')
    else:
        break # this condition is a correct guess
    
if guessed_number==random_number:
    print('Nice job, you guessed it right')
    
