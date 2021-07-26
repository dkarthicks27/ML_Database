import math


def isSquare(x):
    if not math.sqrt(x).is_integer():
        return 1
    return 0


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        val = 0
        for i in arr:
            if isSquare(i):
                val = 1
                break

        if val:
            print('YES')
        else:
            print('NO')
