import random
# Heads = 0
# Tails = 1


def heads_or_tails(num=1):
    """
    -> Flip a coin 100x and see whether it gets a six streak of head or tails.

    :param num: Number of times to flip the coin and get an output.
    """
    lista = []
    heads = tails = streaks = 0
    for n in range(num):
        lista.append('H' if random.randint(0, 1) == 0 else 'T')
        if lista[n] == 'H':
            heads += 1
            tails = 0
        else:
            tails += 1
            heads = 0
        if heads == 6 or tails == 6:
            streaks += 1
    return True if streaks else False


values = 0
for exp in range(10000):
    values += heads_or_tails(100)

print(f'Chance of streak: {values / 100}%')
