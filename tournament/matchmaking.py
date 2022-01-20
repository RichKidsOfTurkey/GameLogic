import random
from tournament.matchmatking_utils import score_comparator, rebound_comparator, steal_comparator, block_comparator, assist_comparator
from tournament.tournament_utils import grouper
from gen_team.generate_team import team_making


class Tournament:
    def __init__(self, all_players):
        self.groups = None
        self.all_players = all_players
        self.teams = team_making.generate_teams(self.all_players)
        self.power_calculated_teams = team_making.calculate_powers(self.teams)


    @staticmethod
    def match(first_team, second_team):
        winner = None
        score_winner = score_comparator(first_team, second_team)
        rebound_winner = rebound_comparator(first_team, second_team)
        block_winner = block_comparator(first_team, second_team)
        steal_winner = steal_comparator(first_team, second_team)
        assist_winner = assist_comparator(first_team, second_team)
        first_team_total_points = score_winner['team points'][0] + rebound_winner['team points'][0] + block_winner['team points'][0] + steal_winner['team points'][0] + assist_winner['team points'][0]
        second_team_total_points = score_winner['team points'][1] + rebound_winner['team points'][1] + block_winner['team points'][1] + steal_winner['team points'][1] + assist_winner['team points'][1]

        if first_team_total_points > second_team_total_points:
            winner = first_team['team_index']

        elif second_team_total_points > first_team_total_points:
            winner = second_team['team_index']
        elif first_team_total_points == second_team_total_points:
            winner = 'there is a tie between ' + f'{first_team["team_index"]}' + ' and ' + f'{second_team["team_index"]}'

        out = {
            'overall winner': winner,
            'stats': {'score_winner': score_winner,
                      'rebound_winner': rebound_winner,
                      'block_winner': block_winner,
                      'steal_winner': steal_winner,
                      'assist_winner': assist_winner},
            'team who played': [first_team, second_team]
        }

        return out


    def create_lobby(self, group_number):
        print('Create lobby is active')
        teams = self.teams
        shuf = random.sample(teams, len(teams))
        groups = grouper(shuf, group_number)
        self.groups = groups
        return groups

    @staticmethod
    def match_lobby(groups):
        for lobby in groups:
            total_team_count = len(lobby)
            count = 0
            match = []
            pair_teams = grouper(lobby, 2)
            team_numbers = 0
            for pair in pair_teams:
                temp = Tournament.match(pair[0], pair[1])
                match.append(temp)
            return match

    @staticmethod
    def extract_winner_teams(played_matches):
        winner_team_indexes = []
        return None




