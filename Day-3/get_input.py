def get_input(filename) -> str:
    out = ""
    with open(filename) as f:
        for line in f:
           out += line
    return out
