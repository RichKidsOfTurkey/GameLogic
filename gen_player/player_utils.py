import random
from gen_player.math_utils import round_half_up


def rarity_detector(prob):
    output = None
    if prob >= 0.5:
        output = {
            'index': 0,
            'rarity': 'common'
        }
    if 0.5 > prob >= 0.2:
        output = {
            'index': 1,
            'rarity': 'uncommon'
        }
    if 0.2 > prob >= 0.05:
        output = {
            'index': 2,
            'rarity': 'rare'
        }
    if prob < 0.05:
        output = {
            'index': 3,
            'rarity': 'legendary'
        }
    return output


def generate_score(prob):
    index = prob['index']
    score_val = None
    if index == 0:
        # it means common
        temp = random.randint(150, 855)/100
        score_val = temp
    if index == 1:
        temp = random.randint(855, 1560)/100
        score_val = temp
    if index == 2:
        temp = random.randint(1560, 2265)/100
        score_val = temp
    if index == 3:
        temp = random.randint(2265, 2970)/100
        score_val = temp
    return score_val


def generate_rebound(prob):
    index = prob['index']
    rebound_val = None
    if index == 0:
        # it means common
        temp = random.randint(0, 378) / 100
        rebound_val = temp
    if index == 1:
        temp = random.randint(378, 755) / 100
        rebound_val = temp
    if index == 2:
        temp = random.randint(755, 1133) / 100
        rebound_val = temp
    if index == 3:
        temp = random.randint(1133, 1510) / 100
        rebound_val = temp
    return rebound_val


def generate_block(prob):
    index = prob['index']
    block_val = None
    if index == 0:
        # it means common
        temp = random.randint(0, 65) / 100
        block_val = temp
    if index == 1:
        temp = random.randint(70, 140) / 100
        block_val = temp
    if index == 2:
        temp = random.randint(140, 210) / 100
        block_val = temp
    if index == 3:
        temp = random.randint(210, 280) / 100
        block_val = temp
    return block_val


def generate_steal(prob):
    index = prob['index']
    steal_val = None
    if index == 0:
        # it means common
        temp = random.randint(0, 65) / 100
        steal_val = temp
    if index == 1:
        temp = random.randint(65, 110) / 100
        steal_val = temp
    if index == 2:
        temp = random.randint(110, 155) / 100
        steal_val = temp
    if index == 3:
        temp = random.randint(155, 200) / 100
        steal_val = temp
    return steal_val


def generate_assist(prob):
    index = prob['index']
    assist_val = None
    if index == 0:
        # it means common
        temp = random.randint(30, 273) / 100
        assist_val = temp
    if index == 1:
        temp = random.randint(273, 515) / 100
        assist_val = temp
    if index == 2:
        temp = random.randint(515, 758) / 100
        assist_val = temp
    if index == 3:
        temp = random.randint(758, 1000) / 100
        assist_val = temp
    return assist_val


def index_config(number):
    out = None
    number = round_half_up(number)
    if number == 0:
        out = 'common'
    if number == 1:
        out = 'uncommon'
    if number == 2:
        out = 'rare'
    if number == 3:
        out = 'legendary'

    return out
