if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        arr = list(map(int, input().split()))

        if sum(arr) == m:
            print('YES')
        else:
            print('NO')