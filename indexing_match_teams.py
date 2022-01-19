import json


with open('storage/matchteams.json', 'r') as jsonfile:
    match_teams = json.load(jsonfile)
out = []
index = 1

for team in match_teams:
    anan = {'index': index,
            'team_score': team}
    index = index + 1
    out.append(anan)
# with open('index_match_teams.json', 'w') as jsonfile:
#     json.dump(out, jsonfile, indent=4)

for team in match_teams:
    team_score = 0
    team_rebound = 0
    team_block = 0
    team_steal = 0
    team_assist = 0

    temp = {'index': index,
            'team_score': team_score,
            'team_rebound': team_rebound,
            'team_block': team_block,
            'team_steal': team_steal,
            'team_assist': team_assist
            }




