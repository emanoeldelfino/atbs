print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))

print('My name is Simon'.split(maxsplit=2))

print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))
