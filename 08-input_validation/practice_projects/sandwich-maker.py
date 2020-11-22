import pyinputplus as pyip

prices = {'wheat': 1,
          'white': 2,
          'sordough': 3,
          'chicken': 2,
          'turkey': 1.5,
          'ham': 4,
          'tofu': 0.5,
          'cheddar': 1,
          'Swiss': 3,
          'mozzarella': 5,
          }

for key, value in prices.items():
    print('%s = $%0.2f' %(key, value))

print()

cost = 0

options = []

options.append(pyip.inputMenu(['wheat', 'white', 'sordough']))  # breadType

print()

options.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu']))  # proteinType

print()

cheese =  pyip.inputYesNo(prompt='Do you want cheese? ')
if cheese == 'yes':
    options.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella']))  # cheesetype

addons = pyip.inputYesNo(prompt='Do you want mayo, mustard, lettuce or, tomato? ($4) ')  # 4

print()

numSandwiches = pyip.inputInt(prompt='How many sandwiches do you want? ', min=1)

for option in options:
    cost += prices[option]

if addons:
    cost += 4

cost *= numSandwiches

print('\nTotal cost: $%0.2f' %(cost))
