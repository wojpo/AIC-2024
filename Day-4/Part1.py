import re
from get_input import get_input

def check_xmas(l: list[str]) -> int:
    ans = 0
    vertical = [""] * len(l[0])
    for i in range(len(l)):
        for j in range(len(l[i])):
            vertical[j] += l[i][j]

    for i in range(len(l) - 3):
        for j in range(len(l[i]) - 3):
            a = l[i][j] + l[i + 1][j + 1] + l[i + 2][j + 2] + l[i + 3][j + 3]
            if a == "XMAS" or a == "SAMX":
                ans += 1

    for i in range(len(l) - 3):
        for j in range(3, len(l[i])):
            a = l[i][j] + l[i + 1][j - 1] + l[i + 2][j - 2] + l[i + 3][j - 3]
            if a == "XMAS" or a == "SAMX":
                ans += 1

    for i in l:
        ans += len(re.findall("XMAS", i))
        ans += len(re.findall("XMAS", i[::-1]))
    for i in vertical:
        ans += len(re.findall("XMAS", i))
        ans += len(re.findall("XMAS", i[::-1]))

    return ans

if __name__ == "__main__":
    print(check_xmas(get_input("input")))
