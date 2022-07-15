def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
        if not text[i].isdecimal():
            return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
#it will only print the first phone number
message = ('call me at 123-456-7890. 123-456-7899 is my office.')

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
