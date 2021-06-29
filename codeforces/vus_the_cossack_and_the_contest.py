if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    if m >= n and k >= n:
        print('yes')
    else:
        print('no')