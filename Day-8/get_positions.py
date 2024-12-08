import collections

def get_positions(l: list) -> dict:
    cache = collections.defaultdict(set)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != '.':
                cache[l[i][j]].add((i,j))
    return cache
