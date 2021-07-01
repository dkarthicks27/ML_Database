import re

if __name__ == '__main__':
    n = int(input())
    arr = []
    count = 0
    targ = False
    for _ in range(n):
        x = input()
        if count == 0:
            pattern = r'OO'
            res = re.search(pattern, x)
            if res:
                x = x.replace('OO', '++', 1)
                count = 1
                targ = True
                arr.append(x)
            else:
                arr.append(x)
        else:
            arr.append(x)

    if targ:
        print('YES')
        for i in arr:
            print(i)
    else:
        print('NO')