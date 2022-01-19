import json
import random
from itertools import zip_longest


with open('index_match_teams.json', 'r') as jsonfile:
    match_teams = json.load(jsonfile)


def team_power_calculator(teams):
    out = []
    for team in teams:
        team_score = 0
        team_rebound = 0
        team_block = 0
        team_steal = 0
        team_assist = 0
        for player in team['team']:
            team_score = team_score + player['score'][1]
        for player in team['team']:
            team_rebound = team_rebound + player['rebound'][1]
        for player in team['team']:
            team_block = team_block + player['block'][1]
        for player in team['team']:
            team_steal = team_steal + player['steal'][1]
        for player in team['team']:
            team_assist = team_assist + player['assist'][1]

        team_power = {
            'team_index': team['index'],
            'team_score': team_score,
            'team_rebound': team_rebound,
            'team_block': team_block,
            'team_steal': team_steal,
            'team_assist': team_assist
        }
        out.append(team_power)
    return out


def score_comparator(teamone, teamtwo):
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_score'] > teamtwo['team_score']:
        teamone_point = teamone_point + 1
    elif teamone['team_score'] < teamtwo['team_score']:
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_score'] == teamtwo['team_score']:
        teamone_point = 0
        teamtwo_point = 0
    return teamone_point, teamtwo_point


def rebound_comparator(teamone, teamtwo):
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_rebound'] > teamtwo['team_rebound']:
        teamone_point = teamone_point + 1
    elif teamone['team_rebound'] < teamtwo['team_rebound']:
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_rebound'] == teamtwo['team_rebound']:
        teamone_point = 0
        teamtwo_point = 0
    return teamone_point, teamtwo_point


def block_comparator(teamone, teamtwo):
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_block'] > teamtwo['team_block']:
        teamone_point = teamone_point + 1
    elif teamone['team_block'] < teamtwo['team_block']:
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_block'] == teamtwo['team_block']:
        teamone_point = 0
        teamtwo_point = 0
    return teamone_point, teamtwo_point


def steal_comparator(teamone, teamtwo):
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_steal'] > teamtwo['team_steal']:
        teamone_point = teamone_point + 1
    elif teamone['team_steal'] < teamtwo['team_steal']:
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_steal'] == teamtwo['team_steal']:
        teamone_point = 0
        teamtwo_point = 0
    return teamone_point, teamtwo_point


def assist_comparator(teamone, teamtwo):
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_assist'] > teamtwo['team_assist']:
        teamone_point = teamone_point + 1
    elif teamone['team_assist'] < teamtwo['team_assist']:
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_assist'] == teamtwo['team_assist']:
        teamone_point = 0
        teamtwo_point = 0
    return teamone_point, teamtwo_point


def match(teamone, teamtwo):
    winner = None
    score_winner = score_comparator(teamone, teamtwo)
    rebound_winner = rebound_comparator(teamone, teamtwo)
    block_winner = block_comparator(teamone, teamtwo)
    steal_winner = steal_comparator(teamone, teamtwo)
    assist_winner = assist_comparator(teamone, teamtwo)

    teamone_point = score_winner[0] + rebound_winner[0] + block_winner[0] + steal_winner[0] + assist_winner[0]
    teamtwo_point = score_winner[1] + rebound_winner[1] + block_winner[1] + steal_winner[1] + assist_winner[1]

    if teamone_point > teamtwo_point:
       winner = teamone['team_index']

    elif teamtwo_point > teamone_point:
        winner = teamtwo['team_index']
    elif teamone_point == teamtwo_point:
        winner = 'there is a tie between ' + f'{teamone["team_index"]}' + ' and ' + f'{teamtwo["team_index"]}'
    temp_out = {
        'winner team index': winner,
        'stats': {'score_winner': score_winner,
                  'rebound_winner': rebound_winner,
                  'block_winner': block_winner,
                  'steal_winner': steal_winner,
                  'assist_winner': assist_winner},
        'team who played': [teamone, teamtwo]
    }
    return temp_out


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def tournament(match_teams):
    team_powers = team_power_calculator(match_teams)
    shuf = random.sample(team_powers, len(team_powers))
    coupled_teams = []
    for first_team, second_team in grouper(shuf, 2):
        coup = [first_team, second_team]
        coupled_teams.append(coup)

    match_results = []
    for m in coupled_teams:
        match_results.append(match(m[0], m[1]))

    return match_results




anan = tournament(match_teams)

team_powers = team_power_calculator(match_teams)
# winner_indexes = []
# for aa in anan:
#     winner_indexes.append(aa['winner team index'])
#

tarrt = match(team_powers[653], team_powers[207])
print(tarrt)


