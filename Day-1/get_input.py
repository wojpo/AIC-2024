def get_input(filename):
    l1 = []
    l2 = []
    with open(filename) as f:
        for line in f:
            l1.append(int(line.strip().split()[0]))
            l2.append(int(line.strip().split()[1]))
    return l1, l2



print(get_input("input"))