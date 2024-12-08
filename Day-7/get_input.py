def get_input(filename: str) -> list:
    inp = []
    with open(filename) as f:
        for i in f:
             inp.append([int(i.strip().split(":")[0]), list(map(int, i.strip().split(":")[1].split()))])
    return inp
