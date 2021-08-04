if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p, a, b, c = list(map(int, input().split()))
        a = (a - p % a) % a
        b = (b - p % b) % b
        c = (c - p % c) % c
        print(min(a, b, c))
