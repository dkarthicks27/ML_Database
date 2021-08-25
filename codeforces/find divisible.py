if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        print(l, 2*l)