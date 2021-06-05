if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        l, b = list(map(int, input().split()))
        print(min(max(2*l, b), max(l, 2*b)) ** 2)
