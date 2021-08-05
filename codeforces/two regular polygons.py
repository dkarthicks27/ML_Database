if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        if (n/m).is_integer():
            print('YES')
        else:
            print('NO')