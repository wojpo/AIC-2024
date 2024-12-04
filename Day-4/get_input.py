def get_input(filename):
    a = []
    with open(filename) as f:
        for line in f:
            a.append(line.strip())
    return a
