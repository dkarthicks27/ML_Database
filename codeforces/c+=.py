if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, n = list(map(int, input().split()))
        r = n // (a + b)
        print(r)