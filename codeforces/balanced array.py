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
                p = [i*2 for i in range(1, x + 1, 1)] + [i for i in range(1, n-1) if i % 2 == 1] + [(n - 1) + x]
                print(' '.join([str(i) for i in p]))
            else:
                print('NO')
