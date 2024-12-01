from get_input import get_input

def summarize(l1: list, l2: list) -> int:
    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))

if __name__ == '__main__':
    inp = get_input("input")
    print(summarize(sorted(inp[0]), sorted(inp[1])))

