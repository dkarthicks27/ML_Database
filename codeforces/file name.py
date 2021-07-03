import re


if __name__ == '__main__':
    n = int(input())
    x = input()
    pattern = r'x{3,}'
    count = 0
    res = re.findall(pattern, x)
    if not res:
        print(0)
    else:
        for i in res:
            count += len(i) - 2

        print(count)