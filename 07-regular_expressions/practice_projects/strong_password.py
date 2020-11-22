def password_strength(password):
    """
    -> Validates a password strength.
    :password: mandatory, the password that's going to be tested.
    """
    import re

    regexes = {
        'Length 8 characters': r'\w{8,}',
        'Lowercase character': r'[a-z]',
        'Uppercase character': r'[A-Z]',
        'One digit': r'\d',
    }

    checks = []

    for name, reg_pattern in regexes.items():
        regex = re.compile(reg_pattern)
        mo = regex.search(password)
        checks.append(mo != None)
        print(f'{name} = {mo != None}')

    if False in checks:
        return False
    else:
        return True


while True:
    password = input('\nPassword: ')

    print()

    strong = password_strength(password=password)

    if strong:
        print('\nThat\'s a strong password!')
        break
    print('\nYour password didn\'t pass all requisites. Try again.')
