if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a, b, c, d = list(map(int, input().split()))
        if a != d:
            print(a, d)
        elif a != c:
            print(a, c)
        elif b != c:
            print(b, c)
        else:
            print(b, d)
