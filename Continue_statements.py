#This will be for a continue statement in a loop(Not Sure.. if we can use the continue statement out side of any conditional loop statements, this is used , when we want to have the loop to skip consecutive indented statements and to get back to the beggining of the loop
spam=0

while spam < 5:
    spam=spam+1
    if spam==3:
        continue
    print(spam)
    


print('Thank you')
