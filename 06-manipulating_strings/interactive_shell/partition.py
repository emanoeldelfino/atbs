print('Hello, world!'.partition('w'))  # ('Hello, ', 'w', 'orld!')
print('Hello, world!'.partition('world'))  # ('Hello, ', 'world', '!')
print('Hello, world!'.partition('o'))  # ('Hell', 'o', ', world!')
print('Hello, world!'.partition('XYZ'))  # ('Hello, world!', '', '')

# packing/unpacking
before, sep, after = [1, 2, 3]
print(before, sep, after)

before, sep, after = {1, 2, 3}
print(before, sep, after)

before, sep, after = {1: 'one', 2: 'two', 3: 'three'}
print(before, sep, after)

before, sep, after = 'Hello, world!'.partition(' ')
print(before, sep, after, sep='\n')
