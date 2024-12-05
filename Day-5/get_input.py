import collections

def get_input(filename: str) -> tuple[dict, list]:
    a = collections.defaultdict(set)
    b = []
    with open(filename) as f:
        for i in f:
            if "|" in i.strip():
                meow = list(map(int, i.strip().split("|")))
                a[meow[1]].add(meow[0])
            elif "," in i.strip():
                b.append(list(map(int, i.strip().split(","))))
    return a, b
