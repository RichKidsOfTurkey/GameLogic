from gen_player.generate_player import PlayerGenerator
from gen_team.generate_team import TeamMaking
from tournament.matchmaking import Tournament



all_players = PlayerGenerator.player_generator(10, 10, 10, 2)
teams = TeamMaking.generate_teams(all_players)

power_calculated_teams = TeamMaking.calculate_powers(teams)
print(power_calculated_teams)
results = Tournament.match(power_calculated_teams[0], power_calculated_teams[1])

print(results)
