import re
from itertools import repeat

def take(elem):
    return elem[0]


def largeGroupPositions(s):
    pattern = rf'\w{{3,}}'
    un = []
    x = re.finditer(pattern, s)
    if x:
        for m in x:
            print(m)
            un.append([m.start(), m.end() - 1])
        # un.append([x.start(), x.end() - 1])

    un.sort()
    print(un)


if __name__ == '__main__':
    inp = "nnnhaaannnm"
    largeGroupPositions(inp)
