if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        h, m = list(map(int, input().split()))
        tot = (24 - h) * 60 - m
        print(tot)
