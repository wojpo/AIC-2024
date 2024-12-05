from get_input import get_input

def answer(cache: dict, update: list):
    valid = True
    for i in range(len(update)):
        if update[i] in cache:
            for c in cache[update[i]]:
                if c in update[i+1:]:
                    return None
    return update

def summarize(updates: list, cache: dict) -> int:
    correct = []
    ans = 0
    for i in updates:
        if answer(cache, i) is not None:
            correct.append(answer(cache, i))
    for i in correct:
        u = len(i) // 2
        ans += i[u]
    return ans

if __name__ == '__main__':
    inp = get_input("input")
    print(summarize(inp[1], inp[0]))
