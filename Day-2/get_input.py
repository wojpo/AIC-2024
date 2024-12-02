def get_input(filename):
    meow = []
    with open(filename) as f:
        for line in f:
            meow.append(list(map(int, line.strip().split())))
    return meow
