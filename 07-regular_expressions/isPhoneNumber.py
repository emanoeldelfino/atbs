def isPhoneNumber(text, country='US'):
    if country == 'BR':
        if len(text) != 13:
            return False
        for i in range(0, 2):
            if not text[i].isdecimal():
                return False
        if text[2] != ' ':
            return False
        if text[3] != '9':
            return False
        for i in range(4, 8):
            if not text[i].isdecimal():
                return False
        if text[8] != '-':
            return False
        for i in range(9, 13):
            if not text[i].isdecimal():
                return False
        return True
    elif country == 'US' or country == 'USA':
        if len(text) != 12:
            return False
        for i in range(0, 3):
            if not text[i].isdecimal():
                return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True
    else:
        return None


print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

print('47 98481-9147')
print(isPhoneNumber('47 98481-9147', country='BR'))
print('ALOALO')
print(isPhoneNumber('ALOALO', country='BR'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
