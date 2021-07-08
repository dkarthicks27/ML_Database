if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n > 30:
            if n - 30 not in [6, 10, 14]:
                print('YES')
                print(6, 10, 14, n - 30)
            else:
                print('YES')
                print(6, 10, 15, n - 31)

        else:
            print('NO')