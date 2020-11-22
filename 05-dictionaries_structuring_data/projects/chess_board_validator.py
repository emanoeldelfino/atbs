def isValidChessBoard(board):

    bking = wking = False

    bpieces = wpieces = wpawn = bpawn = 0

    for v in board.values():
        if v[0] == 'b':
            bpieces += 1
            if v == 'bking':
                bking = True
            if v == 'bpawn':
                bpawn += 1
        elif v[0] == 'w':
            wpieces += 1
            if v == 'wking':
                wking = True
            if v == 'wpawn':
                wpawn += 1
        else:
            return False

        if v[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            return False

    if not wking or not bking or bpieces > 16 or wpieces > 16 or bpawn > 8 or wpawn > 8:
        return False

    for k in board.keys():
        if k[0] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return False
        elif k[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False
        else:
            return True


board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
board2 = {'1h': 'bking', '6c': 'wque', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(board1))  # True
print(isValidChessBoard(board2))  # False
