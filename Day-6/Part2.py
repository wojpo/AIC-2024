import copy

from get_input import get_input
from Part1 import replace_char_at_index

def check_loop(a: list[str]):
    position = None
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    direction_order = ["up", "right", "down", "left"]
    direction = "up"
    find_guard = False
    for i in range(len(a)):
        if a[i].find("^") != -1:
            position = (i, a[i].find("^"))
            find_guard = True
            break
    if not find_guard:
        return False
    visited_pos = []
    while not position[0] < 0 or position[1] < 0 or position[0] >= len(a) or position[1] >= len(a[0]):
        if [position, direction] in visited_pos:
            return True
        dir_plus = directions[direction]
        next_pos = (position[0] + dir_plus[0], position[1] + dir_plus[1])
        try:
            if a[next_pos[0]][next_pos[1]] == "#":
                direction = direction_order[(direction_order.index(direction) + 1) % 4]
            else:
                visited_pos.append([position, direction])
                position = next_pos
        except IndexError:
            return False
    return False

def summarize(a: list[str]):
    ans = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            m = copy.deepcopy(a)
            m[i] = replace_char_at_index(m[i], j, "#")
            print(ans)
            if check_loop(m):
                ans += 1

if __name__ == "__main__":
    print(summarize(get_input("input")))