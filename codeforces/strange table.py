if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c, x = list(map(int,input().split()))
        r1 = x % r
        if r1 == 0:
            c1 = x // r
            r1 = r
        else:
            c1 = x // r + 1

        res = c * r1 - (c - c1)
        print(res)