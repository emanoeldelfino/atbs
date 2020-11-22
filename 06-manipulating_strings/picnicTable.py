def print_picnic(itemsDict, left_width, right_width):
    total_width = left_width + right_width + 3
    print(f'+{" PICNIC ITEMS ".center(total_width, "-")}+')
    for k, v in itemsDict.items():
        print(f'| {k.ljust(left_width, ".")} {str(v).rjust(right_width)} |')
    print('+' + '-' * total_width + '+', '\n')


picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
