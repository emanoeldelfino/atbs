picnicItems = {'appels': 5, 'cups': 2}
print(f'I am bringing {picnicItems.get("cups", 0)} cups.')
print(f'I am bringing {picnicItems.get("eggs", 0)} eggs.')

picnicItems = {'apples': 5, 'cups': 2}
print(f'I am bringing {picnicItems["eggs"]} eggs') # KeyError
