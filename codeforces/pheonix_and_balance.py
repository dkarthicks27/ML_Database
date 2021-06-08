if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = [2 ** i for i in range(1, n + 1)]
        if len(x) == 2:
            print(2)
        else:
            print(sum(x[0:n//2 - 1]) + x[-1] - sum((x[n//2 -1:-1])))
