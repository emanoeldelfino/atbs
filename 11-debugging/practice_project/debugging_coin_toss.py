# Original program:

# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tailŝ:')
#     guess = input()
# toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')


# We can raise exceptions, use assertions, logging or the debugger.

import random
import logging
logging.basicConfig(filename='coin_toss_log.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

flip = ['tails', 'heads']

guess = ''
while guess not in flip:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input(' > ')

# 0 is tails, 1 is heads
toss = flip[random.randint(0, 1)]

if toss == guess:
    logging.debug(f'Same, Toss = {toss}. Guess = {guess}')
    print('You got it!')
else:
    logging.debug(f'Different, Toss = {toss}. Guess = {guess}')

    print('Nope! Guess again!')
    guess = input(' > ')
    while guess not in flip:
        print('Enter heads or tails:')
        guess = input(' > ')

    if toss == guess:
        logging.debug(f'Same, Toss = {toss}. Guess = {guess}')
        print('You got it!')
    else:
        logging.debug(f'Different, Toss = {toss}. Guess = {guess}')
        print('Nope. You are really bad at this game.')
