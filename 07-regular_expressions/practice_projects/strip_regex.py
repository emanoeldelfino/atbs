import re


def strip(string, characters=''):

    stripRegex = re.compile(rf'{characters}') if characters else re.compile(r'^\s|\s$')

    new_string = stripRegex.sub('', string)

    return new_string

    # if not characters:
    #     stripRegex = re.compile(r'^\s|\s$')

    #     new_string = stripRegex.sub('', string)

    #     return new_string
    # else:
    #     stripRegex = re.compile(rf'{characters}')

    #     new_string = stripRegex.sub('', string)

    #     return new_string


text = ' abc '

print(text)
print(strip(text))
print(strip(text, 'a'))
print(strip(text, 'b'))
print(strip(text, 'c'))
