from re import findall

from get_input import get_input
def replace_char_at_index(s, index, replacement):
    return s[:index] + replacement + s[index + 1:]

def guard_positions(a: list[str]):
    position = None
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    direction_order = ["up", "right", "down", "left"]
    direction = "up"
    for i in range(len(a)):
        if a[i].find("^") != -1:
            position = (i, a[i].find("^"))
            break

    while not position[0] < 0 or position[1] < 0 or position[0] >= len(a) or position[1] >= len(a[0]):
        dir_plus = directions[direction]
        next_pos = (position[0] + dir_plus[0], position[1] + dir_plus[1])
        if a[next_pos[0]][next_pos[1]] == "#":
            direction = direction_order[(direction_order.index(direction) + 1) % 4]
        else:
            a[position[0]] = replace_char_at_index(a[position[0]], position[1], "X")
            position = next_pos
    ans = 0
    for i in range(len(a)):
        ans+= len(findall("X", a[i]))
    return ans

if __name__ == "__main__":
    print(guard_positions(get_input("input")))
