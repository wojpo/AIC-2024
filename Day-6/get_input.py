def get_input(filename: str) -> list[str]:
    inp = []
    with open(filename) as f:
        for line in f:
            inp.append(line.strip())
    return inp
