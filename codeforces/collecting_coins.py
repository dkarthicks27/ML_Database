if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, n = list(map(int, input().split()))
        max_ele = max(a, b, c)
        diff = max_ele - a + max_ele - b + max_ele - c
        if (n - diff) % 3 == 0 and n - diff >= 0:
            print('YES')
        else:
            print('NO')
