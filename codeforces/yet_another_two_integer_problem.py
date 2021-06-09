if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = list(map(int, input().split()))
        if a == b:
            print(0)
        elif b > a and b - a > 10:
            if (b - a) % 10 == 0:
                x = 0
            else:
                x = 1
            print((b - a) // 10 + x)
        elif a > b and a - b > 10:
            if (a - b) % 10 == 0:
                x = 0
            else:
                x = 1
            print((a - b) // 10 + x)
        else:
            print(1)
