import json
import random

with open('players/index_allplayers.json', 'r') as jsonfile:
    all_players = json.load(jsonfile)
shuf = random.sample(all_players, len(all_players))
teams = []
while True:
    team = []
    team.append(shuf[0])
    team.append(shuf[1])
    team.append(shuf[2])
    team.append(shuf[3])

    teams.append(team)

    shuf.remove(shuf[0])
    shuf.remove(shuf[1])
    shuf.remove(shuf[2])
    shuf.remove(shuf[3])
    if len(shuf) == 4:
        teams.append(shuf)
        with open('storage/teams.json', 'w') as jsonfile:
            json.dump(teams, jsonfile, indent=4)
            break

