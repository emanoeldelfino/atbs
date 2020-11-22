string = 'Abc abc'

# print(string.istitle())  # False, returns True if all words starts with capital letter.

# string2 = 'Abc Abc'
# print(string2.istitle())  # True


def get_age(txt):
    while True:
        age = input(txt)
        if age.isdecimal():
            break
        print('Please enter a number for your age.')


def get_password(txt):
    while True:
        password = input(txt)
        if password.isalnum():
            break
        print('Passowrd can only have letters and numbers.')


# Main Program
age = get_age('Enter your age: ')
password = get_password('Enter your password: ')
