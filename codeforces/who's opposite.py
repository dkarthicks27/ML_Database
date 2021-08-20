if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c = list(map(int, input().split()))
        n = 2 * abs(b - a)
        # print(n)
        if c > n or a > n or b > n:
            print(-1)
        else:
            diff = abs(b - a)
            if c > n // 2:
                print(c - diff)
            else:
                print(c + diff)