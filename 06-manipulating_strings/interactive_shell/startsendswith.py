print('Hello, world!'.startswith('Hello'))  # True
print('Hello, world!'.endswith('world!'))  # True
print('abc123'.startswith('abcdef'))  # False
print('abc123'.endswith('12'))  # False
print('Hello, world!'.startswith('Hello, world!'))  # True
print('Hello, world!'.endswith('Hello, world!'))  # True

# startswith and endswith have two arguments, start and end, that are default do 0 and -1 respectively
