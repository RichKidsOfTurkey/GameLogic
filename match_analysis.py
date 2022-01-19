import json

with open('first_matchesplayed.json', 'r') as jsonfile:
    winner_index = json.load(jsonfile)

with open('index_match_teams.json', 'r') as jsonfile:
    teams = json.load(jsonfile)

with open('team_powers.json', 'r') as jsonfile:
    team_powers = json.load(jsonfile)

first = winner_index[1]
anan = teams[first]
count = 0
for a in teams:
    if a['index'] in winner_index:
        team_overall_rarity = 0.0
        for player in a['team']:
            team_overall_rarity = team_overall_rarity + (player['overall rarity'][0])
            if team_overall_rarity / 3 > 1.0:
                count = count + 1


#
# print(count)
print(teams[653])
print(teams[207])


