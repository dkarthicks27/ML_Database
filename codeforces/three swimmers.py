if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p, a, b, c = list(map(int, input().split()))
        print(min(a, b, c) - p)