import re
from get_input import get_input

def part2(inp: str) -> int:
    inp = inp.split("mul")
    enabled = True
    ans = 0
    for i in inp:
        if re.findall("^\\(", i) and enabled:
            ind = i.find(")")
            if 5 <= ind <= 9 and ',' in i:
                a = i[1:ind].split(',')
                ans += int(a[0])*int(a[1])
        if re.findall("don\'t\\(\\)", i):
            enabled = False
        if re.findall("do\\(\\)", i):
            enabled = True
    return ans

if __name__ == "__main__":
    print(part2(get_input("input")))
