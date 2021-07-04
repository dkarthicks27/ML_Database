if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        _n, _m = input().split()
        n_arr = list(map(int, input().split()))
        m_arr = list(map(int, input().split()))
        rem = len(set(n_arr).intersection(set(m_arr)))
        print(rem)