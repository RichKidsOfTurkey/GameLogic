import random
import math


# returns a float between 1 and 0
# in this case used as a probability
def percentage_chance():
    chance = random.randint(0, 100)
    return chance / 100


# it rounds number 2.4 --> 2.0 or 2.5 --> 3.0
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier
