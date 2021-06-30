if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if set(a).intersection(set(b)):
            print('YES')
            print(1, list(set(a).intersection(set(b)))[0])
        else:
            print('NO')
