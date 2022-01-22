from itertools import zip_longest
from statistics import mode


def grouper(sequence, chunk_size):
    return list(zip_longest(*[iter(sequence)] * chunk_size))


def most_frequent(inlist):
    return max(set(inlist), key=inlist.count)


def lobby_seperator(winner_team_list):
    i = 0
    while i < len(winner_team_list):

        i = i + 1
    print(winner_team_list)
    pass


