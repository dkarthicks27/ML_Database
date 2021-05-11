if __name__ == '__main__':
    n, k = list(map(int, input().split()))

    for _ in range(k):
        if n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            n = n - 1
        elif int(str(n)[-1]) == 0:
            n = n // 10
        else:
            n = n - 1

    print(n)