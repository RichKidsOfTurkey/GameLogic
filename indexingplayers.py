import json


with open('players/legendary.json', 'r') as jsonfile:
    legendary_players = json.load(jsonfile)
with open('players/rare.json', 'r') as jsonfile:
    rare_players = json.load(jsonfile)
with open('players/uncommon.json', 'r') as jsonfile:
    uncommon_players = json.load(jsonfile)
with open('players/common.json', 'r') as jsonfile:
    common_players = json.load(jsonfile)

all_players = legendary_players + rare_players + uncommon_players + common_players

index = 1

for player in all_players:
    player['index'] = index
    index = index + 1

with open('players/index_allplayers.json', 'w') as jsonfile:
    json.dump(all_players, jsonfile, indent=4)


