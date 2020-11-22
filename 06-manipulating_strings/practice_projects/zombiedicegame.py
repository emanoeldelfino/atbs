import zombiedice
from random import randint

# zombiedice.demo()


class MyZombieExample:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class RandomFirstRoundZombie:

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()  # first roll

        choice = randint(0, 1)

        if choice == 1:
            while diceRollResults is not None:
                diceRollResults = zombiedice.roll()  # roll again


class StopsTwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()  # first roll

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class StopTwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()  # first roll

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class FourTimesStopTwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        totalRolls = randint(1, 4)

        diceRollResults = zombiedice.roll()  # first roll

        shotguns = rolls = 1

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            rolls += 1
            if shotguns < 2 and rolls < totalRolls:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class StopMoreShotgunsBrainZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()  # first roll

        brains = shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if brains <= shotguns:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


zombies = (
    MyZombieExample(name='Zombie Bot Example'),  # F
    RandomFirstRoundZombie(name='Random after 1st roll'),  # F x
    StopsTwoBrainsZombie(name='Stop in 2 brains'),  # F
    StopTwoShotgunsZombie(name='Stop in 2 shotguns'),  # F
    FourTimesStopTwoShotgunsZombie(name='Rolls Four'),
    StopMoreShotgunsBrainZombie(name='More shotguns than brains')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
