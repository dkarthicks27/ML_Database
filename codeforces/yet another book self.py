import re

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = ''.join(input().split())

        # building a pattern
        pattern = r'(?=(10+1))'
        x = re.findall(pattern, arr)
        # print(arr, list(x))
        tot = 0
        if list(x):
            for i in list(x):
                tot += i.count('0')

        print(tot)