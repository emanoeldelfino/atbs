# This is a guess the number game.
from random import randint

secretNumber = randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    guess = int(input('Take a guess: '))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print(f'Good job! You guessed my number in {guessesTaken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}')
