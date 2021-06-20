if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 2:
            print('NO')
        else:
            x = n // 2
            if x % 2 == 0:
                print('YES')
                print([i for i in range(2, n//2 + 1, 2)] + [i for i in range(1, n//2, 2)] + [(n - 1) + n // 2])
            else:
                print('NO')
