def isphoneNumber(text):
    if len(text) != 12:
        return False    # Phone number should be 12 digits
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-': 
        return False    # missing # in between
    
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # if the next set of 3 numbers are not numbers
        
    if text[7] != '-':
        return False    # if there is a missing dash in between

    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


##print(isphoneNumber('123-456-7899'))
##print(isphoneNumber('Mahesh'))

print("Type in your message")
message=input()

foundNumber = False
for i in range(len(message)):
    chunk=message[i:i+12]
    if isphoneNumber(chunk):
            print("Phone Number Found : ", chunk)
            foundNumber = True

if not foundNumber:
    print('Could Not find a number')


