import collections

from get_input import get_input

def un_answer(cache: dict, update: list):
    valid = True
    for i in range(len(update)):
        if update[i] in cache:
            for c in cache[update[i]]:
                if c in update[i+1:]:
                    valid = False
    if not valid:
        return update


def topological_sort(cache: dict, update: list) -> list:
    s_cache = collections.defaultdict(set)
    r_cache = collections.defaultdict(set)
    for i in update:
        if i in cache:
            for c in cache[i]:
                if c in update:
                    s_cache[i].add(c)
                    r_cache[c].add(i)

    a = {i: len(r_cache[i]) for i in update}
    queue = [page for page in update if a[page] == 0]
    sorted_update = []

    while queue:
        current = queue.pop(0)
        sorted_update.append(current)
        for c in s_cache[current]:
            a[c] -= 1
            if a[c] == 0:
                queue.append(c)

    return sorted_update

def summarize(updates: list, cache: dict) -> int:
    incorrect = []
    ans = 0

    for i in updates:
        if un_answer(cache, i) is not None:
            incorrect.append(un_answer(cache, i))


    for update in incorrect:
        reordered = topological_sort(cache, update)
        u = len(reordered) // 2
        ans += reordered[u]

    return ans

if __name__ == '__main__':
    inp = get_input("input")
    print(summarize(inp[1], inp[0]))
