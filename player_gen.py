import json
import random
import math
import jsonify
import names

# 0.0 to 0.05 legendary
# 0.05 to 0.20 rare
# 0.20 to 0.50 uncommon
# 0.50 to 1.00 common


def percentage_chance():
    chance = random.randint(0,100)
    return chance/100


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


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


def generate_player():
    chance_count = 0
    chances = []
    while chance_count < 5:
        temp = percentage_chance()
        chances.append(temp)
        chance_count = chance_count + 1

    score_q = rarity_detector(chances[0])
    score = generate_score(score_q)

    rebound_q = rarity_detector(chances[1])
    rebound = generate_rebound(rebound_q)

    block_q = rarity_detector(chances[2])
    block = generate_block(block_q)

    steal_q = rarity_detector(chances[3])
    steal = generate_steal(steal_q)

    assist_q = rarity_detector(chances[4])
    assist = generate_assist(assist_q)

    overall_rarity = (score_q['index'] + rebound_q['index'] + block_q['index'] + steal_q['index'] + assist_q['index'])/5
    rarity_name = index_config(overall_rarity)

    out_player = {
        'overall rarity': [overall_rarity, rarity_name],
        'name': names.get_first_name(),
        'score': [score_q['rarity'], score],
        'rebound': [rebound_q['rarity'], rebound],
        'block': [block_q['rarity'], block],
        'steal': [steal_q['rarity'], steal],
        'assist': [assist_q['rarity'], assist]
    }
    return json.dumps(out_player, indent=4)
count = 0
players = []
# while True:
#     print(count)
#     player = json.loads(generate_player())
#     anan = player['overall rarity'][1]
#     if anan == 'uncommon':
#         print(player)
#         players.append(player)
#         count = count + 1
#     if count == 1200:
#         with open('players/uncommon.json', 'w') as jsonfile:
#             json.dump(players, jsonfile, indent=4)
#             break
# with open('legendary.json', 'r') as jsonfile:
#     data = json.load(jsonfile)
# print(len(data))
