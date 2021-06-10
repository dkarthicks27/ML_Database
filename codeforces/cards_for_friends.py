if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        w, h, n = list(map(int, input().split()))
        res = 1
        while w % 2 == 0:
            res *= 2
            w = w // 2
        while h % 2 == 0:
            res *= 2
            h = h // 2

        if res >= n:
            print('YES')
        else:
            print('NO')
