from get_input import get_input
from get_positions import get_positions

def evaluate_antinodes(cache: dict, size1: int, size2: int) -> list[tuple[int, int]]:
    antinodes = []
    for i in cache.keys():
        if len(cache[i]) >= 2:
            for j in cache[i]:
                if j not in antinodes:
                    antinodes.append(j)
                for k in cache[i]:
                    if k != j:
                        r = (j[0] - k[0], j[1] - k[1])
                        a = (j[0] + r[0], j[1] + r[1])
                        while 0 <= a[0] < size1 and 0 <= a[1] < size2:
                            if a not in antinodes:
                                antinodes.append(a)
                            a = (a[0] + r[0], a[1] + r[1])
    return antinodes

if __name__ == "__main__":
    inp = get_input("input")
    pos = get_positions(inp)
    s1 = len(inp)
    s2 = len(inp[0])
    anti = evaluate_antinodes(pos, s1, s2)
    print(len(anti))
