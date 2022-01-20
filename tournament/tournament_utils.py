from itertools import zip_longest


def grouper(sequence, chunk_size):
    return list(zip_longest(*[iter(sequence)] * chunk_size))

