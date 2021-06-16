import re
from itertools import repeat


def largeGroupPositions(s):
    k = set(s)
    un = []
    for i in k:
        pattern = rf'{i}{{3,}}'
        x = re.search(pattern, s)
        if x:
            un.append([x.start(), x.end() - 1])

    print(un)


if __name__ == '__main__':
    inp = "abbxxxxzzy"
    largeGroupPositions(inp)
