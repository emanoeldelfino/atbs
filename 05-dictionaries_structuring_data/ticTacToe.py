theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

'''
# player X went first and chose the middle space:
theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': 'X', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}

# A board where player O has won by placing Os across the top might look like this:
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
'''


def printBoard(board):
    print(f'  {board["top-L"]} | {board["top-M"]} | {board["top-R"]}')
    print(' ---+---+---')
    print(f'  {board["mid-L"]} | {board["mid-M"]} | {board["mid-R"]}')
    print(' ---+---+---')
    print(f'  {board["low-L"]} | {board["low-M"]} | {board["low-R"]}')


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(f'Turn for {turn}. Move on which space?')
    move = input(' > ')
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
