if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        a, b = list(map(int, input().split()))
        if a % b == 0:
            print(0)
        else:
            print(b - a % b)


