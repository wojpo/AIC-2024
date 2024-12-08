def get_input(filename: str) -> list:
    inp = []
    with open(filename) as f:
        for i in f:
            inp.append(i.strip())
    return inp
