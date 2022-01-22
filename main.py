import itertools
import json
from itertools import permutations

from gen_player.generate_player import PlayerGenerator
from gen_team.generate_team import TeamMaking
from tournament.matchmaking import Tournament


all_players = PlayerGenerator.player_generator(10, 10, 10, 2)
# teams = TeamMaking.generate_teams(all_players)
#
# power_calculated_teams = TeamMaking.calculate_powers(teams)
# print(power_calculated_teams)
# results = Tournament.match(power_calculated_teams[0], power_calculated_teams[1])
# print(results)
# groups = Tournament.create_lobby(power_calculated_teams, 4)
# print(groups[0])
# print(len(groups))

# match_lobby = Tournament.match_lobby(groups)
# print(match_lobby)
# print(len(match_lobby))


temp = Tournament(all_players)
lobby = temp.create_lobby(4)
pairs = temp.pair_lobby()
reports = temp.match_lobby()
temp.get_lobby_scores(reports)
# print(reports)

ex = [[1, 6], [1, 6], [1, 6], [1, 6], [1, 2], [1, 4], [1, 6], [1, 2], [1, 2], [1, 6], [1, 4], [1, 2], [1, 7], [1, 1], [1, 3], [1, 7], [1, 7], [1, 3], [1, 1], [1, 7], [1, 3], [1, 3], [1, 3], [1, 3], [1, 6], [1, 6], [1, 6], [1, 6], [1, 2], [1, 4], [1, 6], [1, 2], [1, 2], [1, 6], [1, 4], [1, 2], [1, 7], [1, 1], [1, 3], [1, 7], [1, 7], [1, 3], [1, 1], [1, 7], [1, 3], [1, 3], [1, 3], [1, 3]]

# with open('storage/match_results.json', 'w') as jsonfile:
#     json.dump(reports, jsonfile, indent=4)


