catNames=[]
while True:
    print("Enter the name of the cat " + str(len(catNames)+1) + '(Or Enter Nothing to stop.):')

    name=input()
    if name == '':
        break
    catNames=catNames + [name]
print('The cat Names are ')
for names in catNames:
    print(''+ names)


##catNames = []
##while True:
##    print('Enter the name of cat ' + str(len(catNames) + 1) +
##      ' (Or enter nothing to stop.):')
##    name = input()
##    if name == '':
##        break
##    catNames = catNames + [name]  # list concatenation
##print('The cat names are:')
##for name in catNames:
##    print('  ' + name)
