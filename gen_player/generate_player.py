from tqdm import tqdm
import names
from gen_player.player_utils import rarity_detector, index_config,generate_assist, generate_score, generate_rebound, generate_block, generate_steal
from gen_player.math_utils import percentage_chance
# 0.0 to 0.05 legendary
# 0.05 to 0.20 rare
# 0.20 to 0.50 uncommon
# 0.50 to 1.00 common


class PlayerGenerator:
    def __init__(self):
        # initializing probabilities for later use in player_generator()
        self.score_prob = percentage_chance()
        self.rebound_prob = percentage_chance()
        self.block_prob = percentage_chance()
        self.steal_prob = percentage_chance()
        self.assist_prob = percentage_chance()

        self.score_quality = rarity_detector(self.score_prob)
        self.rebound_quality = rarity_detector(self.rebound_prob)
        self.block_quality = rarity_detector(self.block_prob)
        self.steal_quality = rarity_detector(self.steal_prob)
        self.assist_quality = rarity_detector(self.assist_prob)

        self.score_values = generate_score(self.score_quality)
        self.rebound_values = generate_rebound(self.rebound_quality)
        self.block_values = generate_block(self.block_quality)
        self.steal_values = generate_steal(self.steal_quality)
        self.assist_values = generate_assist(self.assist_quality)
        overall_rarity_value = (self.score_quality['index'] + self.rebound_quality['index'] + self.block_quality['index'] + self.steal_quality['index'] + self.assist_quality['index'])/5
        rarity_name = index_config(overall_rarity_value)
        self.overall_rarity = [overall_rarity_value, rarity_name]
        self.name = names.get_first_name()

    def get_player(self):
        player = {
            'overall rarity': self.overall_rarity,
            'player name': self.name,
            'score': self.score_values,
            'rebound': self.rebound_values,
            'block': self.block_values,
            'steal': self.steal_values,
            'assist': self.assist_values
        }
        return player

    @staticmethod
    def generate_common_player(count):
        print('generate common player active')
        local_count = 0
        common_players = []
        while local_count < count:
            temp_obj = PlayerGenerator()
            player = temp_obj.get_player()
            with tqdm(total=count) as pbar:
                pbar.set_description('Common players generating')
                pbar.update(local_count)
            if player['overall rarity'][1] == 'common':
                common_players.append(player)
                local_count = local_count + 1

        return common_players

    @staticmethod
    def generate_uncommon_player(count):
        print('generate uncommon player active')
        local_count = 0
        uncommon_players = []
        while local_count < count:
            temp_obj = PlayerGenerator()
            player = temp_obj.get_player()
            with tqdm(total=count) as pbar:
                pbar.set_description('Uncommon players generating')
                pbar.update(local_count)
            if player['overall rarity'][1] == 'uncommon':
                uncommon_players.append(player)
                local_count = local_count + 1

        return uncommon_players

    @staticmethod
    def generate_rare_player(count):
        print('generate rare player active')
        local_count = 0
        rare_players = []
        while local_count < count:
            temp_obj = PlayerGenerator()
            player = temp_obj.get_player()
            with tqdm(total=count) as pbar:
                pbar.set_description('Rare players generating')
                pbar.update(local_count)
            if player['overall rarity'][1] == 'rare':
                rare_players.append(player)
                local_count = local_count + 1

        return rare_players

    @staticmethod
    def generate_legendary_player(count):
        print('generate legendary player active')
        local_count = 0
        legendary_players = []
        while local_count < count:

            with tqdm(total=count, leave=True, position=0) as pbar:
                pbar.set_description('Legendary players generating')
                pbar.update(local_count)
            temp_obj = PlayerGenerator()
            player = temp_obj.get_player()
            if player['overall rarity'][1] == 'legendary':
                legendary_players.append(player)
                local_count = local_count + 1

        return legendary_players

    @staticmethod
    def player_generator(common_count, uncommon_count, rare_count, legendary_count):
        common_players = PlayerGenerator().generate_common_player(common_count)
        uncommon_players = PlayerGenerator().generate_uncommon_player(uncommon_count)
        rare_players = PlayerGenerator().generate_rare_player(rare_count)
        legendary_players = PlayerGenerator().generate_legendary_player(legendary_count)
        all_players = common_players + uncommon_players + rare_players + legendary_players
        index = 1
        for player in all_players:
            player['player_index'] = index
            index = index + 1

        return all_players


# test = PlayerGenerator()
# test_out = test.player_generator(1600, 1200, 800, 2)
# print(test_out)





