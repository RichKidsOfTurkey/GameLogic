
def pick_top_players(team):
    team.sort(key=lambda x: x['overall rarity'][0])
    newteam = team[1:]
    return newteam