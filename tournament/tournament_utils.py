from itertools import zip_longest


def grouper(sequence, chunk_size):
    return list(zip_longest(*[iter(sequence)] * chunk_size))


def most_frequent(inlist):
    return max(set(inlist), key=inlist.count)


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


