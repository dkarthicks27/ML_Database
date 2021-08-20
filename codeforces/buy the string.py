if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, c0, c1, h = list(map(int, input().split()))
        binString = input()
        z = binString.count('0')
        o = binString.count('1')
        price = min(o * c1 + z * c0, n * c1 + z * h, n * c0 + o * h)
        print(price)