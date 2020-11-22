def orglist(lista):
    orglista = ''
    for item in lista:
        if item != lista[-1]:
            orglista += f'{item}, '
        else:
            orglista += f'and {item}.'
    return orglista


lista = ['apples', 'bananas', 'tofu', 'cats']
lista2 = orglist(lista)
print(lista2)
