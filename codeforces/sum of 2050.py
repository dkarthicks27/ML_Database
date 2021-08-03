if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2050 != 0:
            print(-1)
        else:
            x = n//2050
            print(sum([int(i) for i in str(x)]))
