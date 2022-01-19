import random
from gen_team.team_utils import pick_top_players


class TeamMaking:

    @staticmethod
    def generate_teams(players):
        generated_teams = []
        if len(players) % 4 != 0:
            print('player count is not divisible by 4 so can not generate equal teams')
        shuf = random.sample(players, len(players))
        while True:
            team = [shuf[0], shuf[1], shuf[2], shuf[3]]
            generated_teams.append(team)
            shuf.remove(shuf[0])
            shuf.remove(shuf[1])
            shuf.remove(shuf[2])
            shuf.remove(shuf[3])
            if len(shuf) == 0:
                return generated_teams
            if len(shuf) == 4:
                generated_teams.append(shuf)
                return generated_teams

    @staticmethod
    def generate_match_teams(teams):
        match_teams = []
        # picking top 3 player for matchmaking later on
        # top 3 player is hardcoded in pick_top_players()
        for team in teams:
            temp = pick_top_players(team)
            match_teams.append(temp)

        return match_teams

    @staticmethod
    def calculate_powers(match_teams):
        indexed_teams = []
        team_index = 1
        for team in match_teams:
            team_score = team[0]['score'] + team[1]['score'] + team[2]['score']
            team_rebound = team[0]['rebound'] + team[1]['rebound'] + team[2]['rebound']
            team_block = team[0]['block'] + team[1]['block'] + team[2]['block']
            team_steal = team[0]['steal'] + team[1]['steal'] + team[2]['steal']
            team_assist = team[0]['assist'] + team[1]['assist'] + team[2]['assist']
            team_rarity_average =(team[0]['overall rarity'][0] + team[1]['overall rarity'][0] + team[2]['overall rarity'][0]) / 3
            temp_out = {
                'team_index': team_index,
                'team_overall_rarity_average': round(team_rarity_average, 3),
                'team_score': round(team_score, 2),
                'team_rebound': round(team_rebound, 2),
                'team_block': round(team_block, 2),
                'team_steal': round(team_steal, 2),
                'team_assist': round(team_assist, 2),
                'team': team
            }
            indexed_teams.append(temp_out)
            team_index = team_index + 1

        return indexed_teams
