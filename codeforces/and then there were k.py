if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        _n = n
        for i in range(n-1, 0, -1):
            if _n & i == 0:
                print(i)
                break
            else:
                _n = _n & i
