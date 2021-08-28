if __name__ == '__main__':
    a1, a2, a3, a4 = list(map(int, input().split()))
    if a1 + a2 == a3 + a4 or a1 + a3 == a2 + a4 or a1 + a4 == a2 + a3 or a1 == a2 + a3 + a4 or a2 == a1 + a3 + a4 or a3 == a1 + a2 + a4 or a4 == a1 + a2 + a3:
        print('YES')
    else:
        print('NO')