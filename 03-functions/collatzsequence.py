import sys


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        integer = int(input('Type a number: '))
        if integer != abs(integer):
            raise ValueError
    except (ValueError, TypeError):
        print('You must enter a non negative integer.')
    except KeyboardInterrupt:
        sys.exit()
    else:
        break

while True:
    integer = collatz(integer)
    if integer == 1:
        break
