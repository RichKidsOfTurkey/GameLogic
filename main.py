from gen_player.generate_player import PlayerGenerator
from gen_team.generate_team import TeamMaking
from tournament.matchmaking import Tournament


all_players = PlayerGenerator.player_generator(1600, 1200, 800, 20)
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
print(temp.create_lobby(2)[0])


