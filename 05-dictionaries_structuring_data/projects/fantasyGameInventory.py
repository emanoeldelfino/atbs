def displayInventory(inventory):
    total_items = 0
    items = sorted(inventory.items())

    print('Inventory: ')
    for k, v in items:
        print(f'{v:>2} {k}')
        total_items += v
    print(f'Total number of items: {total_items}.')


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)


# Part 2
def addToInventory(inventory, addedItems):
    new_items = {}
    for item in addedItems:
        new_items.setdefault(item, 0)
        new_items[item] += 1

    for item, number in new_items.items():
        inventory.setdefault(item, 0)
        inventory[item] += number

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
