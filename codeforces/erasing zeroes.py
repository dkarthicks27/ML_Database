if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if '1' in s:
            start = s.index('1')
            end = s.rindex('1')
            zero = s.count('0', start, end)
            print(zero)
        else:
            print(0)
