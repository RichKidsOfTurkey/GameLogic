import json


with open('storage/teams.json', 'r') as jsonfile:
    teams = json.load(jsonfile)


def pick_top_players(team):
        team.sort(key=lambda x: x['overall rarity'][0])
        newteam = team[1:]
        return newteam

match_teams = []
for team in teams:
    temp = pick_top_players(team)
    match_teams.append(temp)

# with open('matchteams.json', 'w') as jsonfile:
#     json.dump(match_teams, jsonfile, indent=4)


with open('storage/matchteams.json', 'r') as jsonfile:
    teams = json.load(jsonfile)
print(len(teams[0]))
