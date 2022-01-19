
def score_comparator(teamone, teamtwo):
    winner_team_index = None
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_score'] > teamtwo['team_score']:
        winner_team_index = teamone['team_index']
        teamone_point = teamone_point + 1
    elif teamone['team_score'] < teamtwo['team_score']:
        winner_team_index = teamtwo['team_index']
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_score'] == teamtwo['team_score']:
        teamone_point = 0
        teamtwo_point = 0
        winner_team_index = 'it`s a tie'
    temp = {
        'winner_team_index': winner_team_index,
        'team points': [teamone_point, teamtwo_point]
    }
    return temp


def rebound_comparator(teamone, teamtwo):
    winner_team_index = None
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_rebound'] > teamtwo['team_rebound']:
        winner_team_index = teamone['team_index']
        teamone_point = teamone_point + 1
    elif teamone['team_rebound'] < teamtwo['team_rebound']:
        winner_team_index = teamtwo['team_index']
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_rebound'] == teamtwo['team_rebound']:
        teamone_point = 0
        teamtwo_point = 0
        winner_team_index = 'it`s a tie'

    temp = {
        'winner_team_index': winner_team_index,
        'team points': [teamone_point, teamtwo_point]
    }
    return temp


def block_comparator(teamone, teamtwo):
    winner_team_index = None
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_block'] > teamtwo['team_block']:
        winner_team_index = teamone['team_index']
        teamone_point = teamone_point + 1
    elif teamone['team_block'] < teamtwo['team_block']:
        winner_team_index = teamtwo['team_index']
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_block'] == teamtwo['team_block']:
        teamone_point = 0
        teamtwo_point = 0
        winner_team_index = 'it`s a tie'

    temp = {
        'winner_team_index': winner_team_index,
        'team points': [teamone_point, teamtwo_point]
    }
    return temp


def steal_comparator(teamone, teamtwo):
    winner_team_index = None
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_steal'] > teamtwo['team_steal']:
        winner_team_index = teamone['team_index']
        teamone_point = teamone_point + 1
    elif teamone['team_steal'] < teamtwo['team_steal']:
        winner_team_index = teamtwo['team_index']
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_steal'] == teamtwo['team_steal']:
        teamone_point = 0
        teamtwo_point = 0
        winner_team_index = 'it`s a tie'

    temp = {
        'winner_team_index': winner_team_index,
        'team points': [teamone_point, teamtwo_point]
    }
    return temp


def assist_comparator(teamone, teamtwo):
    winner_team_index = None
    teamone_point = 0
    teamtwo_point = 0
    if teamone['team_assist'] > teamtwo['team_assist']:
        winner_team_index = teamone['team_index']
        teamone_point = teamone_point + 1
    elif teamone['team_assist'] < teamtwo['team_assist']:
        winner_team_index = teamtwo['team_index']
        teamtwo_point = teamtwo_point + 1
    elif teamone['team_assist'] == teamtwo['team_assist']:
        teamone_point = 0
        teamtwo_point = 0
        winner_team_index = 'it`s a tie'

    temp = {
        'winner_team_index': winner_team_index,
        'team points': [teamone_point, teamtwo_point]
    }
    return temp