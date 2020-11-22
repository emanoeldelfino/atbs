cat_names = []

while True:
    name = input(f'Enter the name of {len(cat_names) + 1} (Or enter nothing to stop): ')
    if name == '':
        break
    cat_names += [name]

print(f'The cat names are: ')
for name in cat_names:
    print(f' {name}')
