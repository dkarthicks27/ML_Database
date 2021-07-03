def prime(x):
    for j in range(2, x):
        if x % j == 0:
            return 0
    return 1


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    res = 0
    for i in range(n+1, 51):
        if prime(i):
            if i == m:
                res = 1
            break

    if res:
        print('YES')
    else:
        print('NO')
