spam = {'name': 'Pooka', 'age': 5}

# if 'color' not in spam:
#     spam['color'] = 'black'

# print(spam)

spam.setdefault('color', 'black')  # Returns black
print(spam)

spam.setdefault('color', 'white')  # spam already has a key named 'color' so it's not changed
print(spam)
