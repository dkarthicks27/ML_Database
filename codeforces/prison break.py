if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = list(map(int, input().split()))
        print(a*b)