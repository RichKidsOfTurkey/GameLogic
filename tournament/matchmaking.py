import itertools
import json
import random
from tournament.matchmatking_utils import score_comparator, rebound_comparator, steal_comparator, block_comparator, assist_comparator
from tournament.tournament_utils import grouper, split
from gen_team.generate_team import team_making
from collections import Counter


class Tournament:
    def __init__(self, all_players):
        self.paired_lobby = None
        self.pairs = None
        self.lobby = None
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
            # TODO disconnected tie situation remember to calculate it
                winner = 'there is a tie between ' + f'{first_team["team_index"]}' + ' and ' + f'{second_team["team_index"]}'
            # winner = first_team['team_index']

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
        teams = self.power_calculated_teams
        shuf = random.sample(teams, len(teams))
        lobby = grouper(shuf, group_number)
        out = []
        lobby_index = 1
        for i in lobby:
            temp = {
                'lobby_index': lobby_index,
                'lobby': i
            }
            lobby_index = lobby_index + 1
            out.append(temp)
        self.lobby = out
        return out

    def pair_lobby(self):
        lobby = []
        pairs = []
        out = []
        count = 0
        for l in self.lobby:
            lobby.append(l['lobby'])
        for group in lobby:
            for p in itertools.permutations(group, 2):
                pairs.append(p)
            temp = {
                'lobby_index': self.lobby[count]['lobby_index'],
                'pairs': pairs
            }
            out.append(temp)
            count = count + 1
        self.paired_lobby = out
        self.pairs = pairs
        return pairs

    def match_lobby(self):
        print('match lobby is active')
        match_report = []
        total_match_reports = []
        match_index = 1
        for a in self.paired_lobby:
            pairs = a['pairs']
            for p in pairs:
                match = Tournament.match(p[0], p[1])
                overall_winner = match['overall winner']
                match_report.append(match)
                temp_out = {
                    'match_index': match_index,
                    'lobby_index': a['lobby_index'],
                    'overall_winner': overall_winner,
                    'match_report': match_report
                }
                match_index = match_index + 1
                total_match_reports.append(temp_out)

        return total_match_reports

    def get_lobby_scores(self, total_match_results):
        lobby_count = len(self.lobby)
        print('lobby count is---> ', lobby_count)
        temp_sep_lobbies = split(total_match_results, lobby_count)
        sep_lobbies = []
        for a in temp_sep_lobbies:
            sep_lobbies.append(a)
        winners = []
        count = 0
        while count < len(sep_lobbies):
            m = 0
            while m < len(sep_lobbies[count]):
                winners.append(sep_lobbies[count][m]['overall_winner'])
                m = m + 1
            count = count + 1
        scores = {i: winners.count(i) for i in winners}


        return scores
