if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, y, a, b = list(map(int, input().split()))
        res = (y - x)/(a + b)
        if res.is_integer():
            print(int(res))
        else:
            print(-1)


