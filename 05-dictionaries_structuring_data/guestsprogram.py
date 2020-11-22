all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought


print('Number of things being brought: ')

# print(f' - Apples           {totalBrought(all_guests, "apples")}')
# print(f' - Cups             {totalBrought(all_guests, "cups")}')
# print(f' - Cakes            {totalBrought(all_guests, "cakes")}')
# print(f' - Ham Sandwiches   {totalBrought(all_guests, "ham sandwiches")}')
# print(f' - Apple Pies       {totalBrought(all_guests, "apple pies")}')

for value in ['apples', 'cups', 'cakes', 'ham sandwiches', 'apple pies']:
    print(f' - {value.title():<16} {totalBrought(all_guests, value)}')
