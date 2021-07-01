if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, n = list(map(int, input().split()))
        if a > n or b > n:
            print(0)
        else:
            d = a + b
            c = max(a, b)
            a = d
            b = c
            count = 1
            while d <= n:
                d = a + b
                c = max(a, b)
                a = d
                b = c
                count += 1

            print(count)