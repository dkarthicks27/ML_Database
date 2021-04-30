if __name__ == '__main__':
    s = input()
    w = input()

    if s == w[::-1]:
        print('YES')
    else:
        print('NO')